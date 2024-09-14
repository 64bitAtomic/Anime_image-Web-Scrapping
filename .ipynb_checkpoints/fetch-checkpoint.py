import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the CSV file
csv_file = '100_anime.csv'
df = pd.read_csv(csv_file)

# Define a function to scrape the image URL from MyAnimeList
def get_anime_image_url(anime_name):
    search_url = f"https://myanimelist.net/search/all?q={anime_name.replace(' ', '%20')}&cat=all"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find('a', {'class': 'hoverinfo_trigger'})
        if result:
            anime_page_url = result['href']
            anime_response = requests.get(anime_page_url)
            if anime_response.status_code == 200:
                anime_soup = BeautifulSoup(anime_response.text, 'html.parser')
                image_tag = anime_soup.find('img', {'itemprop': 'image'})
                if image_tag:
                    return image_tag['data-src'] if 'data-src' in image_tag.attrs else image_tag['src']
    return None

# Add a new column for image URLs
df['image_url'] = df['name'].apply(get_anime_image_url)

# Save the updated CSV file
df.to_csv('anime_with_images.csv', index=False)

print("Image URLs added to the CSV file.")