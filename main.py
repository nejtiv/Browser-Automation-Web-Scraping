from selenium import webdriver
import time

def get_driver():
  #opcje przeglądarki inicjacja
  options = webdriver.ChromeOptions()
  #opcje przeglądarki
  options.add_argument("disable-infobars")
  options.add_argument("start-maximixed")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automaton"])
  options.add_argument("disable-blink-features=AutomationControlled")
  #dodanie opcji headless
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

#funkcja czyszcząca tekst
def clean_text(text):
  output = float(text.split(": ")[1])
  return output
  

#funkcja inicjująca proces
def main():
  driver = get_driver()
  time.sleep(2)
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())