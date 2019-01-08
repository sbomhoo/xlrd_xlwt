# -*- coding: utf-8 -*-

def main():
    """
    ************************************************************************
    폴더별로 나눠져있는 text0을 new_text0로 통합
    ************************************************************************
    """
    
    #연도별 텍스트 파일 갯수
    folders = [2003,2008,2013] 
   
    for folder in folders:
        g = open("C:/Users/User/Desktop/file/result/new_text0.txt", 'a', encoding = "utf-8")
        
        f = open("C:/Users/User/Desktop/file/result/{0}/text0.txt".format(folder), 'r', encoding = "utf-8")
        line = f.readlines()            
        g.writelines(line)    
        g.write("\n")
        f.close()
    
        #print(" {0} 처리 파일수는 {1}개,".format(year,i))
        g.close()          
                                                                                     

main()
