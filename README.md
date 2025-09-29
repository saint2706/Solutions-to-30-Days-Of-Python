# Coding for MBA

A guided collection of Python, analytics, and machine learning exercises designed for business-minded learners. Each `Day_XX_*` folder contains focused lessons, scripts, or notebooks that build toward practical data fluency.

## Prerequisites

- Python 3.10 or later
- `pip` for installing Python packages
- A virtual environment tool such as `venv` or `conda`
- (Optional) Google Chrome or another modern browser for exploring visualizations

To create a local environment:

```bash
git clone https://github.com/your-username/Coding-For-MBA.git
cd Coding-For-MBA
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
```

## Run the Day 30 Web Scraper

The refreshed Day 30 script now separates HTTP access from HTML parsing, which makes it easier to test and extend. To execute the scraper:

```bash
python Day_30_Web_Scraping/web_scraping.py
```

The command-line interface reports connection status, shows a preview of the scraped data, and prints summary statistics generated from the cleaned price column.

## Practice Responsible Scraping

The project uses the `books.toscrape.com` sandbox, but the same etiquette applies to production websites:

- Read the site's terms of service and `robots.txt` before scraping.
- Identify your requests with a User-Agent string and keep the frequency reasonable.
- Add delays between requests when crawling multiple pages.
- Avoid collecting personal or sensitive information without consent.

## Run the Automated Tests

Pytest now includes coverage for the Day 30 parser, using deterministic HTML fixtures to verify the DataFrame schema and summary statistics. Execute the full suite or focus on the new tests with:

```bash
pytest tests/test_day_30.py
```

## Repository Layout

- `Day_01_Introduction` … `Day_50_MLOps` – daily folders covering Python, analytics, and machine learning topics.
- `tests/` – lightweight unit tests for selected lessons.
- `requirements.txt` – Python dependencies used across the curriculum.

## Contributing

Issues and pull requests are welcome. Please include tests and documentation updates alongside code changes.
