from selenium import webdriver

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
  driver.get("http://automated.pythonanywhere.com/")
  return driver

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]")
  return element

print(main())