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

articulo = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section/ol/li[3]/div/div/div[1]/a/div/div/div/div/div/img')
articulo.click()

agregar = driver.find_element_by_xpath('//*[@id="root-app"]/div/div[3]/div/div[1]/div/div[1]/div/div[8]/form/div/button[2]')
#agregar.click()
time.sleep(2)
