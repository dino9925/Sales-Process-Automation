import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com/search?q=saas%20jobs%20in%20india&oq=saas%20jobs%20in%20india&gs_lcrp=EgRlZGdlKgcIABAAGIAEMgcIABAAGIAEMggIARAAGBYYHjINCAIQABiGAxiABBiKBTINCAMQABiGAxiABBiKBTINCAQQABiGAxiABBiKBTINCAUQABiGAxiABBiKBTIKCAYQABiABBiiBDIKCAcQABiABBiiBNIBCDQ2NDJqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8&jbr=sep:0&udm=8&ved=2ahUKEwil7ITPoq-NAxV4e_UHHfjMKRYQ3L8LegQIJhAN")

for _ in range(15):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

print("Finished scrolling!")

job_blocks = driver.find_elements(By.CLASS_NAME, "GoEOPd")
company_list = []

for block in job_blocks:
    title = block.find_element(By.CSS_SELECTOR, ".tNxQIb.PUpOsf").text if block.find_elements(By.CSS_SELECTOR,".tNxQIb.PUpOsf") else "N/A"
    company = block.find_element(By.CSS_SELECTOR, ".wHYlTd.MKCbgd.a3jPc").text if block.find_elements(By.CSS_SELECTOR,".wHYlTd.MKCbgd.a3jPc") else "N/A"
    location = block.find_element(By.CSS_SELECTOR, ".wHYlTd.FqK3wc.MKCbgd").text if block.find_elements(By.CSS_SELECTOR,".wHYlTd.FqK3wc.MKCbgd") else "N/A"

    print(f"{title}, {company}, {location}")
    company_list.append({
        "Job Title": title,
        "Company Name": company,
        "Location": location
    })

pd.DataFrame(company_list).to_csv("companies1.csv", index=False)
print("Data saved successfully in companies.csv")

driver.quit()
