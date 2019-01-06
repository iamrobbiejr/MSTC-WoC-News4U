import requests
import bs4

print("\nWelcome to News4U..!!\n")
print("Topics:\n\n all\n national    business\n sports      world\n politics    technology\n startup     entertainment\n science     automobile\n")
topic = input("Enter a topic from above to get news:  \n")

if topic=="all":
    res = requests.get('https://inshorts.com/en/read/')
else:
    res = requests.get('https://inshorts.com/en/read/' + topic)


soup = bs4.BeautifulSoup(res.text, 'lxml')

head = soup.find_all(itemprop="headline")

url = soup.select(".source")
print("\nTop "+topic+" news are:\n")

for i in range(10):
    print(head[i].getText())
    print(url[i].get("href"))
    print("\n")


