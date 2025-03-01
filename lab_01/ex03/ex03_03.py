  
print("nhâp danh sách số nguyên (phân cách nhau bởi dấu ,)")
str_list=input()
int_list=list(map(int,str_list.split(',')))
my_tuple=tuple(int_list)
print("tuple từ list ",my_tuple)