import chromadb

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="movies")

movies = [
    "A superhero protects a city from a dangerous criminal.",
    "A prisoner develops a friendship and hopes for freedom.",
    "A powerful crime family struggles with loyalty and succession.",
    "A group of astronauts travels through space to save humanity.",
    "A detective investigates a mysterious series of murders.",
    "A young wizard discovers a hidden world of magic.",
    "A group of friends embarks on a dangerous adventure.",
    "A soldier struggles to survive during a devastating war.",
    "A scientist creates a machine that can travel through time.",
    "A lonely robot explores an abandoned planet."
]

# collection.add(
#    documents=movies,
#    ids=[str(i) for i in range(len(movies))]
#)

print("Number of documents:", collection.count())