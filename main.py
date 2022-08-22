n, m = map(int, input().split())
element = list(map(int, input().split()))
count = 0
arr = [i for i in range(1, n+1)]

for i in range(len(element)) :
    if len(arr)/2 >= arr.index(element[i]) :
        while True :
            if arr[0] == element[i] :
                del arr[0]
                break
            a = arr[0]
            arr.remove(a)
            arr.append(a)
            count += 1
    else :
        while True :
            if arr[0] == element[i] :
                del arr[0]
                break
            a = arr[-1]
            arr.remove(a)
            arr.insert(0, a)
            count += 1  

print(count)