from flask import Flask ,render_template , url_for ,request
import requests
import bs4
import re

app=Flask('__name__')


@app.route('/',methods=['POST','GET'])
def index():
    news=[]

    if request.method=='POST':
        topic=request.form['topic']
        if topic=="all":
            res = requests.get('https://inshorts.com/en/read/')
        else:
            res = requests.get('https://inshorts.com/en/read/' + topic)

# parsing the document received from requests using beautiful soup
        soup = bs4.BeautifulSoup(res.text, 'lxml')

# getting /extracting the heading of news from parsed beautiful soup object
        head = soup.find_all(itemprop="headline")


# getting /extracting the URL of source of news from parsed beautiful soup object
        url = soup.select(".source")


# getting /extracting the image related to news from parsed beautiful soup object
        image=soup.select(".news-card-image")

# ^ above  actions returns an array of objects


# adding scraped data into an array so that it can easily be rendered
        for i in range(16):
            item=dict(title=head[i].getText(),source =url[i].get("href"),image_url=re.search('(?P<url>https?://[^\s]+)',image[i].get("style") ).group("url"))
            news.append(item)


# added exception  handling and rendering using jinja2 templates
        try:
            return render_template('news4u.html',news_topic=topic,all_news=news)
        except:
            return render_template('news4u.html')

    else:
        return render_template('news4u.html')


if __name__=="__main__":
    app.run(debug=True)