#Find the Runner-Up Score!
n = int(input())
arr = map(int, input().split())
arr1=[*set(arr)]
arr1.sort()
print(arr1[len(arr1)-2])