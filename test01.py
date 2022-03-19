import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# 读取文本线索
# ku:读入的规则库，列表前n-1位为线索，第n位为推导结果 例如[['有奶','哺乳动物']]表示‘有奶’-->哺乳动物
# dw:动物库，存储所有可能推导出的结果库
# l:所有产生式中包含的元素，是一个不重复列表，用来输出

def getrd_txt(ku, dw, l):
    with open("RD.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            ku.append(line.split(' '))
        for val in ku:
            # 获取文本文件中所有推导条件，将推导条件通过与l取差集方式得到所有最终可能推导的结果集
            for val1 in val[:-1]:
                dw.append(val1)
            l += val
    # 先转set去重复，再转回list
    l = list(set(l))
    l.sort()
    # 转换为所有最终可能推导到的结果集
    dw = list(set(l).difference(set(dw)))
    return ku, dw, l


# 根据用户输入推导结果
# map1:用户输入后的字典，Key为产生式中的元素，Value为置信度
# ku:规则库
def tuidao(map1, ku):
    while True:
        # 标记修改状态，0表示未修改，1表示有修改
        flag = 0
        for i in range(0, len(ku)):
            count = 0
            for j in range(0, len(ku[i]) - 1):
                if map1[ku[i][j]] == 1:
                    count = count + 1
            # 置信度比之前高才能算有效推导
            if map1[ku[i][-1]] < round(count / (len(ku[i]) - 1), 2):
                map1[ku[i][-1]] = round(count / (len(ku[i]) - 1), 2)
                if round(count / (len(ku[i]) - 1), 2) == 1:
                    print("由%s-->%s" % (ku[i][:-1], ku[i][-1]))
                flag = 1
        if flag == 0:
            break


# 用户输入线索，存储在map1中
def user_input(map1, l):
    print("请输入线索,用空格分割:")
    for x in input().split():
        map1[l[int(x) - 1]] = 1
    return map1


if __name__ == "__main__":
    # ku:读入的规则裤，列表前n-1位为线索，第n位为推导结果
    ku = list()
    # l:不重复列表，用来输出
    l = list()
    # 字典，存储所有线索推导的置信度
    map1 = {}
    dw = list()
    i = 0
    ku, dw, l = getrd_txt(ku, dw, l)
    # 格式化输出信息
    for item in l:
        i = i + 1
        print("%-2d%-6s" % (i, item), end='')
        # 初始化字典，置信度为0
        map1[str(item)] = 0
        if i % 4 == 0:
            print()
    print()
    map1 = user_input(map1, l)
    tuidao(map1, ku)
    # 输出推导结果
    while True:
        for item in dw:
            if map1[item] == 1:
                print("推导结果：%s" % item)
                exit(0)
        inp = input("没有推导出信息哦！是否补充线索?[y/n]")
        if inp == 'y':
            map1 = user_input(map1, l)
            tuidao(map1, ku)
        else:
            exit(0)
