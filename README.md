# 📰 Hacker News Daily Scraper

A simple Python script that scrapes the top headline from [Hacker News](https://news.ycombinator.com/) and appends it to a text file every time you start your computer.

Perfect for:
- Practicing web scraping
- Automating small daily scripts
- Learning how to run Python scripts at startup on Windows

---

## 🚀 Setup Instructions

### 1. Clone the Repo

    git clone https://github.com/your-username/Webscraper.git
    cd Webscraper
### 2. Create & Activate Virtual Environment

    python -m venv .venv
    .\.venv\Scripts\activate
    3. Install Dependencies

    pip install -r requirements.txt
### 4. Test the Scraper
Run manually to make sure everything works:

    python src/main.py
    Check data/headlines.txt for results.

## ⚙️ Run on Windows Startup (Optional)
Want it to scrape automatically every time you turn on your computer? Follow these steps:

### ✅ Step 1: Create Your Batch File
Copy scripts/run_scraper_template.bat to run_scraper.bat in the same folder.

Open it and replace the file path with the path to your local project folder.

    :: Replace this with your actual path
    cd C:\Users\YourName\Documents\Webscraper
    call .venv\Scripts\activate.bat
    python src\main.py
    Save the file.

### ✅ Step 2: Add to Task Scheduler
Press Win + S → Search for "Task Scheduler"

Click "Create Basic Task…"

Name it something like: HackerNewsScraper

Set the trigger to: "When I log on"

Set the action to: "Start a program"

Browse and select the run_scraper.bat file you just created

(Optional) Add a delay: Right-click task → Properties → Triggers → Edit → Delay by 1 minute

Now every time you start your PC, the scraper will run and log the latest top headline from Hacker News.

