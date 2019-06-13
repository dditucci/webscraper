# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set URL to be scraped
url = 'http://web.mta.info/developers/turnstile.html'

# Connect URL
response = requests.get(url)

# Parse URL for hyperlinks
soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('a')


# Extract 1st turnstile info link
one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']


# Create for loop to iterate through all links we want and save data
for i in range(36, len(soup.findAll('a'))+1):
    one_a_tag = soup.findAll('a')[i] 
    link = one_a_tag['href'] # 'a href' indicates link
    download_url = 'http://web.mta.info/developers/'+ link # Add link to base website URL 
    urllib.request.urlretrieve(download_url, './'+link[link.find('/turnstile_')+1]) # Concatenate full URL and iterate through
    time.sleep(1) # Pause for 1 second between so we are not spamming website
