Following steps from the instructions

Step 1:
Store movie summary and allow queries to different movies
Since each item is just a summary of 2-3 sentences, no need to break down even more
The user query a movie and returns the rank and the summary.

Realstic queries
1. A masked hero faces a dangerous criminal who terrorizes an entire city, challenging his courage and moral principles.
2. A mysterious vigilante struggles to maintain peace while confronting an unpredictable enemy who spreads fear throughout the city.
Expected match: The Dark Knight

Irrelevant query:
I want to learn how to cook pasta with tomatoes and cheese.


Step2:
ChromaDB initialized successfully!
Number of documents: 0

Step3: 
collection.count() still reports your items, good

Step 4:
Each movie's overview is treated as a single document without further chunking, since the overviews are short and there are  natural units already.
(Study note: chunk determines embedding and similarity in meaning)

Note:
Following the note in the example code" you probably don't want to re-embed your whole dataset each time the user 
runs the program, so the next few lines aren't *necessarily* what you should do." I asked AI to avoid re-embed

Complete:
Checked 1000 movies
Total documents: 1000
Elapsed time: 25.77 seconds


Step 5:
Works: Irrelevent search indeed gets a much larger distance, dark knight was given for the first query with low distance

Interesting observation: "A mysterious vigilante struggles to maintain peace while confronting an unpredictable enemy who spreads fear throughout the city." 
This does not really match with Dark Knight, because vigilante happens to be a keyword of a another movie.
(Too many movies with similar plot, also notifies the problem of not giving specific queries)


Step 6:
Test case: Project Hail Mary
Release year: 2026
Genre: Sci-Fi, Adventure
Movie overview: A science teacher awakens alone aboard a spacecraft with no memory of his mission. He must investigate a mysterious threat to Earth's sun and cooperate with an unexpected extraterrestrial companion to prevent a global catastrophe.

Query: A researcher stranded far from home must work with an alien friend to stop a cosmic disaster.

Works!!!!








