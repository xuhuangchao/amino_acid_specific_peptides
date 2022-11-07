# -*- coding: utf-8 -*-
# @Author  : xuhc
# @Time    : 2022/11/4 15:49
# @Function:
import os
import numpy as np
import pandas as pd


# 根据字典的值value获得该值对应的key
def get_dict_key(dic, value):
    key = list(dic.keys())[list(dic.values()).index(value)]
    return key


if __name__ == '__main__':
    path = "aa_all_results"
    datanames = os.listdir(path)
    acidlist = []
    binding_energy = []
    flag = False
    for i in datanames:
        inputpath = path + "\\" + i
        energy = list()
        with open(inputpath, 'r', encoding='utf-8') as infile:
            for line in infile:
                write_line = line
                line = line.strip("\n")
                line = line.strip("(")
                line = line.strip(")")
                data_line = line.split(",")
                # print(data_line)
                energy.append(float(data_line[0]))
                tai_acid = data_line[1].split(".")[0]
                tai = tai_acid.split("_")[0]
                if len(tai_acid.split("_")) > 2:
                    acid = tai_acid.split("_")[1] + "_" + tai_acid.split("_")[2]
                else:
                    acid = tai_acid.split("_")[1]

                if acid not in acidlist:
                    acidlist.append(acid)

                outpath = "output/" + acid + ".txt"
                with open(outpath, "a") as f:
                    f.write(write_line)  # 自带文件关闭功能，不需要再写f.close()
        print(i, "已读完")
    print(acidlist)
