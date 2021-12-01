from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

## Indicar el buscador
print('Seleccione el buscador que desea utilizar')
print('1. Google Chrome')
print('2. Firefox')
print()
buscador = int(input('Buscardor: '))

if buscador == 1:
    driver = webdriver.Chrome()
elif buscador == 2:
    driver = webdriver.Firefox()
else:
    print('Ingresó un valor incorrecto')
    exit()

driver.maximize_window()
driver.get('https://www.amazon.com/-/es/') #Abrir página de Amazon

#Búsqueda de artículo
barra = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]') 
barra.send_keys('ropa nasa')
barra.send_keys(Keys.ENTER)

wait = WebDriverWait(driver,10)
articulo1 = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/span/a/div/img')))

#Elección de artículo                                     
articulo = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/span/a/div/img')
articulo.click()

articulo1 = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))

#Agregar artículo al carrito de compras
agregar = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]') 
agregar.click()

articulo1 = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="hlb-view-cart-announce"]')))

#Ver carrito
carrito = driver.find_element_by_xpath('//*[@id="hlb-view-cart-announce"]')
carrito.click()

driver.close()
