def chia_het5 (so_nhi_phan):
    so_thap_phan=int(so_nhi_phan,2)
    if so_thap_phan %5==0:
        return True
    else:
        return False

print("Nhập các số nhị phân (phân cách bởi dấu ,): ")
str_list_snp=input()
list_snp=str_list_snp.split(',')
so_chia_het_cho5=[so for so in list_snp if chia_het5(so)]

if len(so_chia_het_cho5)>0:
    ketqua=('.'.join(so_chia_het_cho5))
    print('Kết quả số chia hết cho 5 là',ketqua)
else:
    print('Không có số nào chia hết cho 5')
    