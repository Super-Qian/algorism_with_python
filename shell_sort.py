#!/usr/bin/env python
# coding=utf-8


def shell_sort(nums):
    nums_len = len(nums)
    gap = nums_len / 2
    while gap > 0:
        for i in range(nums_len):
            m = i
            j = i + 1
            while j < nums_len:
                if nums[j] < nums[m]:
                    m = j
                j += gap
            if m != i:
                nums[m], nums[i] = nums[i], nums[m]
        gap /= 2
    return nums
if __name__ == '__main__':
    nums = [3, 2, 7, 3, -7, 1]
    print shell_sort(nums)
