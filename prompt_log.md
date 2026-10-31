I used chatgpt 6-Sol, the web version this time.


prompt 1:
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

// collection.add(
//    documents=movies,
//    ids=[str(i) for i in range(len(movies))]
//)

print("Number of documents:", collection.count())
这样？



prompt2:
**Decide what one item is (i.e. how big each chunk will be if you're breaking up a larger piece of text).** A whole book is a terrible item, and not for the reason you might guess: Chroma's default embedding model reads only the first 256 word pieces of whatever you hand it and **silently discards the rest**. Store a three-hundred-page document as one item and you have effectively stored its first paragraph. A paragraph or a section is usually about right. If your source has natural units already (an abstract, a plot summary, a review), use those &#x20;
这个影响怎么切分document对吧？


prompt3:
Chunk 就是语义关联的核心对吗？


prompt4:
每个电影的dictlist里面的其他信息其实应该算是补充信息，overview是关联语义的核心，这么理解对吗？



prompt5:
import csv

with open("imdb_top_1000.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for i, row in enumerate(reader):
        print(row["Series_Title"])
        print(row["Overview"])
        print(row["IMDB_Rating"])
        print()

        if i == 2:
            break
这个实现了只读overview？




prompt6:
step 4需要的code给我



prompt7:
- **Add in batches, not one call per item.** `collection.add()` takes lists. Passing a few hundred documents in one call is dramatically faster than looping and calling it a few hundred times.

啥意思



prompt 8:
`collection.add()`   为什么没用这个？




prompt 9:
# Store the foods. Chroma automatically turns each document into an embedding
# (a list of numbers that represents its meaning) using the embedding model.
# "upsert" means "update or insert": running this program again replaces these
# items instead of adding duplicate copies of them.  Note that for your project
# you probably don't want to re-embed your whole dataset each time the user 
# runs the program, so the next few lines aren't *necessarily* what you should 
# do.
这个问题对应哪个？


prompt 10:
最后优化的时候其实可以map一下distance，放大一下差距



prompt 11:
Realstic queries
1. A masked hero faces a dangerous criminal who terrorizes an entire city, challenging his courage and moral principles.
2. A mysterious vigilante struggles to maintain peace while confronting an unpredictable enemy who spreads fear throughout the city.
Expected match: The Dark Knight
再测一下这两个


prompt 12:
Step 7: 加入一下功能：
1 指数映射展示分数
 
2 每次查找15个，然后用
   IMDb Rating 辅助排序
   年份辅助排序
   关键词重合度排序
  允许用户自己选择