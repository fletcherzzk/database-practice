# Important file: CHECK development.md for how I implemented each step.


# What your app does and why you chose it 
A movie recommender, I chose it because I have got a really good dataset and it is relatively simple, allowing me to focus on technical details more

# What you store in the database:
1. where the data came from : Hugging Face Datasets, imdb_top_1000.csv
2. what counts as one item : An item is an overview of a movie.
3. how you broke it up if you did: No need to break up, natural units.
4. roughly how many items you loaded: 1000 items
5. what metadata (if any) you attach to each one list including overview, rating, release year

# How a user adds new items, and how a user searches

1. Adding New Movies
Users can add new movies by running main.py and selecting 1. Add a movie from the CLI menu. The program asks for the movie's title, release year, genre, plot overview, and IMDb rating (optional). After receiving the information, the application automatically generates an embedding for the overview and stores it in ChromaDB along with the movie's metadata. Newly added movies are saved persistently and remain available after restarting the application.

2. Searching for Movies
Users can search for movies by selecting 2. Search movies and entering a natural-language description of the type of movie they want to watch. The application first uses semantic search to retrieve the 15 most relevant movies from the database.

1. Users can then choose one of four ranking methods:
Semantic Similarity: Rank movies by embedding distance.
IMDb Rating: Prioritize movies with higher IMDb ratings.
Release Year: Prioritize more recently released movies.
Keyword Overlap: Prioritize movies whose plot overviews share more keywords with the query.

2. After re-ranking the 15 candidates, the application displays the top five recommendations, including their titles, release years, genres, IMDb ratings, plot overviews, semantic distances, and relevance scores.

The relevance score is calculated using a shifted exponential mapping of the semantic distance. It provides a more readable display of similarity but does not represent the probability of a correct recommendation.


# Testing with query:

Query with: A masked hero faces a dangerous criminal who terrorizes an entire city, challenging his courage and moral principles.

## Sorting with semantic similarity:
Rank 1
Title: Wreck-It Ralph
Year: 2012
Genre: Animation, Adventure, Comedy
IMDb Rating: 7.7
Semantic Distance: 1.0468
Relevance Score: 74.56/100
Keyword Overlap: 1
Overview: A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives.

Rank 2
Title: Dirty Harry
Year: 1971
Genre: Action, Crime, Thriller
IMDb Rating: 7.7
Semantic Distance: 1.0518
Relevance Score: 73.81/100
Keyword Overlap: 1
Overview: When a madman calling himself "the Scorpio Killer" menaces the city, tough-as-nails San Francisco Police Inspector "Dirty" Harry Callahan is assigned to track down and ferret out the crazed psychopath.

Rank 3
Title: Lat sau san taam
Year: 1992
Genre: Action, Crime, Thriller
IMDb Rating: 7.8
Semantic Distance: 1.0778
Relevance Score: 70.08/100
Keyword Overlap: 0
Overview: A tough-as-nails cop teams up with an undercover agent to shut down a sinister mobster and his crew.

Rank 4
Title: Ang-ma-reul bo-at-da
Year: 2010
Genre: Action, Crime, Drama
IMDb Rating: 7.8
Semantic Distance: 1.0825
Relevance Score: 69.42/100
Keyword Overlap: 0
Overview: A secret agent exacts revenge on a serial killer through a series of captures and releases.

Rank 5
Title: The Dark Knight
Year: 2008
Genre: Action, Crime, Drama
IMDb Rating: 9.0
Semantic Distance: 1.0941
Relevance Score: 67.83/100
Keyword Overlap: 0
Overview: When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.


## sorting with IMDB rating:
Rank 1
Title: The Dark Knight
Year: 2008
Genre: Action, Crime, Drama
IMDb Rating: 9.0
Semantic Distance: 1.0941
Relevance Score: 67.83/100
Keyword Overlap: 0
Overview: When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.
(Nolan is the GOAT!!!!)

Rank 2
Title: Se7en
Year: 1995
Genre: Crime, Drama, Mystery
IMDb Rating: 8.6
Semantic Distance: 1.1289
Relevance Score: 63.26/100
Keyword Overlap: 0
Overview: Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.

Rank 3
Title: The Dark Knight Rises
Year: 2012
Genre: Action, Adventure
IMDb Rating: 8.4
Semantic Distance: 1.1369
Relevance Score: 62.26/100
Keyword Overlap: 1
Overview: Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City from the brutal guerrilla terrorist Bane.

Rank 4
Title: Batman Begins
Year: 2005
Genre: Action, Adventure
IMDb Rating: 8.2
Semantic Distance: 1.1002
Relevance Score: 67.01/100
Keyword Overlap: 1
Overview: After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from corruption.

Rank 5
Title: Zootopia
Year: 2016
Genre: Animation, Adventure, Comedy
IMDb Rating: 8.0
Semantic Distance: 1.1216
Relevance Score: 64.20/100
Keyword Overlap: 1
Overview: In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.

Note: Relevance Score is a display metric,
not a probability of a correct recommendation.

#  sorting with released year
Rank 1
Title: Zootopia
Year: 2016
Genre: Animation, Adventure, Comedy
IMDb Rating: 8.0
Semantic Distance: 1.1216
Relevance Score: 64.20/100
Keyword Overlap: 1
Overview: In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.

Rank 2
Title: Wreck-It Ralph
Year: 2012
Genre: Animation, Adventure, Comedy
IMDb Rating: 7.7
Semantic Distance: 1.0468
Relevance Score: 74.56/100
Keyword Overlap: 1
Overview: A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives.

Rank 3
Title: The Dark Knight Rises
Year: 2012
Genre: Action, Adventure
IMDb Rating: 8.4
Semantic Distance: 1.1369
Relevance Score: 62.26/100
Keyword Overlap: 1
Overview: Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City from the brutal guerrilla terrorist Bane.

