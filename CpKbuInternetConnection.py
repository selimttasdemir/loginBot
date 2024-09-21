from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = ''
Passwd = "passwd"
UserName = "ogrenciNo@ogrenci.karabuk.edu.tr"

try:
    driver = webdriver.Chrome(driver_path)
    
    driver.get("https://cp.karabuk.edu.tr/connect/PortalMain/")
    
    username_field = driver.find_element(By.NAME, "Username")
    password_field = driver.find_element(By.NAME, "Password")

    username_field.send_keys(UserName)
    time.sleep(1)
    password_field.send_keys(Passwd)
    time.sleep(1)
    username_field.send_keys(Keys.RETURN)
    time.sleep(1)
    print("Giriş yapıldı")
    time.sleep(1)

except Exception as e:
    print("Bu sayfaya ulaşılamıyor.")
    print(f"Hata mesajı: {e}")
    driver.quit()
    
finally:
    driver.quit()