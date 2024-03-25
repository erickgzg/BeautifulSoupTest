import requests
from bs4 import BeautifulSoup

url = "https://test.activeport.com.au/#/login"

# Send a GET request to the URL
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find Title of the page
    title = soup.find('title').get_text()

    # Check if the title is correct
    if title == 'ActivePortal':
        print("Portal working well!")
    else:
        print("Something Wrong!!!")
else:
    print("Failed to fetch the page. Status code:", response.status_code)