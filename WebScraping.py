import requests
import bs4

# Sending request with URL
URL = 'https://www.theTestingWorld.com'
response = requests.get(URL)

# print html content
print(response.text)

# check status code
print(response.status_code)

# open file in write mode
f = open('C:\\Users\\carol\\Documents\\result.txt','wb')

for data in response.iter_content(10000):
    f.write(data)

f.close()

# parse using bs4
parsed_data = bs4.BeautifulSoup(response.text)
all_links = parsed_data.select('a')
print(len(all_links))

for l in all_links:
    print(l.getText()) # the text
    print(l.get('href')) # url
    print(l.get('title')) # title attribute
    print(l.attrs) # all the attributes