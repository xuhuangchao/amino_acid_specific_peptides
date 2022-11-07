# -*- coding: utf-8 -*-
# @Author  : xuhc
# @Time    : 2022/11/7 11:20
# @Function:

import os
import numpy as np
import pandas as pd


# 根据字典的值value获得该值对应的key
def get_dict_key(dic, value):
    key = list(dic.keys())[list(dic.values()).index(value)]
    return key


if __name__ == '__main__':
    path = "output"
    datanames = os.listdir(path)
    filenamelist = []
    binding_energy = []
    flag = False
    total = 2898000
    for i in datanames:
        filenamelist.append(i)
        inputpath = path + "\\" + i
        energy = list()
        with open(inputpath, 'r', encoding='utf-8') as infile:
            for line in infile:
                line = line.strip("\n")
                line = line.strip("(")
                line = line.strip(")")
                data_line = line.split(",")
                # print(data_line)
                energy.append(float(data_line[0]))
            if len(energy) < total:
                fill = total - len(energy)
                print("补全缺失位", fill)
                for j in range(fill):
                    energy.append(100.0)

        energy_ = np.array(energy)
        print(energy_.shape)
        if flag == False:
            binding_energy = energy_
            flag = True
        else:
            binding_energy = np.vstack((binding_energy, energy_))
    print(binding_energy.shape)
    index = range(1, 21)
    acid_dict = dict(zip(index, filenamelist))

    files = ['alanine', 'arginine', 'asparagine', 'aspartic_acid',
             'cysteine', 'glutamic_acid', 'glutamine', 'glycine',
             'histidine', 'isoleucine', 'leucine', 'lysine',
             'methionine', 'phenalalanine', 'proline', 'serine', 'threonine',
             'tryptophan', 'tyrosine', 'valine']

    # for file in files:
    #     key = get_dict_key(acid_dict, file)
    #     print(key)

    np.save('binding_energy_renew.npy', binding_energy)
    # dataframe = pd.DataFrame(binding_energy)
    # dataframe.to_csv("binding_energy.csv", index=False)
