from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_basket_with_playwright():
    match_data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1) Chargement de la page
        page.goto("https://www.bet261.mg/sports/102", wait_until="networkidle")

        # 2) Cliquer sur l'onglet Basket si présent
        try:
            page.click('button:has-text("Basket")', timeout=5000)
        except:
            pass

        # 3) Scroll vers le bas + attente lazy-load
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000)

        # 4) Attente des blocs de match Angular
        page.wait_for_selector('hg-event-with-event-bet-type.ng-star-inserted', timeout=30000)

        # 5) Récupération du HTML complet après rendu JS
        content = page.content()

        # 6) Parser le HTML avec BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        cards = soup.select('hg-event-with-event-bet-type.ng-star-inserted')

        print(f"{len(cards)} cartes trouvées")

        # 7) Itération sur les blocs et extraction d'infos
        for card in cards:
            name_spans = card.select('div.event-informations span.name')
            teams = name_spans[0].get_text(strip=True) if name_spans else "???"
            time_span = card.select_one('span.hour')
            time = time_span.get_text(strip=True) if time_span else "--:--"
            day_span = card.select_one('span.day')
            day = day_span.get_text(strip=True) if day_span else "???"

            print(f"{day} {time} — {teams}")
            match_data.append({
                "jour": day,
                "heure": time,
                "equipes": teams
            })

        browser.close()
    
    return match_data
