def input_list(n):
    arr = []
    i = 0
    while True:
        x = input(f"Input item[{i}]: ")
        try:
            arr.append(int(x))
            i += 1
            if i >= n:
                break
        except:
            print("Chưa nhập đúng số nguyên. Nhập lại!")
    return arr
def tinhtong(arr):
    bientong = 0
    for i in arr:
        bientong+=i
    return bientong
n = int(input("Nhập số phần tử tính tổng : "))
arr = input_list(n)
print(arr)
print(tinhtong(arr))
def tinhtich(arr):
    tich=1
    for i in arr:
        tich *= i
    return tich
n = int(input("Nhập số phần tử tính tích : "))
arr = input_list(n)
print(arr)
print(tinhtich(arr))
def timmax(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if max < arr[i]:
           max = arr[i]
    return max
n = int(input("Nhập số phần tử tìm số max : "))
arr = input_list(n)
print(arr)
print(timmax(arr))
def timmin(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if  min > arr[i]:
            min = arr[i]
    return min
n = int(input("Nhập số phần tử tìm số min : "))
arr = input_list(n)
print(arr)
print(timmin(arr))
def sole(arr):
    result = []
    for i in arr:
        if i%2!=0:
            result.append(i)
    return result
n = int(input("Nhập số phần tử tìm số lẻ : "))
arr = input_list(n)
print(arr)
print(sole(arr))
def sochan(arr):
    result = []
    for i in arr:
        if i%2==0:
            result.append(i)
    return result
n = int(input("Nhập số phần tử tìm số chẵn : "))
arr = input_list(n)
print(arr)
print(sochan(arr))
def kiem_tra_snt(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count == 2:
        return "La so nguyen to"
    return "Khong la so nguyen to"
n = int(input("Nhập số : "))
print(kiem_tra_snt(n))