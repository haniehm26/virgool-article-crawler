import time
from typing import List
from article import Article
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

WAITING_TIME = 3
SCROLL_PAUSE_TIME = 2

class Crawler():
    def __init__(self) -> None:
        self.URL = 'https://virgool.io/@haniehmahdavi26'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def request(self) -> None:
        self.driver.get(self.URL) 
        time.sleep(WAITING_TIME)

    def crawl(self) -> List[Article]:
        articles = []
        self.scroll_down()
        streams = self.driver.find_elements(By.CLASS_NAME, 'streamItem-caption')
        for stream in streams:
            title = stream.find_element(By.TAG_NAME, 'h3').text
            href = stream.find_element(By.TAG_NAME, 'a').get_attribute('href')
            article = Article(title=title, href=href)
            articles.append(article)
        return articles
            
    def scroll_down(self) -> None:
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
    def close_driver(self) -> None:
        self.driver.close()

    def save_to_file(self, articles: List[Article]) -> None:
        title = "لیست پست‌های منتشر شده توسط من"
        contact = "ارتباط با من"
        virgool = "ویرگول"
        telegram = "کانال تلگرام"
        with open('articles.md', 'w', encoding='utf-8') as f:
            f.write("## " + title + "\n")
            for article in reversed(articles):
                f.write("#### [" + article.title + "](" + article.href + ")\n\n")
            f.write("## " + contact + "\n")
            f.write("#### [" + virgool + "](https://virgool.io/@haniehmahdavi26)\n")
            f.write("#### [" + telegram + "](https://t.me/honio_notes)\n")
            f.close()
        print("articles.md saved successfully!")

    def run(self):
        self.request()
        articles = self.crawl()
        self.close_driver()
        self.save_to_file(articles=articles)
        