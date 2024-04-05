from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def play_youtube_video(video_url):
    # Initialiser le navigateur web automatisé
    options = webdriver.EdgeOptions()
    # options.add_argument('--headless')
    options.use_chromium = True  # Utiliser le nouveau Microsoft Edge basé sur Chromium
    driver = webdriver.Edge(options=options)

    try:
        # Ouvrir directement la vidéo avec le lien
        wait = WebDriverWait(driver, 10)  # Define the wait variable

        driver.get(video_url)
        time.sleep(5)
        # driver.implicitly_wait(300)
        
        # driver.find_element(By.XPATH, '//span[text()="Tout refuser"]').click()
        # driver.find_element(By.XPATH, '//span[text()="Tout accepter"]').click()
        # driver.find_element(By.XPATH, '//button[@Class="yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m"]').click()
        if 'consent.youtube.com' in driver.current_url: # THIS IS THE CHECK
            print('Consent page found')
            driver.find_element(By.XPATH, '//span[text()="Tout refuser"]').click()
            driver.find_element(By.XPATH, '//span[text()="Tout accepter"]').click()
            driver.find_element(By.XPATH, '//button[@Class="yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m"]').click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ytp-play-button.ytp-button')))

        # Cliquer sur le bouton de lecture de la vidéo en utilisant JavaScript
        play_button = driver.find_element(By.CSS_SELECTOR, '.ytp-play-button.ytp-button')
        driver.execute_script("arguments[0].click();", play_button)
        
        # Attendre 32 secondes pour la fin de la vidéo
        # time.sleep()
        
        # Rejouer la vidéo 100 fois
        for i in range(300):
            replay = driver.find_element(By.CSS_SELECTOR, '.ytp-play-button.ytp-button')
            driver.execute_script("arguments[0].click();", replay)
            time.sleep(35)

    except Exception as e:
        print("Une erreur s'est produite:", e)

    finally:
        # Fermer le navigateur après l'exécution
        driver.quit()

video_url = "https://www.youtube.com/watch?v=Y1zqL4y0-7w&ab_channel=MathisVisuals"
play_youtube_video(video_url)
