# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:54:55 2022

@author: xuhc
"""

import pandas as pd
import numpy as np


def selectk(k, input_type):
    aminoacid = spec_results['aminoacid']
    # 筛选氨基酸类别为输入的多肽数据
    spec_input_type = spec_results[aminoacid == input_type]
    # 获取多肽和此种氨基酸的对接结合自由能
    binding_energy = spec_input_type.iloc[:, input_type - 1]
    # 计算多个结合自由能的平均值，并排序
    mean = np.mean(binding_energy)
    binding_energy = binding_energy.sort_values()
    # 筛选出结合自由能绝对值大于平均值的多肽（标准：结合自由能绝对值大入选）
    print(binding_energy[binding_energy < mean])
    loc = binding_energy[binding_energy < mean]
    cnt = 0
    output = []
    for i, v in loc.items():
        if cnt < k:
            # 记录前k个特异性多肽的序号
            res = spec_results.iloc[i, 21]
            # print(res)
            output.append(res)
            cnt = cnt + 1
    print(output)
    return output


if __name__ == "__main__":
    spec_results = pd.read_excel("binding_energy_spec0919.xlsx", sheet_name=0)
    m, n = spec_results.shape
    docking_results = np.load("docking_results.npy", allow_pickle=True)
    # 输入氨基酸的种类，寻找排名前k个特异性多肽
    input_type = 13
    k = 5
    # 输出特异性多肽的信息
    output = selectk(k, input_type)
    for i in output:
        print(docking_results[i])


