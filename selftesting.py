# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:53:44 2022

@author: phwangk
"""

import re

def gNorm(matrix_string, size):
    
    collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
    list_matrix = collect_numbers(matrix_string)
    list_final = []
    
    counter = 0
    for i in range(int(size)):
        row_i = []
        for j in range(int(size)):
            row_i.append(list_matrix[counter])                      
            counter +=  1
        list_final.append(row_i)
    
    integralList = []
    for row_i in range(len(list_final)):
        tempRowList = []
        for col_j in range(len(list_final[row_i])):
            if col_j ==0:
                intUpper = list_final[row_i][0]
            else:
                # Integrating calculation in here, and substitute the upper bound inside
                coeff_new = list_final[row_i][col_j]/(col_j+1)                                
                int_result_temp = coeff_new*(intUpper**(col_j+1))                    
                tempRowList.append(int_result_temp)                                    
    integralList.append(tempRowList)            
    return round(sum(integralList[i][j] for i in range(len(integralList)) for j in range(len(integralList[i]))),2)



def oneNorm(matrix_string, size):
    collect_numbers = lambda x : [int(i) for i in re.split("[^0-9]", x) if i != ""]
    list_matrix = collect_numbers(matrix_string)
    list_final = []
    
    counter = 0
    for i in range(int(size)):
        row_i = []
        for j in range(int(size)):
            row_i.append(list_matrix[counter])                      
            counter +=  1
        list_final.append(row_i)
        
    col_sums = [0] * len(list_final[0])
    for row in list_final:
        for col in range(0,len(row)):
            col_sums[col] += row[col]

    norm = max(col_sums)
    return norm # an int