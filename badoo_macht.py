#https://github.com/errodringer/selenium_con_python/blob/master/selenium_scraping_example.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os



def ejecutar_baboo_mach(number):
    
    opciones = webdriver.ChromeOptions()
    p = r'C:\\Users\\LENOVO\\AppData\\Local\\Google\\Chrome\\User Data'
    opciones.add_argument('--user-data-dir='+p)
    driver = webdriver.Chrome("C:\\Users\\LENOVO\\OneDrive\\.AProgramacion\\python\\Slenium\\badoo\\chromedriver_win32\\chromedriver.exe",chrome_options=opciones)
    driver.get('https://badoo.com/')
    
    repetidor = int(number) 
    
    i = 0  
    while i < repetidor:
        try:
            time.sleep(5)
            WebDriverWait(driver, 60)\
                .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/main/div[1]/div/div[1]/section/div/div[2]/div/div[2]/div[1]/div[1]')))\
                .click()
            i += 1
            time.sleep(5)
        except:
            time.sleep(5)
            driver.close()
            return f'El programa dio {i} maches'
        
    time.sleep(5)
    driver.close()
    return f'El programa dio {i} maches'
        
    
                
            
# opciones = webdriver.ChromeOptions()
# p = r"C:\\Users\\afriv\AppData\\Local\\Google\\Chrome\\User Data"
# opciones.add_argument('--user-data-dir='+p)

# driver = webdriver.Chrome('chromedriver.exe' ,chrome_options=opciones)
# driver.get('https://badoo.com/')
