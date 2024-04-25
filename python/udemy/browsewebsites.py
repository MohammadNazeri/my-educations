from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.amazon.ca/dp/B07R6XYN5Q/ref=twister_B0CGWW4W1X?_encoding=UTF8&th=1"
#url = "https://www.amazon.ca/gp/product/B09N93L2RQ/ref=ewc_pr_img_1?smid=A2MVL5OZYL2KXQ&psc=1"

driver.get(url)


input("Enter to continue ... ")

#price = driver.find_element(By.CLASS_NAME, value='a-offscreen')
price = driver.find_element(By.XPATH, value='//*[@id="corePrice_feature_div"]/div/div/div/div/span[1]/span[1]')

print(price.get_attribute('innerHTML'))

driver.quit()
