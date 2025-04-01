import undetected_chromedriver as uc
import time
import os
from selenium.webdriver.common.by import By


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
    driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4192786158&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII")

    lista_trabajos = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list")
    ul = lista_trabajos[0].find_element(By.TAG_NAME, "ul")
    lis = ul.find_elements(By.TAG_NAME, "li")

    encontrado = False
    iterador = 1

    while encontrado == False:
        post_job = driver.find_elements(By.CSS_SELECTOR, ".jobs-search__job-details--wrapper")

        if post_job and post_job[0].find_elements(By.CSS_SELECTOR, ".job-details-people-who-can-help__section--two-pane.artdeco-card.ph5.pv4"):

            encontrado = True
            link = post_job[0].find_elements(By.CSS_SELECTOR, ".job-details-people-who-can-help__section--two-pane.artdeco-card.ph5.pv4")[0].find_elements(By.CSS_SELECTOR, ".DOgZOenwMQbHzVlKpcdwpsKlJNhiKoDGZrrVVbuM")
            if link:
                link[0].click()

            time.sleep(5)

            print("Encontrado")
            
        else:
            lis[iterador+1].click()
            time.sleep(5)
            print("No encontrado")
        iterador+= 1
        
            
    # Aca ya se encuentra en el prefil de la persona
    # agarrar link y printearlo
    perfil = driver.current_url
    print(perfil)
    
    input("entre para salir")

    # Cerrar navegador después de iniciar sesión
    driver.quit()

if __name__ == "__main__":
    main()
