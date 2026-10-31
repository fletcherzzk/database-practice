
import csv
import time
import chromadb

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="imdb_movies")

documents = []
metadatas = []
ids = []

with open("imdb_top_1000.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for i, row in enumerate(reader):
        overview = row["Overview"].strip()

        if not overview:
            continue

        documents.append(overview)
        metadatas.append({
            "title": row["Series_Title"],
            "year": row["Released_Year"],
            "genre": row["Genre"],
            "rating": float(row["IMDB_Rating"])
        })
        ids.append(f"imdb_{i}")

# Initially test 50 movies, then change this to 1000.
LIMIT = 1000
BATCH_SIZE = 1000

start = time.time()

for i in range(0, min(LIMIT, len(ids)), BATCH_SIZE):
    end = min(i + BATCH_SIZE, LIMIT, len(ids))

    batch_ids = ids[i:end]

    # Find which movies have already been stored.
    existing_ids = set(collection.get(ids=batch_ids)["ids"])

    new_indices = [
        j for j in range(i, end)
        if ids[j] not in existing_ids
    ]

    if new_indices:
        collection.add(
            documents=[documents[j] for j in new_indices],
            metadatas=[metadatas[j] for j in new_indices],
            ids=[ids[j] for j in new_indices]
        )

    print(f"Checked {end} movies")

print("Total documents:", collection.count())
print(f"Elapsed time: {time.time() - start:.2f} seconds")
