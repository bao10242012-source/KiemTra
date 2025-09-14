date = int(input("Nhập ngày: ")) 
month = int(input("Nhập tháng: ")) 
year = int(input("Nhập năm: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if month == 2:
    if is_leap and date <= 29:
        print("True")
    elif not is_leap and date <= 28:
        print("True")
    else:
        print("False")
elif month in (1, 3, 5, 7, 8, 10, 12):
    if 1 <= date <= 31:
        print("True")
    else:
        print("False")
elif month in (4, 6, 9, 11):
    if 1 <= date <= 30:
        print("True")
    else:
        print("False")
else:
    print("False")