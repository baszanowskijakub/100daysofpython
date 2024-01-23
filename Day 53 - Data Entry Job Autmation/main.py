from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time


properties = []
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, 'html.parser')
listings = soup.find_all("div", {"class": "StyledPropertyCardDataWrapper"})
addresses = [address.get_text(strip=True) for address in soup.select("div.StyledPropertyCardDataWrapper address[data-test='property-card-addr']")]
prices = [price.get_text(strip=True) for price in soup.select("div.StyledPropertyCardDataWrapper span[class='PropertyCardWrapper__StyledPriceLine']")]
cleaned_prices = [price.split('+')[0].split('/')[0] for price in prices]
links = [link['href'] for link in soup.select("div.StyledPropertyCardDataWrapper a[data-test='property-card-link']")]

for i in range(len(listings)):
    property_entry = {
        "address": addresses[i],
        "price": cleaned_prices[i],
        "link": links[i]
    }
    properties.append(property_entry)

print(properties)
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(edge_options)


address_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
price_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
link_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
send_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'
again_button_xpath = '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'
driver.get("https://forms.gle/GtJjmv3p4TPCWKfy5")

for item in properties:
    time.sleep(4)
    address_input = driver.find_element(By.XPATH, value=address_xpath)
    address_input.send_keys(item["address"])
    price_input = driver.find_element(By.XPATH, value=price_xpath)
    price_input.send_keys(item["price"])
    link_input = driver.find_element(By.XPATH, value=link_xpath)
    link_input.send_keys(item["link"])
    send_button = driver.find_element(By.XPATH, value=send_button_xpath)
    send_button.click()
    time.sleep(1)
    again_button = driver.find_element(By.XPATH, value=again_button_xpath)
    again_button.click()
    time.sleep(1)

link_input = driver.find_element(By.XPATH, value=link_xpath)






