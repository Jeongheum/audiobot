#from gtts import gTTS
import pyttsx3
from selenium import webdriver # python3 -m pip install selenium

print('start')

driver=webdriver.Chrome(./chromedriver)

url='https://news.naver.com'
driver.get(url)
div=driver.find_element_by_id('today_main_news')
elem=div.find_element_by_class_name('hdline_article_list')
childs=elem.find_elements_by_tag_name('li')

def Saying(msg):
   engine=pyttsx3.init()
   engine.setProperty('rate',170)
   engine.say(msg)
   engine.runAndWait()

for child in childs:
   print(child.text)
   Saying(child.text)

driver.quit()
