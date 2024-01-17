import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_number(driver, xpath):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        number_match = re.search(r'\d+(?:,\d+)*', element.text)
        return int(number_match.group().replace(',', '')) if number_match else 0
    except StaleElementReferenceException:
        return 0


def extract_metric(driver, xpath):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    metric_match = re.search(r'\d+(\.\d+)?', element.text)
    return float(metric_match.group()) if metric_match else 0


def main():
    driver_options = webdriver.EdgeOptions()
    driver_options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=driver_options)
    driver.get("https://orteil.dashnet.org/experiments/cookie/")

    cookie_button_xpath = '//*[@id="cookie"]'
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, cookie_button_xpath))
    )

    start_time = time.time()
    running = True
    clicks_count = {
        "Cursor": 0, "Grandma": 0, "Factory": 0, "Mine": 0,
        "Shipment": 0, "Alchemy lab": 0, "Portal": 0, "Time machine": 0
    }

    while running:
        cookie_button.click()
        current_time = time.time()

        if current_time - start_time > 10000000:  # 10 million seconds
            running = False
            continue

        prices = {item: extract_number(driver, f'//*[@id="buy{item}"]') for item in clicks_count}
        money_xpath = '//*[@id="money"]'
        money = extract_number(driver, money_xpath)
        cps = extract_metric(driver, '//*[@id="cps"]')

        items_sorted = sorted(prices.items(), key=lambda x: x[1])
        for i, (item, price) in enumerate(items_sorted):
            next_price = float('inf') if i == len(items_sorted) - 1 else items_sorted[i + 1][1]
            if price <= money and (price * 2.5 <= next_price or i == len(items_sorted) - 1):
                best_item_xpath = f'//*[@id="buy{item}"]'
                best_item_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, best_item_xpath))
                )
                best_item_element.click()
                clicks_count[item] += 1
                break

    driver.quit()


if __name__ == "__main__":
    main()