Rank 4
Title: Ang-ma-reul bo-at-da
Year: 2010
Genre: Action, Crime, Drama
IMDb Rating: 7.8
Semantic Distance: 1.0825
Relevance Score: 69.42/100
Keyword Overlap: 0
Overview: A secret agent exacts revenge on a serial killer through a series of captures and releases.

Rank 5
Title: Watchmen
Year: 2009
Genre: Action, Drama, Mystery
IMDb Rating: 7.6
Semantic Distance: 1.1446
Relevance Score: 61.32/100
Keyword Overlap: 0
Overview: In 1985 where former superheroes exist, the murder of a colleague sends active vigilante Rorschach into his own sprawling investigation, uncovering something that could completely change the course of history as we know it.


# sorting with keyword:
Rank 1
Title: Wreck-It Ralph
Year: 2012
Genre: Animation, Adventure, Comedy
IMDb Rating: 7.7
Semantic Distance: 1.0468
Relevance Score: 74.56/100
Keyword Overlap: 1
Overview: A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives.

Rank 2
Title: Dirty Harry
Year: 1971
Genre: Action, Crime, Thriller
IMDb Rating: 7.7
Semantic Distance: 1.0518
Relevance Score: 73.81/100
Keyword Overlap: 1
Overview: When a madman calling himself "the Scorpio Killer" menaces the city, tough-as-nails San Francisco Police Inspector "Dirty" Harry Callahan is assigned to track down and ferret out the crazed psychopath.

Rank 3
Title: Batman Begins
Year: 2005
Genre: Action, Adventure
IMDb Rating: 8.2
Semantic Distance: 1.1002
Relevance Score: 67.01/100
Keyword Overlap: 1
Overview: After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from corruption.

Rank 4
Title: Zodiac
Year: 2007
Genre: Crime, Drama, Mystery
IMDb Rating: 7.7
Semantic Distance: 1.1012
Relevance Score: 66.87/100
Keyword Overlap: 1
Overview: In the late 1960s/early 1970s, a San Francisco cartoonist becomes an amateur detective obsessed with tracking down the Zodiac Killer, an unidentified individual who terrorizes Northern California with a killing spree.

Rank 5
Title: Zootopia
Year: 2016
Genre: Animation, Adventure, Comedy
IMDb Rating: 8.0
Semantic Distance: 1.1216
Relevance Score: 64.20/100
Keyword Overlap: 1
Overview: In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.

Note: Relevance Score is a display metric,
not a probability of a correct recommendation.

# one-sentence explanation search 
IMDB and Semantic works well even if this query is a bit vague
Release year also works
Although keyword search indeed works. However, the keyword itself is not a good idea for searching. As we can see that the keyword overlap is "city".






# Downloading and Loading the Dataset
The original dataset is not included in this repository. To reproduce the database:
1. Visit the [IMDb Movies Dataset on Hugging Face](https://huggingface.co/datasets/drossi/EDA_on_IMDB_Movies_Dataset).
2. Download the `imdb_top_1000.csv` file.
(Or using the link https://drive.google.com/file/d/1pXs1Kbzn5cqtX3cG6-tdmtH3Q7D-VwSQ/view?usp=sharing)
3. Place the CSV file in the project root directory, alongside `main.py` and `load_data.py`.
4. Install ChromaDB if it is not already installed:

   ```bash
   pip install chromadb==1.5.9
   ```

5. Run the data-loading script:

   ```bash
   python load_data.py
   ```

6. Once the data has been loaded, start the application:

   ```bash
   python main.py
   ```

The `load_data.py` script reads movie overviews from the CSV file and inserts them into a persistent ChromaDB collection named `imdb_movies`. Each movie is stored as a separate document, with its title, release year, genre, and IMDb rating saved as metadata.

The database is stored locally in the `chroma_store/` directory, which is automatically created and does not need to be committed to GitHub.




## Vector Database and Embedding Model

This project uses **ChromaDB (version 1.5.9)** as its vector database and the default **all-MiniLM-L6-v2** embedding model.

The embedding model converts movie plot overviews and user queries into numerical vectors.

The model runs locally and is automatically downloaded and cached by ChromaDB when embeddings are generated for the first time. An internet connection may therefore be required on the first run. Subsequent runs can reuse the cached model.

The movie database is stored persistently in the local `chroma_store/` directory.



## Installation and Running

**Requirements:** Python 3 and an internet connection for the initial setup.

1. Download the project repository and open a terminal in the project root directory.

2. Install ChromaDB:

   ```bash
   python -m pip install chromadb==1.5.9
   ```

3. Download `imdb_top_1000.csv` from the [IMDb dataset on Hugging Face](https://huggingface.co/datasets/drossi/EDA_on_IMDB_Movies_Dataset) or from (https://drive.google.com/file/d/1pXs1Kbzn5cqtX3cG6-tdmtH3Q7D-VwSQ/view?usp=sharing) and place it in the project root directory.

4. Load the movie dataset:

   ```bash
   python load_data.py
   ```

   This creates the persistent ChromaDB collection and imports the movie overviews and metadata. The dataset only needs to be loaded once.

5. Start the application:

   ```bash
   python main.py
   ```

6. Follow the CLI menu to add movies, search for recommendations, or exit the application.

The application automatically saves newly added movies. When restarting the program, users can access previously stored movies without reloading the dataset.

On Windows, `py` can be used instead of `python` if necessary.



# Citation:
    1. The last 3 sections and How a user adds new items, and how a user searches section are written by AI 
    2. I did chekck it and at a path to .csv file on my google-drive
    3. I used chatgpt 6-sol model for this problem.



