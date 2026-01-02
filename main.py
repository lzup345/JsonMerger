#include<iostream>

"""
 ┌───┐   ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┬───┐ ┌───┬───┬───┐
 │Esc│   │ F1│ F2│ F3│ F4│ │ F5│ F6│ F7│ F8│ │ F9│F10│F11│F12│ │P/S│S L│P/B│
 └───┘   └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┴───┘ └───┴───┴───┘
 ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┐ ┌───┬───┬───┐ ┌───┬───┬───┬───┐
 │~ `│! 1│@ 2│# 3│$ 4│% 5│^ 6│& 7│* 8│( 9│) 0│_ -│+ =│ <---- │ │Ins│Hom│PUp│ │N L│ / │ * │ - │
 ├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┤ ├───┼───┼───┤ ├───┼───┼───┼───┤
 │ Tab │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │{ [│} ]│| \\ │ │Del│End│PDn│ │ 7 │ 8 │ 9 │   │
 ├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴─────┤ └───┴───┴───┘ ├───┼───┼───┤ + │
 │ Caps │ A │ S │ D │ F │ G │ H │ J │ K │ L │: ;│" '│ Enter  │               │ 4 │ 5 │ 6 │   │
 ├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴────────┤     ┌───┐     ├───┼───┼───┼───┤
 │ Shift  │ Z │ X │   │   │ B │ N │ M │< ,│> .│? /│  Shift   │     │ ↑ │     │ 1 │ 2 │ 3 │   │
 ├─────┬──┴─┬─┴──┬┴───┴───┴───┴───┴───┴──┬┴───┼───┴┬────┬────┤ ┌───┼───┼───┐ ├───┴───┼───┤  ││
 │     │Win │Alt │         Space         │ Alt│Win │Menu│Ctrl│ │ ← │ ↓ │ → │ │   0   │ . │<─┘│
 └─────┴────┴────┴───────────────────────┴────┴────┴────┴────┘ └───┴───┴───┘ └───────┴───┴───┘
服了，注释是不能放单个反斜杠吗

不要问我为什么没有左Ctrl、C和V
问就是不知道
"""
#不明所以的注释↑↑↑


#导入一些库
import os
import sys
import json
from deepmerge import Merger #用于json合并
import bext #彩色文本

#方便使用颜色
def print_colour_f(text,colour):
    bext.fg(colour)     #设定颜色
    print(text)         #输出文本
    bext.fg('reset')    #恢复颜色

# 懒癌犯了
def line_break():
    print("\n")

print_colour_f("创建时间：26/01/01","blue")
print_colour_f("by lzup\n","blue")

#输出当前工作目录
print_colour_f("当前工作目录"+os.getcwd()+"\n","green") #输出当前工作目录

while True: #死循环 通过break跳出
    #询问用户文件路径
    input_json_path_high = input("请输入要处理的第1个json文件路径|当前文件优先级：较高\n>")
    input_json_path_low = input("请输入要处理的第2个json文件路径|当前文件优先级：较低\n>")

    #输出当前处理文件
    print("当前待处理json文件：")
    print_colour_f("高优先级json文件："+input_json_path_high,"green")
    print_colour_f("低优先级json文件："+input_json_path_low,"green")

    #询问用户是否确认
    print("是否确认？(y/n)")
    json_path_confirm=input('>')
    if json_path_confirm.lower() == 'y': #如果确认
        break #退出循环以继续程序

    else: #如果输入的为其他值，则输出提示语并回到循环开头
        print_colour_f("请重新输入路径！","red")



#检测outputs是否存在、是否为目录
if not os.path.exists("outputs"):

    os.mkdir("outputs") #如果不存在，则创建

elif not os.path.isdir("outputs"): #检测outputs是否为目录
    #用户确认是否删除
    print_colour_f("当前工作目录"+os.getcwd()+"\n","green") #输出当前工作目录

    #lower防大小写错误
    if input('为程序能够继续运行，需删除当前工作目录下的outputs文件\n是否继续? (y/n)\n>').lower()=='y':
        #如果条件为真，则删除原outputs文件并创建outputs文件夹

        line_break() #单纯为了看着舒服

        os.remove("outputs") #删除原文件
        os.mkdir("outputs")  #创建新文件夹
    else:
        #如果条件为否，则退出程序
        print_colour_f("程序已退出！","red") #提示语
        sys.exit(0) #退出程序

#防异常
try:
    with open(input_json_path_high, 'r', encoding='utf-8') as file:
        process_json_file_high = json.loads(file.read()) #读取文件
        file.close() #关闭文件
except FileNotFoundError: #当文件未找到时
    print_colour_f("高优先级文件未找到！请检查文件路径","red") #提示语
    sys.exit(0) #退出程序

try:
    with open(input_json_path_low, 'r', encoding='utf-8') as file:
        process_json_file_low = json.loads(file.read()) #读取文件
        file.close() #关闭文件
except FileNotFoundError: #当文件未找到时
    print_colour_f("低优先级文件未找到！请检查文件路径", "red") #提示语
    sys.exit(0) #退出程序

#还是Ctrl+C、V好用
merger = Merger([(list, ["append"]),(dict, ["merge"]),(set, ["union"]),],["override"],["override"])
merged = merger.merge(process_json_file_low, process_json_file_high) #合并!
json_outputs_data=json.dumps(merged,indent=2,ensure_ascii=False) #写回json形式 ##修复中文字符输出为unicode码点的问题

os.chdir("outputs") #切换至输出路径
print("请输入输出文件的名称：")
output_file_name=input('>') #接受用户输入
file = open(output_file_name, "w") #创建并打开文件
file.write(json_outputs_data) #写入文件
file.close() #关闭文件
print_colour_f("处理完毕!","blue") #提示语

#完工时间：2026/01/02
#好累
