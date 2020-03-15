import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver
driver = webdriver.Chrome()
url = 'http://www.amazon.com/war-peace-leo-nikolayevich-tolstoy/dp/1427030200'
driver.get(url)
# time.sleep(20)
# 单击修改地址(继续)按钮
driver.find_element_by_xpath('//span[@class="a-button-inner"]').click()
# 单击图书预览按钮
driver.find_element_by_id('sitbLogoImg').click()
imagelist = set()
# 等待页面加载完成
time.sleep(5)
#单向右箭头可以单击时,开始翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    #获取与加载的新页面(一次可以加载多个页面,但是重复的页面不能加载到集合中)
    pages = driver.find_elements_by_xpath('//div[@class="pageImage"]/div/img')
    for page in pages:
        # time.sleep(12)
        image = page.get_attribute('src')
        imagelist.add(image)
driver.quit()
#用tesseract处理我们收集的图片URL链接
for image in sorted(imagelist):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(['tesseract', 'page.jpg', 'page'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r')
    print(f.read())
