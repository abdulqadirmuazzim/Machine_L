import requests as rq
from bs4 import BeautifulSoup as BS


def search(item):
    obj = item.replace(" ", "+")

    url = f"https://www.bing.com/search?q={obj}"
    # headers
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = rq.get(url, headers=head)

    soup = BS(response.text, "html.parser")
    returns = soup.select("a")

    if returns:
        lis = [item for item in returns if "https" in str(item)]
        print(f"Search result for {url}:\n")
        for li in lis:
            print(li)

    else:
        print("No items for this css attribute")


(search("Roles of english language"))
