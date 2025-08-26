# Stage 04 — Data Acquisition & Ingestion (auto-generated notes)

**Timestamp:** 2025-08-26T10:01:00.312100

## API ingestion
- Preferred source: Alpha Vantage (CSV) using `TIME_SERIES_DAILY_ADJUSTED` endpoint.
- Fallback: `yfinance` Python package.
- Config / env:
  - .env (local, not committed): API_KEY (Alpha Vantage key), TICKER (e.g., AAPL)
  - .env.example is present in repo root.
- Example Alpha Vantage params used:
  - function=TIME_SERIES_DAILY_ADJUSTED, symbol=AAPL, outputsize=compact, datatype=csv
- Validations performed:
  - check presence of a date/timestamp column and convert to datetime
  - check for numeric columns: open, high, low, close, volume (or nearest variants)
  - report NA counts and DataFrame shape
- Output file: data/raw/api_{source}_AAPL_20250826-1000.csv

## Scraping ingestion
- Source URL: https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
- Table: S&P 500 constituents (table id='constituents' or first wikitable sortable)
- Validation:
  - required columns: Symbol, Security
  - check NA counts and shape
- Output file: data/raw/scrape_wikipedia_sp500_constituents_20250826-1000.csv

## Assumptions & Risks
- Alpha Vantage has rate limits (5 calls/minute for free tier). Use API key responsibly.
- Wikipedia's HTML structure can change; the scraper uses common selectors and falls back to generic table selection.
- Do NOT commit `.env` with real API keys. Use `.env.example` in your repo.
- Data freshness depends on API / source availability.

## Files created by this run
- API CSV, scrape CSV in `data/raw/`
- diagnostics text files in `data/raw/`
- ingestion log: c:\Users\sarda\Desktop\bootcamp_darshit_sarda\homework\data\raw\ingestion_log_20250826-1000.txt
