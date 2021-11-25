from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

buscador = 1

if buscador == 1:
    driver = webdriver.Chrome('C:/Users/DianaEspitiaTorres/Downloads/chromedriver/chromedriver.exe')
elif buscador ==2:
    driver = webdriver.Firefox()

driver.get("https://www.mercadolibre.com.co/") # Abrir Google

barra = driver.find_element_by_xpath('/html/body/header/div/form/input')
barra.send_keys('Kit Lettering')
barra.send_keys(Keys.ENTER)
time.sleep(2)
