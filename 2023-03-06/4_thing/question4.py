list1 = [8, 7, 6, 5, 9, 3, 2, 4]
list2 = [1.1, 5.4, 6.8, 9.3, 4.2, 3.8, 12.5]


def calc_average(nums):
    if len(nums) == 0:
        return 0
    sum_nums = nums[0]
    for i in range(1, len(nums)):
        sum_nums += nums[i]

    average = sum_nums / len(nums)
    return average


print(f"The average = {calc_average(list1)}")
print(f"The average = {calc_average(list2)}")
