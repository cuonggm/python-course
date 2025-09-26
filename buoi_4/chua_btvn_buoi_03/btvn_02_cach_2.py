# Yeu cau nguoi dung nhap vao 1 so
so = int(input("Hay nhap vao 1 so: "))

# Kiem tra tu  2 -> so nhap vao xem so nao la so nguyen to
for so_can_kiem_tra in range(2, so+1):

  # Tam thoi coi so hien tai la so nguyen to
  co_phai_la_so_nguyen_to_hay_khong = True

  # Chay tu 2 toi so_can_kiem_tra - 1 xem co so nao duoc chia het hay khong
  for so_chia in range(2, so_can_kiem_tra):
    # Neu co
    if so_can_kiem_tra % so_chia == 0:
      # thi in ra day khong phai la so nguyen to
      # print("So", so_can_kiem_tra, " khong phai la so nguyen to")
      # danh dau lai day khong phai la so nguyen to
      co_phai_la_so_nguyen_to_hay_khong = False
      break # pha vo vong lap gan no nhat
  if co_phai_la_so_nguyen_to_hay_khong == True:
    print("So", so_can_kiem_tra, "la so NGUYEN TO")
