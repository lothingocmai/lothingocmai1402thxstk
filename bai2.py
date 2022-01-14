tendem = input("Tên đệm của bạn là:") #nhập tên đệm
print(tendem) #in tên đệm
def tongdodaiten(n): #khai báo và thực hiện vòng lặp while
    tong = 0;
    while (n > 0):
        tong = tong + n % 10;
        n = int(n / 10);
    return tong;
a = input("Tên của bạn là:") #nhập tên
n=len(a)+len(tendem) #tính
print("Độ dài tên là:",n) #in ra độ dài tên đệm + tên
print("Tổng độ dài tên là", n, "là", tongdodaiten(n)); #tính tổng độ dài tên