import requests
from bs4 import BeautifulSoup
from weasyprint import HTML, CSS

def scrape_subpages(main_url):
    try:
        response = requests.get(main_url)
        response.raise_for_status()
        print("Main page fetched successfully.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error fetching main URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    nav_menu = soup.find(class_='wporg-chapter-list__list')
    if not nav_menu:
        print("Navigation menu not found.")
        return

    links = [link.get('href') for link in nav_menu.find_all('a')]
    print(f"Found {len(links)} links to process.")

    all_html_content = "<style>img {max-width: 100%; height: auto;}</style>"

    for index, link in enumerate(links, start=1):
        try:
            subpage_response = requests.get(link)
            subpage_response.raise_for_status()
            print(f"Processing link {index}/{len(links)}: {link}")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e} for URL: {link}")
            continue
        except requests.exceptions.RequestException as e:
            print(f"Error fetching subpage URL: {e}")
            continue

        subpage_soup = BeautifulSoup(subpage_response.text, 'html.parser')
        content = subpage_soup.find('article', class_='wp-block-group')

        if content:
            all_html_content += str(content)
        else:
            print(f"Content not found in {link}")

    print("Generating PDF, please wait...")
    HTML(string=all_html_content).write_pdf("compiled_content.pdf", stylesheets=[CSS(string='@page {size: A4; margin: 1cm;}')])
    print("PDF created successfully.")

main_page_url = 'https://developer.wordpress.org/block-editor'
scrape_subpages(main_page_url)
