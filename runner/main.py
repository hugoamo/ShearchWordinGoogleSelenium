from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.implicitly_wait(3)

driver.get("https://www.google.com")

inputTextShearch = driver.find_element(by=By.XPATH, value="//textarea[@title='Buscar']")

inputTextShearch.send_keys("programacion orientada a objertos")

buttonSumint = driver.find_element(by=By.NAME, value="btnK")

buttonSumint.click()

h3_elements = driver.find_elements(By.CSS_SELECTOR, "h3")


for i in h3_elements:
    if i.text == "Programación orientada a objetos":
        print(i.text)

driver.quit()
