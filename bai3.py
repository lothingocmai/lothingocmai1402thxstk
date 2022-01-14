def KTSoThuanNghich(n):
    str1 = str(n)  # ep kieu so n thanh chuoi
    str2 = str1[::-1]  # dao nguoc chuoi str1
    if (str1 == str2):
        return True         #trả về kết quả đúng là số thuận nghịch
    else:
        return False         #trả về kq sai k phải là số thuận nghịch

h=len(input("Họ của bạn là:")) #nhập họ
d=len(input("Tên đệm của bạn là:")) #nhập tên đệm
t=len(input("Tên của bạn là:")) #nhập tên
n = str(h)+str(d)+str(t) #dãy số lượng họ tên đệm
print("Dãy số tên của bạn là",n) #in ra dãy
print("Số", n , "là" ,KTSoThuanNghich(n)) #in ra kq true hoặc false