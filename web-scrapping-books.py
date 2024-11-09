import requests
from bs4 import BeautifulSoup

# URL of Amazon Best Sellers in Books
url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/"

# Define headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the list of best-selling books
    books = soup.find_all("div", class_="zg-grid-general-faceout")

    if books:
        print("Top 5 Best Sellers in Books on Amazon:")
        for i, book in enumerate(books[:5], start=1):
            # Extract book title
            title_element = book.find("div", class_="p13n-sc-truncate-desktop-type2")
            title = title_element.text.strip() if title_element else "Title Not Found"

            # Extract author (some items may not have an author listed)
            author_element = book.find("a", class_="a-size-small a-link-child")
            author = author_element.text.strip() if author_element else "Unknown Author"

            # Print the book details
            print(f"{i}. {title} by {author}")
    else:
        print("No books found. The structure might have changed.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
