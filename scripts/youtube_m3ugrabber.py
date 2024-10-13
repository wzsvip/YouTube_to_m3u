import requests
from bs4 import BeautifulSoup
import time

def extract_m3u8_links(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            m3u8_links = [link['href'] for link in soup.find_all('a', href=True) if 'http' in link['href'] and '.m3u8' in link['href']]
            return m3u8_links
    except Exception as e:
        print(f"Error while accessing {url}: {e}")
    return []

def save_m3u8_links_to_file(links, file_path):
    with open(file_path, 'w') as f:
        for link in links:
            f.write(link + '
')

if __name__ == "__main__":
    input_file = '../youtube_channel_info.txt'
    output_file = '../wz.txt'

    with open(input_file, 'r') as f:
        urls = f.readlines()

    all_m3u8_links = []
    for url in urls:
        url = url.strip()
        m3u8_links = extract_m3u8_links(url)
        all_m3u8_links.extend(m3u8_links)
        time.sleep(1)  # Wait for 1 second before accessing the next URL

    save_m3u8_links_to_file(all_m3u8_links, output_file)
