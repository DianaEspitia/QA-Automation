from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/DianaEspitiaTorres/Downloads/chromedriver/chromedriver.exe')

driver.get('https://www.amazon.com/-/es/')

barra = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
barra.send_keys('ropa nasa')
barra.send_keys(Keys.ENTER)
                                         
articulo = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/span/a/div/img')
articulo.click()

agregar = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]') 
agregar.click()

carrito = driver.find_element_by_xpath('//*[@id="hlb-view-cart-announce"]')
carrito.click()
time.sleep(2)
