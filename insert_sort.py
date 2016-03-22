#!/usr/bin/env python
# coding=utf-8


def insert_sort(nums):
    nums_len = len(nums)
    if nums_len < 2:
        return nums
    for i in range(1, nums_len):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

if __name__ == '__main__':
    nums = [3, 4, 2, 98, 2, 6]
    print insert_sort(nums)
