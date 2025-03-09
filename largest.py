from typing import List
def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]
if __name__ == "__main__":
    n = int(input())  
    arr = list(map(int, input().split())) 
    print(sortArr(arr))

