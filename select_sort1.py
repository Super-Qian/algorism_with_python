#!/usr/bin/env python
# coding=utf-8


def select_sort(nums):
    nums_len = len(nums)
    if nums_len < 2:
        return nums
    for i in range(nums_len - 1):
        smallest = nums[i]
        location = i
        for j in range(i, nums_len):
            if nums[j] < smallest:
                smallest = nums[j]
                location = j
            if i != location:
                nums[i], nums[location] = nums[location], nums[i]
    return nums
if __name__ == '__main__':
    nums = [2, 3, 7, 1, -4]
    print select_sort(nums)
