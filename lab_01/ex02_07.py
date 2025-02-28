print("Nhập dòng văn bản của bạn (Nhập 'done' để kết thúc)")
lines=[]
while True:
    line=input()
    if line.lower()=="done":
        break
    lines.append(line)
print("Kết quả")
for x in lines:
    print(x.upper())