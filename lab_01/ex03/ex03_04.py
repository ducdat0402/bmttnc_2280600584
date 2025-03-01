def truy_cap_pt(data):
    first=data[0]
    last=data[-1]
    return first,last

print("nhâp danh sách số nguyên (ví dụ (1,2,3) )")
tuple_list=eval(input())
first,last=truy_cap_pt(tuple_list)

print("phần tử đầu tiên",first)
print("phần tử cuối cùng",last)
