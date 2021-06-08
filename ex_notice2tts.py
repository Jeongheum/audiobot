from gtts import gTTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import PyPDF2 # pip install PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter # pip install pdfminer.six
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import time, os
from os.path import exists
import json
import requests
from bs4 import BeautifulSoup

#import pytesseract, tesseract # pip install pytesseract, tesseract

print('started...')

# 1.You need to check the chromium version, then download the driver of that version
# 2. sudo apt-get install chromium-chromedriver
# refer to https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; CrOS armv7l 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.187 Safari/537.36")
browser=webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',options=options) #'chromedriver' executable needs to be in PATH.
#driver=webdriver.Chrome('/usr/bin/chromedriver') # unexpectedly exited

url='https://www.ealimi.com'
browser.get(url)
time.sleep(1)
islogin=browser.find_element_by_class_name('login_box')
if not islogin:
    print('you have logged in')
else:
    with open('test.json','r') as f:
        json_data = json.load(f)
        
    idm=json_data['ealimi']['id'] #input('Enter your id = ')
    pwdm=json_data['ealimi']['pw'] #input('Enter your passwd = ')
    id_in=browser.find_element_by_id('id')    
    id_in.send_keys(idm) # your_id
    pw_in=browser.find_element_by_id('pw')
    pw_in.send_keys(pwdm) # your_pwd
    log_in=browser.find_element_by_id('signInSubmitBtn')
    log_in.click()
    
    time.sleep(1)
    
    try:   # if pop-up occurs
        action=ActionChains(browser)
        action.click()
        action.perform()
        
    except:
        pass
        
time.sleep(2)
menulist=browser.find_element_by_link_text('받은알리미')
menulist.click()

#url2="https://www.ealimi.com/receivednoti"
#res = requests.get(url2)
#soup = BeautifulSoup(res.content, 'html.parser')
#tmplist1 = soup.body.div.div.find_all(attrs={'class':'content_title'})
#tmplist2 = soup.select(".content_title")
#print(tmplist1)
#print(tmplist2)

alim_list=browser.find_elements_by_class_name('content_title')


for n in range(len(alim_list)):
    a=browser.find_element_by_link_text(alim_list[n].text)
    a.click()
    time.sleep(5)
    fig_name='fig'+str(n)+'.png'
    browser.get_screenshot_as_file(fig_name)
    time.sleep(2)
    browser.back()
    time.sleep(10)

#d1=browser.find_element_by_class_name('article_con')
#e=d1.text
#print(e)
try:
    dd1=d1.find_element_by_class_name('attach_title')
    dd2=d1.find_element_by_id('download')

    if not d22:
        dd2.click()
    elif not dd1:
        dd1.click()
except:
    pass

#dl_path="/home/pi/Downloads/"
#os.system('!ls -al dl_path')
#fname='Download_202105171215448510.pdf'
#f_ext=fname[-3:]


#if f_ext=='pdf':
    #print('pdf2txt')
#elif f_ext=='png':
    #print('jpg2txt')

def pdf2txt(filepath):
    fp=open(filepath,'rb')
    total_page=PyPDF2.PdfFileReader(fp).numPages
    
    page_text={}
    for page_no in range(total_pages):
        rsrcmgr=PDFResourceManager()
        retstr=StingIO()
        codec='utf-8'
        
        laparams=LAParams()
        device=TextConcerter(rsrcmgr,retstr,codec=codec,laparams=laparams)
        fp=open(filepath,'rb')
        password=None
        maxpages=0
        interpreter=PDFPageInterpreter(rsrcmgr,device)
        caching=True
        pagenos=[page_no]
        
        for page in PDFPage.get_pages(fp,pagenos,maxpages=maxpages,password=password,caching=caching,check_extractable=True):
            interpreter.process_page(page)
    

#browser.quit()
#playsound('art_headline.mp3')