# -*- coding: utf-8 -*-
# @Time    : 2021/10/18 13:20
# @Author  : Cheung0
import ddddocr
import time
import getpass
from selenium import webdriver
from PIL import Image

# 记录账号密码
username = input("请输入账号:")
password = getpass.getpass("请输入密码:")

# 启动浏览器
driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("http://my.nuist.edu.cn/index.portal?.pn=p3629")
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)

# 等待验证码出现
time.sleep(3)

# 截取验证码图片
driver.save_screenshot("./screen.png")
element = driver.find_element_by_id('captchaImg')
capimg = Image.open("./screen.png")
capimg = capimg.crop((997, 333, 1140, 410))
capimg.save("./capimg.png")

# 读取验证码
ocr = ddddocr.DdddOcr()
with open('./capimg.png', 'rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)

# 输入验证码并登录
driver.find_element_by_id("captcha").send_keys(res)
driver.find_element_by_id("login_submit").click()
time.sleep(2)
driver.quit()
