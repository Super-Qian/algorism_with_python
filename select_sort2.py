#!/usr/bin/env python
# coding=utf-8


def select_sort(nums):
    nums_len = len(nums)
    for i in range(nums_len):
        min_index = i
        for j in range(i + 1, nums_len):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

if __name__ == '__main__':
    nums = [2, 5, 9, 30, -3, 6]
    print select_sort(nums)
