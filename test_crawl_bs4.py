import requests
from bs4 import BeautifulSoup as bs

keyword = '한로로'
url = 'https://www.youtube.com/results?search_query='+keyword
yt = requests.get(url).text
# yt = bs(yt, 'lxml')
# yt = str(yt)
# print(len(yt))
# idx = yt.find('"webCommandMetadata":{"url":"/watch')
# print(idx)
# soup = bs(yt.text, "html.parser")
# tmps = soup.find('a', id='video-title')
# print(tmps)

# elements = soup.select('ytd-page-manager > ytd-search > div > ytd-two-column-search-results-renderer > div > ytd-section-list-renderer > div2')
# print(elements)
# print(yt[idx+29:idx+74])
url_pre_text = '"commandMetadata":{"webCommandMetadata":{"url":"/watch'
title_pre_text = '"title":{"runs":[{"text":"'

urls = []
titles = []
ytdotcom = 'https://youtube.com'

idx = 0
while True:
    yt = yt[idx:]   
    if title_pre_text in yt:
        idx = yt.find(title_pre_text)
        titles.append(yt[idx+len(title_pre_text):idx+len(title_pre_text)+10])

        if url_pre_text in yt:
            
            idx = yt.find(url_pre_text)
            end = 68#yt[idx:].find('\\')
            element = yt[idx+48:idx+end]
            idx += 1

            urls.append(ytdotcom+element)
            # print(urls[-1])
        else:
            break
    else:
        break

urls = list(set(urls))
titles = list(set(titles))
print(*titles, sep='\n')

# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write(yt)