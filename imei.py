from selenium import webdriver
from selenium.webdriver.common.by import By

# WebDriver'ı başlatın (örneğin, Firefox veya Chrome için)
driver = webdriver.Chrome()  # Chrome tarayıcı kullanımı

# Hedef URL'yi açın
driver.get("https://www.turkiye.gov.tr/imei-sorgulama")

# Metin girdisi alanını bulun ve metni gönderin
text_input = driver.find_element(By.ID, "txtImei")  # txtImei, HTML'de metin girdisi alanının kimliğine karşılık gelmelidir
text_input.send_keys("111111111111111")

# Gönder düğmesini bulun ve tıklayın
submit_button = driver.find_element(By.CLASS_NAME , "submitButton")  # submitButton, HTML'de gönder düğmesinin kimliğine karşılık gelmelidir
submit_button.click()

# Sayfadan dönen veriyi alın
response_text = driver.find_element(By.CLASS_NAME, "compact").text  # response_id, dönen veri alanının kimliğine karşılık gelmelidir
print(response_text)

# WebDriver'ı kapatın
driver.quit()
