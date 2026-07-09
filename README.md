# API Intelligence Agent



# Repository Structure

```text
.
├── data
│   └── apps.csv
│
├── outputs
│   └── results.csv
│
├── src
│   ├── coordinator.py
│   ├── research_agent.py
│   ├── scraper.py
│   ├── llm_service.py
│   ├── models.py
│   ├── storage.py
│   ├── insights.py
│   ├── report_generator.py
│   └── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

# Tech Stack

* Python
* Requests
* BeautifulSoup4
* Groq API
* Pydantic
* Pandas
* python-dotenv

---

# Installation

Clone the repository

```bash
git clone https://github.com/Themonk20/Composio-Product-Scraper.git

cd Composio-Product-Scraper
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\\Scripts\\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Running the Project

Run the pipeline

```bash
python src/main.py
```

The pipeline will:

* Read applications from `data/apps.csv`
* Scrape documentation
* Extract structured information
* Save results into

```text
outputs/results.csv
```





