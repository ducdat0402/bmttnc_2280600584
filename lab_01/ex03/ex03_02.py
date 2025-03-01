
print("nhâp danh sách số nguyên (phân cách nhau bởi dấu ,)")
str_list=input()
int_list=list(map(int,str_list.split(',')))
print("kết quả đảo ngược là ",int_list[::-1])