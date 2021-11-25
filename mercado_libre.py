from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

buscador = 1 #Seleccionar el buscador

if buscador == 1:
    driver = webdriver.Chrome('C:/Users/DianaEspitiaTorres/Downloads/chromedriver/chromedriver.exe') 
elif buscador ==2:
    driver = webdriver.Firefox()

driver.get("https://www.mercadolibre.com.co/") #Abrir página de mercado libre

barra = driver.find_element_by_xpath('/html/body/header/div/form/input') #Identificar el elemento (barra de búsqueda)
barra.send_keys('Kit Lettering') #Artículos que deseamos buscar
barra.send_keys(Keys.ENTER) #Enter para buscar 
time.sleep(2)
