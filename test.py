# from playwright.sync_api import sync_playwright
# from bs4 import BeautifulSoup

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()
#     page.goto("https://www.bet261.mg/sports/102", timeout=60000)
#     page.wait_for_timeout(5000)  # attendre JS (ajuster si nécessaire)
#     html = page.content()
#     soup = BeautifulSoup(html, 'html.parser')
#     print(soup.title)
#     browser.close()
from utils.getMatch import scrape_basket_with_playwright
from utils.export_csv import export_to_csv

data=scrape_basket_with_playwright()
export_to_csv(data)
