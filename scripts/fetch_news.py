import requests
from bs4 import BeautifulSoup

# Function to fetch news from Cailian Press

def fetch_cailian_news():
    url = 'https://www.cls.cn/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('div', class_='news-item')
    news_list = []
    for item in news_items:
        title = item.find('h3').text
        link = item.find('a')['href']
        news_list.append({'title': title, 'link': link})
    return news_list

# Function to fetch news from East Money

def fetch_east_money_news():
    url = 'http://www.eastmoney.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('li', class_='news-item')
    news_list = []
    for item in news_items:
        title = item.find('a').text
        link = item.find('a')['href']
        news_list.append({'title': title, 'link': link})
    return news_list


# Main function to fetch news from both sources

def main():
    print('Fetching news from Cailian Press...')
    cailian_news = fetch_cailian_news()
    print('Cailian News:')
    for news in cailian_news:
        print(f"{news['title']} - {news['link']}")
    
    print('\nFetching news from East Money...')
    east_money_news = fetch_east_money_news()
    print('East Money News:')
    for news in east_money_news:
        print(f"{news['title']} - {news['link']}")


if __name__ == '__main__':
    main()