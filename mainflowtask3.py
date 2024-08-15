import requests
from bs4 import BeautifulSoup
url = 'https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website'
response = requests.get(url)
if response.status_code == 200:
    soup= BeautifulSoup(response.text,'html.parser')
    page_text=soup.get_text()
    links= [a['href'] for a in soup.find_all('a',href=True)]
    images=[img['src'] for img in soup.find_all('img',src=True)]
    print("page test:")
    print(page_text)
    print("\nLinks:")
    for link in links:
        print(link)
    print("\nImages:")
    for image in images:
        print(image)
else:
    print(f"failed to reciee the web page. Status code: (response.status_code)")
