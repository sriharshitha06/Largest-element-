def findLargestElement(arr, n):
    max_value = arr[0] 
    for i in range(1, n):  
        if max_value < arr[i]:
            max_value = arr[i]
    return max_value

if __name__ == "__main__":
    n = int(input())  
    arr = list(map(int, input().split())) 
    
    max_value = findLargestElement(arr, n)
    print(max_value)
