from pyautogui import typewrite,press,prompt,alert
from time import sleep
from random import choice,uniform
from sys import exit

alert(text='开始之前，请先将输入法调整至英文，已经是英文请忽略。\n调整之后按确认键', title='提示', button='OK')

def integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

while True:
    try:
        for_num=prompt(text='请输入发送数量', title='发送数量' , default='')
        if not integer(for_num) or for_num==0:
            alert(text='你输入了非法字符(只能输入数字哦,但也不能是0)', title='警告', button='OK')
        else:
            break
    except:
        exit(0)

sleep(10)

try:
    with open('message.txt','r',encoding='u8') as f:
        lines=f.readlines()

    for i in range(int(for_num)):
        typewrite(choice(lines), interval=uniform(0.001,0.01))
        press('enter')
        sleep(uniform(0.5,2.0))
except:
    alert(text='遇到一些问题,即将退出\n若要联系作者:\n邮箱:zzj_zijun0925@163.com (常用)\noscarzhu@aliyun.com\n电话:18053255821',title='致命性错误',button='OK')

alert(text='轰炸完成', title='提示', button='OK')