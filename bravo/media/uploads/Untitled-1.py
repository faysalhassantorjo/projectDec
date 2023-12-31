# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
    
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
    
#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     left_index, right_index = 0, 0
    
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] >= right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1
    
#     result.extend(left[left_index:])
#     result.extend(right[right_index:])
    
#     return result

# n=int(input())
# for i in range(n):
#     n,m=map(int,input().split())
#     arr1=list(map(int,input().split()))
#     arr2=list(map(int,input().split()))
#     array = merge_sort(arr1 + arr2)[::-1]
#     array.sort(reverse=True)
#     for i in array:
#         print(i,end=' ')

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the number of balls and rattles
    n, m = map(int, input().split())
    
    # Read the sizes of sets of balls and rattles
    balls = list(map(int, input().split()))
    rattles = list(map(int, input().split()))
    
    # Sort the sets of balls and rattles in descending order
    balls.sort(reverse=True)
    rattles.sort(reverse=True)
    
    # Merge and print the sorted sets
    merged_array = sorted(balls + rattles, reverse=True)
    print(*merged_array)
