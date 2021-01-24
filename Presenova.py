from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


browser.get('https://lms.presenova.com/user/login')

browser.find_element_by_name('name').send_keys('lavya.shivu@gmail.com')
browser.find_element_by_name('pass').send_keys('V1shnvsh')
browser.find_element_by_name('op').click()