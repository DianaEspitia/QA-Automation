from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

## Indicar el buscador
print('Seleccione el buscador que desea utilizar')
print('1. Google Chrome')
print('2. Firefox')
print()
buscador = int(input('Buscardor: '))

if buscador == 1:
    driver = webdriver.Chrome('C:/Users/DianaEspitiaTorres/Downloads/chromedriver/chromedriver.exe')
elif buscador == 2:
    driver = webdriver.Firefox()
else:
    print('Ingresó un valor incorrecto')
    exit()

driver.get('https://www.amazon.com/-/es/') #Abrir página de Amazon

#Búsqueda de artículo
barra = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]') 
barra.send_keys('ropa nasa')
barra.send_keys(Keys.ENTER)
time.sleep(2)

#Elección de artículo                                     
articulo = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/span/a/div/img')
time.sleep(1)
articulo.click()
time.sleep(1)

#Agregar artículo al carrito de compras
agregar = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]') 
time.sleep(1)
agregar.click()
time.sleep(1)

#Ver carrito
carrito = driver.find_element_by_xpath('//*[@id="hlb-view-cart-announce"]')
time.sleep(1)
carrito.click()
time.sleep(2)
