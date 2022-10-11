# def rotate_array(rotation_number: int, array: []) -> []:
#     i = 0
#     length = len(array)
    
#     while i < rotation_number:
#         last = array[-1]
#         print(f"last: {last}")
#         for j in range(length-1):
#             print(j)
#             print(f"array[j] before: {array[j]}")
#             array[j+1] = array[j]
#             print(f"array[j] after: {array[j]}")
#         array[0] = last
#         i += 1
#     return array

# def rotate(n, l):
#     return l[n:] + l[:n]
from collections import deque

def main():
    items = deque([1, 2])
    items.append(3)
    items.rotate(1)
    # try:
    #     print("Inter the rotation number:")
    #     number = int(input())
    # except Exception as e:
    #     print(e)
    # result = default_array.rotate(3)
    print(items)
    

if __name__ == "__main__":
    main()