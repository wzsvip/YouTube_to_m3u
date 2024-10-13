import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        if windows:
            return None
        os.system(f'curl "{url}" > temp.txt')
        response = ''.join(open('temp.txt').readlines())
        if '.m3u8' not in response:
            return None
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    return f"{link[start : end]}"

m3u8_links = []
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            continue
        m3u8_link = grab(line)
        if m3u8_link:
            m3u8_links.append(m3u8_link)

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')

print("通用的链接m3u8地址：")
for link in m3u8_links:
    print(link)
