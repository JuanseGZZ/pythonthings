import undetected_chromedriver as uc
import time
import os

# Ruta a una carpeta para guardar el perfil de usuario (no la de Chrome real)
user_data_dir = os.path.abspath("C:/Users/juans/OneDrive/Escritorio/selenium/perfilSelenium")

def main():
    options = uc.ChromeOptions()
    
    # Carpeta del perfil persistente (separada del Chrome real)
    options.user_data_dir = user_data_dir
    
    # Maximizar ventana al abrir
    options.add_argument("--start-maximized")

    # Inicializar el navegador (stealth activado por defecto en uc)
    driver = uc.Chrome(options=options, headless=False)

    # Ir a LinkedIn
    driver.get("https://www.linkedin.com")

    # Esperar a que el usuario se loguee
    input("🟡 Iniciá sesión manualmente en la pestaña abierta y luego presioná Enter aquí...")

    # Cerrar navegador después de iniciar sesión
    driver.quit()

if __name__ == "__main__":
    main()
