
import chromadb
import uuid
import math
import re

# Connect to the persistent database
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="imdb_movies")

# Search settings
CANDIDATE_COUNT = 15
DISPLAY_COUNT = 5

# Exponential relevance score settings
K = 2.0
DISTANCE_BASELINE = 0.9

# Common words excluded from keyword overlap
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at",
    "to", "for", "of", "with", "by", "from", "is", "are",
    "was", "were", "be", "been", "being", "who", "which",
    "that", "this", "his", "her", "their", "its", "he",
    "she", "they", "it", "as", "into", "through", "while"
}


def relevance_score(distance):
    """Map semantic distance to a display score from 0 to 100."""
    adjusted_distance = max(0.0, distance - DISTANCE_BASELINE)
    return 100 * math.exp(-K * adjusted_distance)


def extract_keywords(text):
    """Extract meaningful lowercase words from text."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return set(words) - STOP_WORDS


def keyword_overlap(query, overview):
    """Count shared meaningful words between query and overview."""
    query_words = extract_keywords(query)
    overview_words = extract_keywords(overview)

    return len(query_words & overview_words)


def add_movie():
    """Add a new movie to the persistent database."""
    print("\n=== Add a Movie ===")

    title = input("Movie title: ").strip()
    year = input("Release year: ").strip()
    genre = input("Genre: ").strip()
    overview = input("Movie overview: ").strip()

    if not title or not overview:
        print("Title and overview cannot be empty.")
        return

    rating_input = input(
        "IMDb rating (leave blank if unknown): "
    ).strip()

    try:
        rating = float(rating_input) if rating_input else 0.0
    except ValueError:
        print("Invalid rating. Using 0.0.")
        rating = 0.0

    if not 0.0 <= rating <= 10.0:
        print("Rating must be between 0 and 10.")
        return

    movie_id = "custom_" + str(uuid.uuid4())

    collection.add(
        ids=[movie_id],
        documents=[overview],
        metadatas=[{
            "title": title,
            "year": year,
            "genre": genre,
            "rating": rating
        }]
    )

    print("\nMovie added successfully!")
    print("Total movies:", collection.count())


def get_year(movie):
    """Convert release year to an integer for sorting."""
    year = str(movie["year"])

    try:
        return int(year)
    except ValueError:
        return 0


def get_rating(movie):
    """Return IMDb rating or 0 if unavailable."""
    try:
        return float(movie["rating"])
    except (ValueError, TypeError):
        return 0.0


def rank_movies(movies, mode):
    """Re-rank the 15 candidates according to user preference."""

    if mode == "2":
        # Higher IMDb rating first, distance breaks ties
        return sorted(
            movies,
            key=lambda m: (-get_rating(m), m["distance"])
        )

    elif mode == "3":
        # Newer movies first, distance breaks ties
        return sorted(
            movies,
            key=lambda m: (-get_year(m), m["distance"])
        )

    elif mode == "4":
        # More keyword overlap first, distance breaks ties
        return sorted(
            movies,
            key=lambda m: (-m["keyword_overlap"], m["distance"])
        )

    else:
        # Smaller semantic distance first
        return sorted(
            movies,
            key=lambda m: m["distance"]
        )


def search_movies():
    """Search movies and allow the user to choose a ranking mode."""
    print("\n=== Search Movies ===")

    query = input("Describe the movie you want: ").strip()

    if not query:
        print("Query cannot be empty.")
        return

    count = collection.count()

    if count == 0:
        print("The database is empty.")
        return

    # Stage 1: Semantic retrieval of the nearest 15 movies
    results = collection.query(
        query_texts=[query],
        n_results=min(CANDIDATE_COUNT, count)
    )

    movies = []

    for i in range(len(results["ids"][0])):
        metadata = results["metadatas"][0][i]
        overview = results["documents"][0][i]
        distance = results["distances"][0][i]

        movie = {
            "title": metadata.get("title", "Unknown"),
            "year": metadata.get("year", "Unknown"),
            "genre": metadata.get("genre", "Unknown"),
            "rating": metadata.get("rating", 0.0),
            "overview": overview,
            "distance": distance,
            "keyword_overlap": keyword_overlap(query, overview)
        }

        movies.append(movie)

    # Stage 2: User-selected re-ranking
    print("\n=== Ranking Options ===")
    print("1. Semantic Similarity (default)")
    print("2. IMDb Rating (highest first)")
    print("3. Release Year (newest first)")
    print("4. Keyword Overlap (most shared words first)")

    mode = input("Choose ranking method (1-4): ").strip()

    if mode not in {"1", "2", "3", "4"}:
        print("Invalid choice. Using Semantic Similarity.")
        mode = "1"

    ranked_movies = rank_movies(movies, mode)

    mode_names = {
        "1": "Semantic Similarity",
        "2": "IMDb Rating",
        "3": "Release Year",
        "4": "Keyword Overlap"
    }

    print("\n" + "=" * 60)
    print("Query:", query)
    print("Ranking:", mode_names[mode])
    print("Candidates searched:", len(movies))
    print("=" * 60)

    # Display the top 5 after re-ranking
    for i, movie in enumerate(ranked_movies[:DISPLAY_COUNT]):
        score = relevance_score(movie["distance"])

        print(f"\nRank {i + 1}")
        print("Title:", movie["title"])
        print("Year:", movie["year"])
        print("Genre:", movie["genre"])

        rating = get_rating(movie)
        print(
            "IMDb Rating:",
            rating if rating > 0 else "Unknown"
        )

        print(f"Semantic Distance: {movie['distance']:.4f}")
        print(f"Relevance Score: {score:.2f}/100")
        print("Keyword Overlap:", movie["keyword_overlap"])
        print("Overview:", movie["overview"])

    print("\nNote: Relevance Score is a display metric,")
    print("not a probability of a correct recommendation.")


def main():
    while True:
        print("\n=== Semantic Movie Recommender ===")
        print("Total movies:", collection.count())
        print("1. Add a movie")
        print("2. Search movies")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movie()

        elif choice == "2":
            search_movies()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
