so = int(input("Hay nhap vao 1 so: "))
for so_can_kiem_tra in range(2, so+1):
  # Can kiem tra so_can_kiem_tra co dung la chi chia het cho 1 va chinh no hay khong
  # print("Dang kiem tra so", so_can_kiem_tra, "xem co phai la so nguyen to hay khong")
  da_chia_het_cho_may_so_roi = 0
  for so_chia in range(1, so_can_kiem_tra + 1):
    if(so_can_kiem_tra % so_chia == 0):
      # print("So", so_can_kiem_tra, "chia het cho", so_chia)
      da_chia_het_cho_may_so_roi += 1
  if(da_chia_het_cho_may_so_roi == 2):
    print("So", so_can_kiem_tra, "la so NGUYEN TO")
