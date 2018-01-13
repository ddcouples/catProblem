import pytesseract # install
import time
import os
import subprocess
import re
# from selenium import webdriver  # install
from PIL import Image

last = time.time()
lp = os.linesep
t= 119 / 563
b= 372 / 563
def shellsystemExec(cmd):
  # return _code = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE);
  return os.system(cmd);
def shellSubExec(cmd):
  return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE);
# 截图
def shotImg (url='./img/cddh/', i=2, exp='.jpg'):
  img = Image.open(url + str(i) + exp)
  w = img.size[0]
  h = img.size[1]
  print(w, h)
  box = (0, t * h, w, b * h)
  _img = img.crop(box)
  _img.save(url+str(i)+'_thu'+exp)
  return _img

def showChin(url='./img/cddh/', i=2, exp='.jpg'):
  last = time.time()
  img = Image.open(url + str(i) + exp)
  code = pytesseract.image_to_string(img, lang='chi_sim,eng')
  now = time.time()
  print(code, now - last)
def showChiByImg(img):
  code = pytesseract.image_to_string(img, lang='chi_sim')
  return textHandle(code)
def textHandle(text):
  tList = []
  _texts = []
  text = text.strip()
  text = text.replace(lp, ' ')
  texts = text.split('?')
  texts[0] and tList.append((texts[0] + '?').replace(' ', ''))
  if len(texts) > 1 and texts[1]:
    _texts = re.split(r'[;,\s]\s*', texts[1])
  secText = []
  for i in _texts:
    if i != '':
      secText.append(i)
  tList.append(secText)
  return tList

# driver = webdriver.Chrome()
# driver.maximize_window()  # 最大化浏览器

# driver.get("https://www.baidu.com/s?wd=" + result[0])
# 1. 开始截屏
i = 1
filename = '%s.png' % i
shellsystemExec('idevicescreenshot %s'%filename)
result = showChiByImg(shotImg(url='./',i=1, exp='.png'))
# result = '?!'
print(result)
shellSubExec('google-chrome https://www.baidu.com/s?wd=%s'%result[0])
now = time.time()
print('耗时：', now-last)