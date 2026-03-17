import requests
from bs4 import BeautifulSoup

def scrape_books(page_number):

    url = f"http://books.toscrape.com/catalogue/page-{page_number}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        name = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        rating = book.p["class"][1]

        products.append({
            "Product Name": name,
            "Price": price,
            "Rating": rating,
            "Page": page_number
        })

    return products
