from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Set up the WebDriver
driver_path = 'C:/chromedriver-win64/chromedriver.exe'  # Update the path to your WebDriver
driver = webdriver.Chrome(executable_path=driver_path)

# Step 2: Open the HTML page
url = 'file:///D:/1_TASK/2024_06_13_Python_CPIDataScraping/CPI_Homepage/Consumer%20Price%20Index%20Archived%20News%20Releases%20_%20U.S.%20Bureau%20of%20Labor%20Statistics.html'
driver.get(url)

# Step 3: Get elements using XPath
xpath_expression = '//*[@id=\"bodytext\"]/div[1]/div/ul[32]/li[12]'  # Example XPath expression to get <h1> elements

elements = driver.find_element(By.XPATH, xpath_expression)

# Print the elements' text content
for element in elements:
    print(element.text)

# Step 4: Close the WebDriver
driver.quit()
