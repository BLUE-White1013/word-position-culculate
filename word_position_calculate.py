#coding = 'utf-8'


def word_search(text,search_list):    #type(text) = str
    ''' #search word in text to get its index and len'''
    for search in search_list:
        char_len = len(search)
        start = 0
        while True:
            index = text.find(search, start)
            if index ==-1:
                break
            print ( "%d|%d|%s" % (index,char_len, search))
            start = index + 1
    return


def word_position(text):
    '''change str to list then get their index'''
    word_dict = {}
    your_list = list(text)
    for i,value in enumerate(your_list):
        # print('%d|%s' %(i,value))
        word_dict[i] = value
    mystr = str(word_dict)
    print(mystr)
    return
#
# text = '在上海举行的首届两岸和平论坛于12日发布《论坛纪要》后闭幕。与会两岸学者、各界人士颇为振奋，期待该机制持续运作，让和平更有共识、分歧逐步消解。'
# search = ['上海','12日','两岸和平论坛','闭幕']
# # word_position(text)
# word_search(text,search)

import pandas as pd
import re

df = pd.read_excel('data.xlsx')   #数据文件
for i in range(2):   #excel行数
    text = df.ix[[i],['文本']].values[0].tolist()  #按行读取每列数据 numpy.array 变成list
    trigger = str(df.ix[[i],['trigger']].values[0].tolist())
    print(trigger)
    argument = df.ix[[i],['argument']].values[0].tolist()
    p = re.compile(r'[\u4e00-\u9fa5\\s]+')          #闭幕：14  保留trigger
    t_search = re.findall(p,trigger)    #search is a list
    # argu_str1 = str(argument[0]).split('，')
    # argu_str2 = str(argu_str1).split('；')
    # print(argu_str2)
    # a_str = str(str(argument[0]).split('，')).split('；')     #以；和分号分割argument成list
    a_str = str(argument[0])
    a_search = re.sub(r'[|]+[A-Za-z]+', '', a_str).split('；')
    print(a_search)
    res1 = word_search(str(text[0]),t_search)
    res2 = word_search(str(text[0]),a_search)










