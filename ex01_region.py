# -*- coding: utf-8 -*-

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ex01_region.py
이 프로그램은 엑셀파일을 입력받아 3개의 폴더별(시기별 분류)로 
각각의 텍스트파일로 출력하는 프로그램이다.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

import xlrd

WORK_PATH = "C:/Users/User/Desktop/file"
DATA_PATH = WORK_PATH + "/data"
RESULT_PATH = WORK_PATH + "/result"


def text_write_1(tot1, d):
    f = open(RESULT_PATH + "/2003/text{0}.txt".format(tot1), 'w',
             encoding = "utf-8")
    f.write(d)
    f.close()
    

def text_write_2(tot2, d):
    f = open(RESULT_PATH +"/2008/text{0}.txt".format(tot2), 'w',
             encoding = "utf-8")
    f.write(d)
    f.close()
    
def text_write_3(tot3, d):
    f = open(RESULT_PATH +"/2013/text{0}.txt".format(tot3), 'w',
             encoding = "utf-8")
    f.write(d)
    f.close()   
 
def main():
    input_file_name = DATA_PATH + "/data_560.xlsx"
    
    wb = xlrd.open_workbook(input_file_name)
    ws = wb.sheet_by_index(0)
    ncol = ws.ncols
    nlow = ws.nrows
    tot1 = 0 ; tot2 = 0 ; tot3 = 0 ;   
    print(ncol, "    ", nlow)
    
    for i in range(1,nlow):
        m = str(ws.col_values(2)[i]) 
        d = ws.col_values(1)[i]
        if m < "200302" or m > "201802":
            pass
        else:
            if m >= "200302" and m < "200802":
                tot1 = tot1 + 1
                text_write_1(tot1, d)
            else:
                if m >= "200802" and m < "201302":
                    tot2 = tot2 + 1
                    text_write_2(tot2, d)
                else:
                    tot3 = tot3 +1
                    text_write_3(tot3, d) 
                                                                                                  
    print("1기 파일수는 {0}개,".format(tot1),
          "2기 파일수는 {0}개,".format(tot2), 
          "3기 파일수는 {0}개,".format(tot3), 
          "   총 계 {0}개".format(nlow-1))     
 
main()
