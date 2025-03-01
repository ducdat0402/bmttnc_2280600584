def tong_list(lst):
    tong=0
    for x in lst:
        if x%2==0:
            tong+=x
    return tong
    
print("nhâp danh sách số nguyên (phân cách nhau bởi dấu ,)")
str_list=input()
int_list=list(map(int,str_list.split(',')))
print("tong các số chẳn là ",tong_list(int_list))