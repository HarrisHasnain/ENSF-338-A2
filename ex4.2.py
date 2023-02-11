def replace(arr, length, index, val):

    if (index < 0 or index >= length):
        print("Invalid index.")
        return arr

    del arr[index]

    arr.insert(index, val)

    return arr
   
if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5]
    replace(nums, 5, 2, 10)
    print(nums)