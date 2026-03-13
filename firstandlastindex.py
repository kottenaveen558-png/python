def Findindexes(arr,target):
    first = -1
    last = -1
    flag = False
    for i in range(len(arr)):
        if arr[i] == target:
            flag =True
            if first == 0:
                first = i
            else:
                last = i
    
    if flag:
        print(f"first:{first} last:{last}")
    else:
        print("element not found")

arr = [5, 3, 8, 3, 9, 3, 1]
target = 3

Findindexes(arr,target)
