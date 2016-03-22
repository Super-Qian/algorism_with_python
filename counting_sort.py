#!/usr/bin/env python
# coding=utf-8

# 序列元素必须是整数
# 元素的最大值不能大于等于序列的长度


def counting_sort(nums, k):
    temp_nums = []
    new_nums = nums[:]
    for j in range(0, k):
        temp_nums.append(0)
    for j in range(0, len(nums)):
        temp_nums[nums[j]] = temp_nums[nums[j]] + 1
    for j in range(1, k):
        temp_nums[j] = temp_nums[j] + temp_nums[j - 1]
    for j in range(len(nums) - 1, -1, -1):
        new_nums[temp_nums[nums[j]] - 1] = nums[j]
        temp_nums[nums[j]] = temp_nums[nums[j]] - 1
    return new_nums

nums = [2, 1, 4, 3]
print counting_sort(nums, 5)
