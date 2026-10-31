
import chromadb
import uuid

# Connect to the existing persistent database
client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="imdb_movies")


def add_movie():
    # Get movie information from the user
    title = input("Movie title: ").strip()
    year = input("Release year: ").strip()
    genre = input("Genre: ").strip()
    overview = input("Movie overview: ").strip()

    # Validate required fields
    if not title or not overview:
        print("Title and overview cannot be empty.")
        return

    # Generate a unique ID
    movie_id = "custom_" + str(uuid.uuid4())

    # Add the movie to ChromaDB
    collection.add(
        ids=[movie_id],
        documents=[overview],
        metadatas=[{
            "title": title,
            "year": year,
            "genre": genre,
            "rating": 0.0
        }]
    )

    print("\nMovie added successfully!")
    print("Total movies:", collection.count())


def search_movies():
    query = input("Describe the movie you want: ").strip()

    if not query:
        print("Query cannot be empty.")
        return

    results = collection.query(
        query_texts=[query],
        n_results=min(5, collection.count())
    )

    for i in range(len(results["ids"][0])):
        metadata = results["metadatas"][0][i]

        print(f"\nRank {i + 1}")
        print("Title:", metadata["title"])
        print("Year:", metadata["year"])
        print("Genre:", metadata["genre"])
        print("Distance:", results["distances"][0][i])
        print("Overview:", results["documents"][0][i])


def main():
    while True:
        print("\n=== Semantic Movie Recommender ===")
        print("1. Add a movie")
        print("2. Search movies")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movie()
        elif choice == "2":
            if collection.count() == 0:
                print("The database is empty.")
            else:
                search_movies()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
