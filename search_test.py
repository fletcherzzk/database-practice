
import chromadb

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="imdb_movies")

print("Total movies:", collection.count())

queries = [
    "A masked hero faces a dangerous criminal who terrorizes an entire city, challenging his courage and moral principles.",
    "A mysterious vigilante struggles to maintain peace while confronting an unpredictable enemy who spreads fear throughout the city.",
    "I want to learn how to cook pasta with tomatoes and cheese."
]

results = collection.query(
    query_texts=queries,
    n_results=5
)

for i, query in enumerate(queries):
    print("\n" + "=" * 60)
    print(f"Query {i + 1}: {query}")
    print("=" * 60)

    for j in range(len(results["ids"][i])):
        print(f"\nRank {j + 1}")
        print("Title:", results["metadatas"][i][j]["title"])
        print("Distance:", results["distances"][i][j])
        print("Overview:", results["documents"][i][j])

    print()
