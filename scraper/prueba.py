from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

driver.get("https://www.eneba.com/latam/store/games")

input("Cuando termine de cargar, presiona Enter...")

with open("listado.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

driver.quit()