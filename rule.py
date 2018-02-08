#  coding: utf-8

from condition1 import get_det
import word_ord

def rule_init():
    file = 'marryrule.txt'
    book = open(file,'r')  # 获得excel的book对象
    rules=[]
    lines=''
    is_start=False

    def dispose(a_str):
        if len(a_str) and a_str[0]!=' ':
            __i=1
            __i+=1
            keys = []
            for word in word_ord.fenci(a_str):
                keys.append(word)
            rules.append((get_det(keys),a_str))


    for strs in book:
        line= strs.decode('gbk')
        if len(line)>4 and is_start:
            if line[0] == u'第' and line[2] == u'条' or line[3] == u'条' or line[4] == u'条':
                dispose(lines)
                lines = line
            elif line[0] == u'第' and line[2] == u'章':
                print
                if len(lines.split('\n'))!=2:
                    dispose(lines)
            else:
                lines += line
        elif line[:3] == u'第一条':
            dispose(line)
            is_start=True

    return rules

def rule_for_user(user_array):
    rules=[]
    isfor_user=True
    i=1
    for det,rule in rule_init():
        for x in range(12):
            if 1==det[x]:
                if 1!=user_array[x]:
                    isfor_user=False
            if 2==det[x]:
                if 2!=user_array:
                    isfor_user=False
        if isfor_user:
            rules.append(rule)
        i+=1
    return rules


#表格完善后吧婚姻法的矩阵写入文件，平时调用.
def get_rule_file():
    pass

if __name__=='__main__':
    i=1
    for det in rule_init():
        print i
        print det
        i+=1