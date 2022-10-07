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



def extractNumbers_NoFormat_Square(output_string, size, style):
    # delete space character element
    temp_list = output_string.split('\n') #['myAwesomeMatrix Test 5', '1 0', '3 1', '']
    temp_list =  [i for i in temp_list if i] #['myAwesomeMatrix Test 5', '1 0', '3 1']
    temp_list = temp_list[1:]  #TODO: check final grading need print the test name or not
    # temp_list.remove("")
    style_pass = False
    
    element_list = []
    # compostite the result to list of list
    for r in range(size):
        row_i = []
        row_list_temp = temp_list[r].strip().split(' ')
        
        print(r)
        print(row_list_temp)
        for c in range(size):
            
            print(type(row_list_temp[c]))
            row_i.append(int(row_list_temp[c]))
        element_list.append(row_i)
    
    if style == 'symmetric':
        fail_count = 0
        for r in range(size):
            for c in range(size):
                if r != c:
                    if (element_list[r][c] != element_list[c][r]):
                        fail_count +=1
    
    elif style == 'upper':
        fail_count = 0
        for r in range(size):
            for c in range(size):
                if r > c:
                    if (element_list[r][c] != 0):
                        fail_count +=1
    elif style == 'lower':
        fail_count = 0
        for r in range(size):
            for c in range(size):
                if r < c:
                    if (element_list[r][c] != 0):
                        fail_count +=1
                        
    elif style == 'diagonal':
        fail_count = 0
        for r in range(size):
            for c in range(size):
                if r != c:
                    if (element_list[r][c] != 0):
                        fail_count +=1
    else:
        regular_dum = 1
        
    return fail_count
    
    
if __name__ == '__main__':
    a = 1
    output_string = 'myAwesomeMatrix Test 5\n 1 0 \n 3 1 \n'
    extractNumbers_NoFormat_Square(output_string, 2, 'lower')
    