#!/usr/bin/env python
# coding: utf-8

# from selenium.webdriver import Chrome, ChromeOptions, Remote
# from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager


import logging
from typing import List  # 型ヒントのためにインポート


def d20220217():

    # options = ChromeOptions()
    # #dockerエラーの修正
    # options.add_argument('--headless')
    # options.add_argument("--remote-debugging-port=9222")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.headless = True
    # driver = Chrome(ChromeDriverManager().install(), options=options)
    # #driver = Chrome(options=options)
    # driver.get('https://www.ris.bka.gv.at/Ergebnis.wxe?Abfrage=Justiz&Gericht=&Rechtssatznummer=&Rechtssatz=&Fundstelle=&AenderungenSeit=Undefined&SucheNachRechtssatz=False&SucheNachText=True&GZ=&VonDatum=&BisDatum=24.01.2022&Norm=&ImRisSeitVonDatum=&ImRisSeitBisDatum=&ImRisSeit=Undefined&ResultPageSize=100&Suchworte=Garant&Position=1&SkipToDocumentPage=true')

    # next_page=True
    # next_url='https://www.ris.bka.gv.at/Ergebnis.wxe?Abfrage=Justiz&Gericht=&Rechtssatznummer=&Rechtssatz=&Fundstelle=&AenderungenSeit=Undefined&SucheNachRechtssatz=False&SucheNachText=True&GZ=&VonDatum=&BisDatum=24.01.2022&Norm=&ImRisSeitVonDatum=&ImRisSeitBisDatum=&ImRisSeit=Undefined&ResultPageSize=100&Suchworte=Garant&Position=1&SkipToDocumentPage=true'
    # result=[]

    # #修正
    # driver.quit()

    # while next_page==True:
    #     options = ChromeOptions()
    #     options.add_argument('--headless')
    #     options.add_argument("--remote-debugging-port=9222")
    #     options.add_argument("--no-sandbox")
    #     options.add_argument("--disable-dev-shm-usage")

    #     options.headless = True
    #     driver = Chrome(ChromeDriverManager().install(), options=options)
    #     driver.get(next_url)
        
        
    #     #続きのページdriver
    #     next_page_pointer=driver.find_elements_by_css_selector('span.Next')
    #     if len(next_page_pointer) == 0:
    #         next_page = False
    #     else:
    #         next_page = True
    #         a = next_page_pointer[0].find_element_by_css_selector('a')
    #         next_url=a.get_attribute('href')
            
        
    #     div=driver.find_elements_by_css_selector('div#MainContent_DocumentsList_TableScrollContainer')[0]
    #     trs=div.find_elements_by_css_selector('tr')[1:]
    #     print(len(trs))
        
    #     urls=[]
    #     for tr in trs:
    #         a = tr.find_element_by_css_selector('a')
    #         url=a.get_attribute('href')
    #         urls.append(url)
            
    #     contents=[]
    #     #testのため一旦５まで
    #     for url in urls[:5]:
    #         options_a = ChromeOptions()
    #         options_a.add_argument('--headless')
    #         options_a.add_argument("--remote-debugging-port=9222")
    #         options_a.add_argument("--no-sandbox")
    #         options_a.add_argument("--disable-dev-shm-usage")

    #         options_a.headless = True
    #         detail_driver = Chrome(ChromeDriverManager().install(), options=options_a)
    #         detail_driver.get(url)
    #         #div=detail_driver.find_elements_by_css_selector('p')
    #         dettail_div=detail_driver.find_elements_by_css_selector('div.documentContent')[0].text
    #         contents.append(dettail_div)
    #         #修正
    #         detail_driver.quit()
    #     result.append(contents)

    #     #修正
    #     driver.quit()

    result = ["20220710sample"]

    return result