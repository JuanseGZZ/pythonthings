import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

# Ruta al perfil persistente
user_data_dir = os.path.abspath("C:/Users/juans/OneDrive/Escritorio/selenium/perfilSelenium")

# Configurar Chrome invisible (headless)
options = uc.ChromeOptions()
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument("--profile-directory=Default")
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

# Iniciar navegador
driver = uc.Chrome(options=options)
driver.get("https://web.whatsapp.com")

try:
    # Esperar a que aparezca el canvas (el QR)
    wait = WebDriverWait(driver, 30)
    qr_canvas = wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))

    # Capturar pantalla completa
    screenshot_path = "whatsapp_full.png"
    driver.save_screenshot(screenshot_path)

    # Recortar QR del screenshot
    location = qr_canvas.location
    size = qr_canvas.size

    image = Image.open(screenshot_path)
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    qr_image = image.crop((left, top, right, bottom))
    qr_image.save("whatsapp_qr.png")
    print("✅ QR guardado como whatsapp_qr.png. Esperando que te loguees...")

    # Esperar hasta que desaparezca el QR (canvas), lo que indica que te logueaste
    WebDriverWait(driver, 180).until(EC.invisibility_of_element(qr_canvas))
    print("✅ Logueo detectado. Cerrando navegador...")

    # Eliminar la imagen completa si no la necesitas
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
        print("✅ Imagen completa eliminada.")
    if os.path.exists("whatsapp_qr.png"):
        os.remove("whatsapp_qr.png")
        print("✅ Imagen QR eliminada.")

    #espera 40 segundos para salir
    time.sleep(40)

except Exception as e:
    print("❌ Error:", e)

driver.quit()
