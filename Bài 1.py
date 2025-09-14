a = int(input("Nhập cạnh đầu tiên của tam giác: "))
b = int(input("Nhập cạnh thứ hai của tam giác: "))
c = int(input("Nhập cạnh thứ ba của tam giác: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
elif a == b == c:
    print("Tam giác đều")
elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("Tam giác vuông")
elif a == b or a == c or b == c:
    print("Tam giác cân")
else:
    print("Tam giác thường")







   


