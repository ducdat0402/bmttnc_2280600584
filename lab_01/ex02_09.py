def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

number=int(input("Nhập số n: "))

if isPrime(number):
    print(number,"Là số nguyên tố")
else:
    print(number,"Không là số nguyên tố")
    