## Selenium ile e-devlet üzerinden imei sorgulama

Bu belge, Python kullanarak Selenium kütüphanesi ile IMEI sorgulama işlemi yapmak için kullanılabilecek bir örnek kodu içerir.

### Gereksinimler

- Python 3.9
- Selenium kütüphanesi
- Selenium Webdriver (örneğin, Chrome veya Firefox için)

### Nasıl Kullanılır

1. Python ve gerekli bağımlılıkları yükleyin. Selenium kütüphanesi için `pip3 install selenium` komutunu kullanabilirsiniz.

2. Webdriver'ı başlatın (örneğin, Chrome için `webdriver.Chrome()`).

3. Hedef URL'yi açın (`driver.get("https://www.turkiye.gov.tr/imei-sorgulama")`).

4. Metin girdisi alanını bulun ve IMEI numarasını gönderin.

```python
text_input = driver.find_element(By.ID, "txtImei")
text_input.send_keys("111111111111111")
```

5. Gönder düğmesini bulun ve tıklayın.

```python
submit_button = driver.find_element(By.CLASS_NAME , "submitButton")
submit_button.click()
```

6. Sayfadan dönen veriyi alın ve ekrana yazdırın.

```python
response_text = driver.find_element(By.CLASS_NAME, "compact").text
print(response_text)
```

7. WebDriver'ı kapatın (`driver.quit()`).

### Uyarı

- Bu kod örneği, belirli bir web sitesi yapısına dayanmaktadır ve HTML yapısı değiştiğinde güncellenmesi gerekebilir.

- Web scraping ve otomasyon işlemleri, web sitesi sahiplerinin kullanım koşullarına ve hukuki düzenlemelere tabi olabilir. Kullandığınız web sitesinin kullanım koşullarını ve yasal düzenlemeleri dikkate alın.
