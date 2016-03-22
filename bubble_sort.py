#!/usr/bin/env python
# coding=utf-8


def bubble_sort(nums):
    nums_len = len(nums)
    if nums_len < 2:
        return nums
    for i in range(nums_len - 1):
        for j in range(nums_len - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
if __name__ == '__main__':
    nums = [2, 5, 7, 52, 2345, 5, 2]
    print bubble_sort(nums)
