import time
import pandas as pd
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

df = pd.read_excel('Input.xlsx')
driver = webdriver.Chrome('./chromedriver.exe')


urls_not_available = [] # to reconsider the text files in which data extraction isn't complete.
for i in range(len(df)):
    url = df['URL'][i]
    driver.get(url)
    try:
        header_selector = 'div.td-full-screen-header-image-wrap > div.td-container.td-post-header > div.td-post-header-holder > div.td-parallax-header > header > h1'
        header_element = driver.find_element(By.CSS_SELECTOR, value=header_selector)
        body_selector = 'div.td-container > div > div.td-pb-span8.td-main-content > div > div.td-post-content'
        body_element = driver.find_element(By.CSS_SELECTOR, value=body_selector)
        if not os.path.exists('/extracted_data'):
            # Create the directory
            os.makedirs('/extracted_data')
        file=open('/extracted_data'+str(df['URL_ID'][i])+".txt","w")
        file.write(header_element.text)
        file.write(body_element.text)
        file.close()
        time.sleep(2)
    except:
        try:
            header_selector = 'div.td-post-header > header > h1'
            header_element = driver.find_element(By.CSS_SELECTOR, value=header_selector)
            body_selector = 'div.td-post-content'
            body_element = driver.find_element(By.CSS_SELECTOR, value=body_selector)
            file=open('/extracted_data'+str(df['URL_ID'][i])+".txt","w")
            file.write(header_element.text)
            file.write(body_element.text)
            file.close()
            time.sleep(2)
        except:
            print("Header not found",url)
            file=open('/extracted_data'+str(df['URL_ID'][i])+".txt","w")
            file.write(' ')
            file.close()
            urls_not_available.append(url)


for url in urls_not_available:
    
    try:
        driver.get(url)
        header_selector = 'div.td-post-header > header > h1'
        header_element = driver.find_element(By.CSS_SELECTOR, value=header_selector)
        body_selector = 'div.td-container > div > div.td-pb-span8.td-main-content > div > div.td-post-content'
        body_element = driver.find_element(By.CSS_SELECTOR, value=body_selector)
        file=open('/extracted_data'+str(df['URL_ID'][i])+".txt","w")
        file.write(header_element.text)
        file.write(body_element.text)
        file.close()
        time.sleep(5)
    except:
        try:
            driver.get(url)
            header_selector_2 = 'div.td-post-header > header > h1'
            header_element_2 = driver.find_element(By.CSS_SELECTOR, value=header_selector_2)
            body_selector_2 = 'div.td-post-content'
            body_element_2 = driver.find_element(By.CSS_SELECTOR, value=body_selector_2)
            file=open('/extracted_data'+str(df['URL_ID'][i])+".txt","w")
            file.write(header_element_2.text)
            file.write(body_element_2.text)
            file.close()
            time.sleep(5)
        except:
            driver.get(url)
            print("Header not found",url)
            file=open('/extracted_data'+str(df['URL_ID'][i])+".txt","w")
            file.write(' ')
            file.close()
            time.sleep(2)