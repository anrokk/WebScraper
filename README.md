# WebScraper

## Description

A web scraper created in the Advanced Python course in TalTech. This project uses Scrapy to extract product data from an Estonian e-commerce store and stores it in an SQLite database. A Flask-based web application allows users to query and display the data.

The products.json file is also in the repository. Please delete it before going through the setup procedure

## Setup

1. Install scrapy (if not already installed):
```bash
pip install scrapy
```
2. Run the scrapy spider to collect product data:
```bash
cd scraper
scrapy crawl ifit_spider -o products.json
```
3. Initialize the database and import the scraped data:
```bash
cd database
python database_setup.py
```
4. Start the web application:
```bash
cd web
python app.py
```
The app will be available at:
```bash
http://127.0.0.1:5000/
```
