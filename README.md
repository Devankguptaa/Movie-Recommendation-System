# 🎬 BingeBuddy – Movie Recommendation System  

BingeBuddy is a **Streamlit-based movie recommendation system** that suggests movies similar to the one you like.  
It uses **content-based filtering with cosine similarity** on movie metadata and fetches posters dynamically from **TMDB API**.  

🚀 Live Demo: [BingeBuddy on Render](https://bingebuddy-annp.onrender.com/)  
🐳 Docker Image: [Docker Hub – devankgg/movie-recommender](https://hub.docker.com/repository/docker/devankgg/movie-recommender/general)  

---

## 📂 Project Structure  

```
.
├── app.py                # Streamlit app for deployment
├── notebook.ipynb        # Jupyter notebook (EDA + model building)
├── requirements.txt      # Project dependencies
├── Dockerfile            # Docker configuration
├── tmdb_5000_movies.csv  # Movie dataset
├── tmdb_5000_credits.csv # Credits dataset
├── movie_dict.pkl        # Preprocessed movie dictionary
├── similarity.pkl        # Cosine similarity matrix
├── .env                  # Stores TMDB_API_KEY (not pushed to GitHub)
└── .gitignore
```

---

## ⚡ Features  

- Search for any movie and get **top 5 similar recommendations**  
- Fetches **movie posters** using TMDB API  
- Built using **Content-Based Filtering (Cosine Similarity)**  
- Interactive **Streamlit UI**  
- Dockerized for easy deployment  

---

## 🛠️ Tech Stack  

- **Python** (Streamlit, Pandas, Scikit-learn, NumPy, Requests)  
- **TMDB API** for fetching posters  
- **Docker** for containerization  
- **Render** for cloud deployment  

---

## ▶️ Run Locally  

Clone the repo:  
```bash
git clone https://github.com/Devankguptaa/binge-buddy.git
cd binge-buddy
```

Create a virtual environment & install dependencies:  
```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your **TMDB API Key**:  
```
TMDB_API_KEY=your_api_key_here
```

Run the app:  
```bash
streamlit run app.py
```

App will be live at:  
```
http://localhost:8501
```

---

## 🐳 Run with Docker  

Pull the image:  
```bash
docker pull devankgg/movie-recommender
```

Run the container:  
```bash
docker run -p 8501:8501 -e TMDB_API_KEY=your_api_key_here devankgg/movie-recommender
```

Visit:  
```
http://localhost:8501
```

---

## 📸 Screenshots  

| Home Page | Recommendations |
|-----------|-----------------|
| ![Home](https://via.placeholder.com/400x250?text=Home+Page) | ![Recommendations](https://via.placeholder.com/400x250?text=Recommendations+Page) |

👉 Replace placeholders with actual screenshots from your Streamlit app.  

---

## 📊 Dataset  

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
- Includes `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`  

---

## ✨ Future Improvements  

- Add **hybrid filtering** (content + collaborative)  
- Enhance **UI/UX**  
- Add **genre/actor filtering options**  
- Implement **user history–based personalization**  

---

## 👨‍💻 Author  

**Devank Gupta**  
- 🌐 [Render Deployment](https://bingebuddy-annp.onrender.com/)  
- 🐳 [Docker Hub](https://hub.docker.com/repository/docker/devankgg/movie-recommender/general)  

---
