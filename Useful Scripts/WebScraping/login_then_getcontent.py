from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_service():
    try:
        service = Service(ChromeDriverManager().install())
    except Exception as e:
        service = Service('chromedriver.exe')
    return service
def get_options():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("disable-gpu")
    return options
def get_driver():
    driver = webdriver.Chrome(service=get_service(),chrome_options=get_options())
    driver.implicitly_wait(10)
    driver.maximize_window()
def login(driver,my_username,my_password):
    driver.find_element(By.ID,"login-form-username").send_keys(my_username)
    driver.find_element(By.ID,"login-form-password").send_keys(my_password)
    driver.find_element(By.ID,"login-form-submit").click()
    wait_to_check_if_page_load(driver)
def wait_to_check_if_page_load(driver):
    try:
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID,"element_id_of_afterloginpage")))
        return True
    except TimeoutError:
        return False
    except TimeoutExpired:
        return False
login_url = '#'
driver = get_driver()
driver.get(login_url)
