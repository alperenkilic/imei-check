from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver'ı başlatın (örneğin, Firefox veya Chrome için)
driver = webdriver.Chrome()  # Chrome tarayıcı kullanımı

# Hedef URL'yi açın
driver.get("https://www.turkiye.gov.tr/imei-sorgulama")

# .txt dosyasından metinleri okuyun
with open("metinler.txt", "r") as file:
    metinler = file.readlines()

# Her satır için işlem yapın
for metin in metinler:
    # Metin girdisi alanını bulun ve metni gönderin
    text_input = driver.find_element(By.ID, "txtImei")
    text_input.clear()  # Önceki metni temizle
    text_input.send_keys(metin.strip())  # strip() ile baştaki ve sondaki boşlukları kaldırın

    # Gönder düğmesini bulun ve tıklayın
    submit_button = driver.find_element(By.CLASS_NAME, "submitButton")
    submit_button.click()

    # Sayfadan dönen veriyi alın
    response_text = driver.find_element(By.CLASS_NAME, "compact").text
    print(response_text)
    time.sleep(60)  # 1 saniye bekle
    driver.back()  # Geri düğmesine basarak önceki sayfaya dönün
    

# WebDriver'ı kapatın
driver.quit()
