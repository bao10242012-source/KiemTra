def tach_ho_ten(full_name):
    words = full_name.strip().split()
    if len(words) < 2:
        return ["Không hợp lệ: Cần ít nhất 2 từ trong họ tên."]
    ho = words[0]
    ten = words[-1]
    if len(words) == 2:
        return [f"Họ: {ho}", f"Tên: {ten}"]
    else:
        ten_dem = ' '.join(words[1:-1])
        return [f"Họ: {ho}", f"Tên đệm: {ten_dem}", f"Tên: {ten}"]
ho_ten = input("Nhập họ và tên đầy đủ: ")
ket_qua = tach_ho_ten(ho_ten)
for dong in ket_qua:
    print(dong)










   


