hoten = input('Tên của bạn là:') #nhập họ tên
Masv = input('Mã sinh viên của bạn là: ') #nhập mã sinh viên (kiếu số)
print(hoten + Masv) #in ra họ tên và MSV

def split(hoten): #tao hàm tách chữ
    ketqua = [char for char in hoten]
    return ketqua
print("In ra màn hình phân tách dấu , là: ") #in
print(split(hoten))
print(tuple(Masv))
