from selenium.webdriver.common.by import By
import re

elementos = driver.find_elements(
    By.XPATH,
    "//*[contains(text(),'US$')]"
)

precios = []

for e in elementos:
    texto = e.text.strip()

    m = re.search(r'(\d+,\d+)\s*US\$', texto)
    if m:
        precio = float(m.group(1).replace(",", "."))
        precios.append(precio)

if precios:
    datos["precio"] = f"{min(precios):.2f}"