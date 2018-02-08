# -*- coding: utf-8 -*-

import CentreParag
import condition
import result
import numpy as np

list_condition = []
list_result = []
for i in range(1, 11):
    flag_condition = condition.condition_judge(i)
    list_condition.append(flag_condition)
    flag_result = result.result_judge(i)
    list_result.append(flag_result)
array_condition = np.array(list_condition)
array_result = np.array(list_result)

#print array_condition
#print array_result