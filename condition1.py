# -*- coding: utf-8 -*-

import collections
import xlrd

U=0#UNKNOW
Y=1#YES
N=2#NO

xlsx_file = r'table.xlsx'
book = xlrd.open_workbook(xlsx_file)  # 获得excel的book对象
sheet = book.sheet_by_index(0)  # 获取sheet对象
ncols = 4  # 总列数
nrows = sheet.nrows  # 总行数

# 本函数用于显示提取文案条件,返回条件dict：key值为情况，value为一个list，包含后面的关键值三项，且每一项为一个list
def __condition_judge():
   conditions = collections.OrderedDict()
   col_data = list()

   for i in range(ncols):#一共有4列
      col_data.append(sheet.col_values(i))
   for x in range(nrows):
      cdvalues = [0,0,0,0]
      for j in range(ncols):
         cdvalues[j] = col_data[j][x].split('/')
      conditions[col_data[0][x]] = [cdvalues[1], cdvalues[2], cdvalues[3]]

   return conditions

conditions = __condition_judge()

# 本函数传入关键词array，得其与表格关键字的匹配矩阵list：相符为1
def get_det(userinput):
   a = []#返回的矩阵
   b = []#用户的分词得的某个关键字与表格中的第几个关键字匹配
   b1 = {}#key为相匹配的表格行数，value为用户输入关键词的第几个
   c1 = {}
   d1 = {}
   num_userkey = len(userinput)
   #得到用户关键词与表格每列匹配的list:b,和
   for x in range(nrows):
      if x==0:#排除第一行
         continue
      for y in range(num_userkey):
         for z in range(len(conditions.values()[x][0])):
            if conditions.values()[x][0][z] == userinput[y]:
               b.append(x-1)
               b1[x-1]=y
         for z in range(len(conditions.values()[x][1])):
            if conditions.values()[x][1][z] == userinput[y]:
               c1[x-1] = y
         for z in range(len(conditions.values()[x][2])):
            if conditions.values()[x][2][z] == userinput[y]:
               d1[x-1] = y

   def __append(y,num):
         a.append(num)
         return y+1

   y=0
   for x in range(nrows-1):
      isadd=False
      if len(b)==0:
         a.append(U)
      elif x>b[len(b)-1] or y>=len(b):
            a.append(U)
      elif x==0 and 0==b[y]:   #b[y]存在时
         if d1.get(x)!=None:        #先考虑匹配了否定说法
            if b1.get(x)==d1.get(x) or b1.get(x)==d1.get(x)+1:
               y=__append(y,N)
               isadd =True
         if not isadd:              #没有匹配否定说法
            if [u'']==conditions.values()[x+1][1]:#该情况没有肯定说法，即有关键词为1
               y=__append(y,Y)
               isadd =True
            elif c1.get(x)!=None:   #匹配了肯定说法
               if b1.get(x)==c1.get(x) or b1.get(x)==c1.get(x)+1:
                  y = __append(y, Y)
                  isadd = True
            if not isadd:     #不符合以上条件时
               y=__append(y,U)
      elif b1.get(b[y])==num_userkey and x==b[y]:
         if d1.get(x)!=None:
            if b1.get(x)==d1.get(x) or b1.get(x)==d1.get(x)-1:
               y=__append(y,N)
               isadd =True
         if not isadd:
            if [u'']==conditions.values()[x+1][1]:
               y = __append(y, Y)
               isadd =True
            elif c1.get(x) != None:
               if b1.get(x) == c1.get(x) or b1.get(x) == c1.get(x) - 1:
                  y = __append(y,Y)
                  isadd = True
            if not isadd:
               y = __append(y, U)
      elif x==b[y]:
         if d1.get(x)!=None:
            if b1.get(x)==d1.get(x) or b1.get(x)==d1.get(x)-1 or b1.get(x)==d1.get(x)+1:
               y=__append(y,N)
               isadd =True
         if not isadd:
            if [u'']==conditions.values()[x+1][1]:
               y = __append(y, Y)
               isadd =True
            elif c1.get(x) != None:
               if b1.get(x) == c1.get(x) or b1.get(x) == c1.get(x) - 1 or b1.get(x) == c1.get(x) + 1:
                  y = __append(y, Y)
                  isadd = True
            if not isadd:
               y=__append(y,U)
      else:
         a.append(U)


   return a

#####例：
def example():
   userinput = [u'分居',u'离婚',u'同意', u'共同生活',u'尚未',u'破裂',u'一女']#]
   print get_det(userinput)
