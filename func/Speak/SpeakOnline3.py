import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import eel

from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')
chrome_options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
website = r"https://tts.5e7en.me/"
driver.get(website)


def Speak(text):
    try:
        # Wait for the element to be clickable
        element_to_click = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
        )

        # Perform the click action
        element_to_click.click()

        # Input text into the element
        text_to_input = text
        element_to_click.send_keys(text_to_input)
        print(text_to_input)
        eel.displayBotResponse(text)


        # Calculate sleep duration based on sentence length
        sleep_duration = min(0.1 + len(text) // 20, 50)  # Minimum sleep is 3 seconds, maximum is 10 seconds

        # Wait for the button to be clickable
        button_to_click = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
        )

        # Perform the click action on the button
        button_to_click.click()

        # Sleep for dynamically calculated duration
        time.sleep(sleep_duration)

        # Clear the text box for the next sentence
        element_to_click.clear()

    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error as needed, e.g., log it, raise it again, etc.

Speak("Hello, How are you?")