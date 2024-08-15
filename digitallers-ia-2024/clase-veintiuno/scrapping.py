from playwright.sync_api import sync_playwright

def scrape_news():

    #p = sync_playwright()
    #try:
    #    p.blablalba(
    #finally:
    #    l.close()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Usa headless=False si deseas ver el navegador
        page = browser.new_page()

        # Navega a la página con las noticias
        page.goto('http://127.0.0.1:5500/noticias.html')

        # Espera a que las secciones de noticias estén visibles
        page.wait_for_selector('main section')

        # Extrae las noticias
        news_items = page.query_selector_all('main section')

        for item in news_items:
            title = item.query_selector('h2').inner_text()
            content = item.query_selector('p').inner_text()
            print(f'Título: {title}')
            print(f'Contenido: {content}')
            print('-' * 40)

        browser.close()

if __name__ == '__main__':
    scrape_news()
