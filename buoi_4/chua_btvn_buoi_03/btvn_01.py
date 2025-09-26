diem = float(input("Nhap vao so diem: "))
print("So diem:", diem)

if diem >= 9.0 and diem <=10:
  print("Xuat sac")
elif diem >=8 and diem < 9:
  print("Gioi")
elif diem >=6.5 and diem < 8:
  print("Kha")
elif diem >=5 and diem < 6.5:
  print("Trung binh")
elif diem < 5 and diem >= 0:
  print("Yeu")
else:
  print("Diem khong hop le")