# def rotate_array(array: []) -> []:
#     temp_last = array[-1]
#     i = 1
#     while i < len(array)-1:
#         print(f"i before increasing: {i}")
#         array[i+1] = array[i]
#         i += 1
#         print(f"i after increasing: {i}")
#     return array

def rotate_array(array: []) -> []:
    return [array.pop()] + array

def iterate_array(array: [], iterations: int) -> []:
    if array:
        j = 0
        while j < iterations:
            array = rotate_array(array)
            j += 1
    return array

def main():
    list = []
    
    items = iterate_array(list, 4)
    print(items)


if __name__ == "__main__":
    main()