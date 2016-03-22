#!/usr/bin/env python
# coding=utf-8


def quick_sort(nums):
    if len(nums) < 2:
        return nums
    return quick_sort([lt for lt in nums[1:] if lt < nums[0]])\
        + nums[0:1]\
        + quick_sort([ge for ge in nums[1:] if ge >= nums[0]])

nums = [3, 7, 2, 9, 0, -3]
print quick_sort(nums)
