#!/usr/bin/env python
# coding=utf-8


def bubble_sort(nums):
    numsLen = len(nums)
    if numsLen < 2:
        return nums
    for i in range(numsLen - 1):
        for j in range(numsLen - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
if __name__ == '__main__':
    nums = [2, 5, 7, 52, 2345, 5, 2]
    print bubble_sort(nums)
