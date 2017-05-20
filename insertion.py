def insertion_sort(nums):
    for i in range(1, len(nums)):
        chk = nums[i]
        j = i-1
        while (j>=0) and (nums[j]> chk):
            nums[j+1] = nums[j]
            j = j - 1
        nums[j+1] = chk
        

def main():
    a = eval(input("Enter nos which have to be sorted"))
    a = list(a)
    insertion_sort(a)
    print(a)
