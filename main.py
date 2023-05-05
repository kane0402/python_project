from selenium import webdriver
from selenium.webdriver.common.by import By

search = input("請輸入關鍵字:")

driver_path = f"D:/driver/msedgedriver.exe"
browser = webdriver.Edge(executable_path=driver_path)

url = f'https://pixabay.com/images/search/{search}/'
browser.get(url)

# 找到包含圖片的div元素
div_element = browser.find_element(
    by=By.XPATH, value="//div[@style='max-width:1824px;padding:10px 3px 20px;margin:auto']")

img_elements = div_element.find_elements(by=By.TAG_NAME, value='img')[:5]

img_srcs = []
for img in img_elements:
    img_srcs.append(img.get_attribute('src'))

browser.close()

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    {images}
</body>
</html>
"""

images_html = ""
for img_src in img_srcs:
    images_html += f"<img src = '{img_src}'>"

html = html_template.format(title=search, images=images_html)

with open(f"{search}.html", "w") as file:
    file.write(html)
