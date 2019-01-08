  # -*- coding: utf-8 -*-

"""
ex01_01.py

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

WORK_PATH = "C:/TM/region_201609"
DATA_PATH = WORK_PATH + "/data"
RESULT_PATH = WORK_PATH + "/result"
RESULT1_PATH = RESULT_PATH + "/2003"
RESULT2_PATH = RESULT_PATH + "/2008"
RESULT3_PATH = RESULT_PATH + "/2013"
"""

def main():
    """
    ************************************************************************
    f파일로 읽아서 g파일(text0)로 쓰는 프로그램
    1. 합할 파일 갯수를 입력하면 됨
    2. 2003, 2008, 2013으로 변환시켜 작업해야 함(각각 2곳)  
    ************************************************************************
    """
   
    g = open("C:/Users/User/Desktop/file/result/2008/text0.txt", 'a',
             encoding = "utf-8")
    
    tot = 0    
    total = input("처리할 파일 수는? ")
    tot = int(total)
    tot = tot + 1
    for i in range(1,tot):
        f = open("C:/Users/User/Desktop/file/result/2008/text{0}.txt".format(i), 'r',
             encoding = "utf-8")
        line = f.readline()
        #line = line + ","
        g.write(line)
        f.close()
    g.close()          
                                                                                                          
    print("처리 파일수는 {0}개,".format(i))
#               
 
main()
