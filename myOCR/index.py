
import time
import os
from PIL import Image
from common import  ocr, methods
# 1. 开始截屏
last = time.time()
lp = os.linesep
def shellsystemExec(cmd):
  # return _code = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE);
  return os.system(cmd);
i = 1
filename = '%s.png' % i
shellsystemExec('idevicescreenshot %s'%filename)



while True:


    img = Image.open("./1.png")

    # 文字识别
    question, choices = ocr.ocr_img(img)

    # 用不同方法输出结果，取消某个方法在前面加上#

    # 打开浏览器方法搜索问题
    methods.run_algorithm(0, question, choices)
    # 将问题与选项一起搜索方法，并获取搜索到的结果数目
    methods.run_algorithm(1, question, choices)
    # 用选项在问题页面中计数出现词频方法
    methods.run_algorithm(2, question, choices)

    go = input('输入回车继续运行,输入 n 回车结束运行: ')
    if go == 'n':
        break

    print('------------------------')
