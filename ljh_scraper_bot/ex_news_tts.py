#from gtts import gTTS
import pyttsx3
from selenium import webdriver # python3 -m pip install selenium

print('start')

driver=webdriver.Chrome('./chromedriver')

url={'news':'https://news.naver.com','notice':'http://www.naver.com'}
kwd='news'
des_url=url[kwd]

#driver.get(url)
driver.get(des_url)
div=driver.find_element_by_id('today_main_news')
elem=div.find_element_by_class_name('hdline_article_list')
childs=elem.find_elements_by_tag_name('li')

n=0
linkd={}
for child in childs:
   f=open('article'+str(n)+'.txt','w+',encoding='utf-8')
   f2=open('article_hline.txt','a+',encoding='utf-8')
   link=child.find_element_by_tag_name('a').get_attribute('href')
   linkd[n]=link
   txt1="{}번째 헤드라인입니다. ".format(n+1) + child.text
   f.write(txt1)
   f.close()
   
   f2.write(txt1+'\n')
   f2.close()
   
   n=n+1

for i in range(len(linkd)):
   f=open('article'+str(i)+'.txt','a+',encoding='utf-8')
   url2=linkd[i]
   driver.get(url2)
   txt2=driver.find_element_by_id('articleBodyContents')
   f.write(txt2.text)
   f.close()
   driver.quit()
          
def Saying(msg):
   engine=pyttsx3.init()
   engine.setProperty('rate',170)
   engine.say(msg)
   engine.runAndWait()

'''
for child in childs:
   print(child.text)
   Saying(child.text)
'''
f=open('article_hline.txt','r',encoding='utf-8')
msg_hl=f.read()
f.close()

Saying(msg_hl)


ind_k=input('몇번째 기사를 자세히 읽어줄까요? ')
fname='article'=str(ind_k+1)+'.txt'
f=open(fname,'r',encoding='utf-8')
msg=f.read()
f.close()

Saying(msg)
driver.quit()
