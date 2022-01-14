Nhapten = str ( input ( "Tên của bạn là:" )) #nhập tên
print ( "xin chào" , Nhapten ) #in ra tên
print("Tên của bạn có", len(Nhapten), "kí tự") #độ dài tên

n = int(input("Nhập độ dài tên n = ")) #nhập độ dài tên vừa in ra
d = dict() #khai báo
for i in range(1, n + 1): #vòng lặp
    d[i] = i * i

print(d) #in ra kq dãy dictionnary