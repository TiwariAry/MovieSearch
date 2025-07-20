<img width="1919" height="1002" alt="Screenshot 2025-07-21 002114" src="https://github.com/user-attachments/assets/e6b39854-7e07-4b71-91d4-6a4978be25a0" /># 🎬 MovieSearch
**A Smart Movie Recommendation App Without Machine Learning**

**MovieSearch** is a full-stack web application that recommends the **top 5 movies** similar to the one entered by the user using a simple yet effective **Bag-of-Words technique**. Built **without any machine learning** library, it uses intelligent text similarity matching and leverages **real-time data from TheMovieDB API** for movie metadata.

🌐 **Live App**: [MovieSearch](https://moviesearch-boli.onrender.com)  
<br/>

---

## 🍿 Features

- 🔍 **Search** for any movie by typing its name
- ✏️ **Auto-completion** for movie titles using fuzzy matching
- 🎞️ Movie results include:
  - Title
  - Description (via TheMovieDB API)
  - Poster image (via TheMovieDB API)
- 🌄 Dynamic background that changes based on:
  - 🌙 Time of Day (Morning, Afternoon, Evening, Night)
  - 📍 User Location (via browser)

---

## 🧱 Tech Stack

| Frontend       | Backend       | Recommendation Logic  | External API        | UI Feature       |
|----------------|---------------|-----------------------|---------------------|------------------|
| HTML, CSS, JS  | Python (Flask)| Bag-of-Words (TextSim)| TheMovieDB          | Time- Based BG   |
|                | Jinja2        | Fuzzy Matching        | IP-based Geolocation|                  |

---

## 🧠 Colab Notebook

Bag of words technique was used to acheive the results.
📓 [Google Colab Notebook]()

---

## 🌿 System Overview



---

## 🗂️ Project Structure

```bash
MovieSearch/
├── static/                   # Static assets (CSS, JS, Backgrounds)
│   └── image/                # Time-based folders (morning, afternoon, evening, night)
│   └── autocomplete.js       # Responsible for auto-completion
│   └── background_setter.js  # Responsible for dynamic background setting
│   └── index_style.css       # Home page styling
│   └── result_style.css      # Result page styling
├── templates/                # HTML templates (Home, Result)
├── app.py                    # Flask backend logic
├── recommender.py            # Responsible for recommendation logic and providing movies detailes (Name, icon, info)
├── movie_names.csv           # Contains all movies names
├── Finalized_file.csv        # Contains the processed file from colab
├── similarity.npy            # Contains similarity value [0-1] of every movie with every other movie
├── requirements.txt          # Python dependencies
└── README.md                 # You're here!
```

---

## ⚙️ How It Works

### 🧠 Movie Similarity (No ML)
1. User enters a movie title.
2. Auto-correction fixes spelling errors using **fuzzy logic**.
3. Backend processes request using a **Bag-of-Words** technique.
4. **Top 5 most similar movies** are selected from dataset.
5. Metadata (overview + poster) is fetched from **TMDB API**.
6. Results are shown with **dynamic background**.

### 🌇 Background Image Logic
1. Browser detects user’s IP address and local time.
2. Script checks current time:
   - 🌅 Morning (6–12)
   - ☀️ Afternoon (12–17)
   - 🌆 Evening (17–20)
   - 🌃 Night (20–6)
3. Background image is picked from the corresponding folder.

---

## 🛠️ Installation & Setup

### 📦 Prerequisites
- Python 3.9+
- Flask
- An API key from TheMovieDB

---

### 🔌 Clone the Repo

```bash
git clone https://github.com/your-username/MovieSearch.git
cd MovieSearch
```

---

### ⚙️ Setup Instructions

#### 1. Configure Backend
```bash
pip install -r requirements.txt
```

#### 2. Set API key
Create a `.env` file:
```
TMDB_API_KEY=your_tmdb_api_key
```

#### 3. Run the App
```bash
python app.py
```

## 🧠 Learnings & Highlights

- Designed a non-ML movie recommendation system using Bag-of-Words
- Implemented real-time spell correction with fuzzy matching
- Used TheMovieDB API to enrich results with live data
- Built a dynamic day/night themed UI based on local time and location
- Developed a modular, scalable Flask application structure

---

## 📈 Future Enhancements

- 🔐 Add user login and personalized recommendations
- 🗑️ Clear history or save favorite movies
- 🔍 Search by genre or actor
- 🌐 Improve location detection using browser geolocation

---

## 🤝 Contributing

**Pull requests are welcome!** For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License



---

## 👨‍💻 Author

**Aryan Tiwari**  
📫 [LinkedIn](https://www.linkedin.com/in/aryan-tiwari-6844a9250)  
💻 [GitHub](https://github.com/TiwariAry)

---
