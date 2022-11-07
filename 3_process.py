# -*- coding: utf-8 -*-
# @Author  : xuhc
# @Time    : 2022/9/19 13:21
# @Function:

import pandas as pd
import numpy as np

# docking_results = np.load("docking_results.npy", allow_pickle=True)
# binding_energy = docking_results[:, 2:22]

binding_energy = np.load("binding_energy_renew.npy", allow_pickle=True).T
m, n = binding_energy.shape
index = range(1, 21)
label = np.zeros((m,), dtype=int)
spec_label = []
poly_index = []
acids = ['alanine', 'arginine', 'asparagine', 'aspartic_acid',
             'cysteine', 'glutamic_acid', 'glutamine', 'glycine',
             'histidine', 'isoleucine', 'leucine', 'lysine',
             'methionine', 'phenalalanine', 'proline', 'serine', 'threonine',
             'tryptophan', 'tyrosine', 'valine']

for i in range(m):
    polypeptide = binding_energy[i]
    d = dict(zip(index, polypeptide))
    a = sorted(d.items(), key=lambda x: x[1])

    cnt = 0
    neg_res = []  # 结合自由能为负值的dictionary
    for kv in a:
        if kv[1] < 0:
            neg_res.append(kv)
        else:
            cnt = cnt + 1
    # if cnt != 0:
    #     print("第", i, "条八肽存在", cnt, "条无活性记录")

    if len(neg_res) > 1:

        # 绝对值最大的结合自由能
        lowest_energy = neg_res[0][1]
        # 对应的氨基酸序号
        lowest_energy_mol = neg_res[0][0]
    
        # 绝对值第二的结合自由能
        second_energy = neg_res[1][1]
        # 对应的氨基酸序号
        second_energy_mol = neg_res[1][0]
    
        if second_energy - lowest_energy >= 1:
            # 对某种氨基酸存在特异性
            print("第", i, "种八肽对第", lowest_energy_mol, "种氨基酸存在特异性,最低结合能为", lowest_energy,
                  "第二结合能为", second_energy, "差值为", second_energy - lowest_energy)
            # print(neg_res)
            label[i] = lowest_energy_mol
            spec_label.append(lowest_energy_mol)
            poly_index.append(i)
            
    elif len(neg_res) == 1:
        # 绝对值最大的结合自由能
        lowest_energy = neg_res[0][1]
        # 对应的氨基酸序号
        lowest_energy_mol = neg_res[0][0]
        
        print("第", i, "种八肽对第", lowest_energy_mol, "种氨基酸存在特异性,最低结合能为", lowest_energy)
        label[i] = lowest_energy_mol
        spec_label.append(lowest_energy_mol)
        poly_index.append(i)
    else:
        print("第", i, "种八肽与20种氨基酸均无活性，无法判断特异性")

location = np.where(label != 0)
flag = False
binding_energy_spec = []
for loc in location:
    if flag == False:
        binding_energy_spec = binding_energy[loc]
        flag = True
    else:
        binding_energy_spec = np.vstack((binding_energy_spec, binding_energy[loc]))

spec_label = np.array(spec_label).T
poly_index = np.array(poly_index).T
binding_energy_spec = np.c_[binding_energy_spec, spec_label]
binding_energy_spec = np.c_[binding_energy_spec, poly_index]

# np.save('binding_energy_spec0914.npy', binding_energy_spec)
# dataframe = pd.DataFrame(binding_energy_spec)
# dataframe.to_excel("binding_energy_spec0914.xlsx", index=False)