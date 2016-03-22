#!/usr/bin/env python
# coding=utf-8


class QuickSort(object):

    def _partition(self, nums, p, r):
        i = p - 1
        x = nums[r]
        for j in range(p, r):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def _quicksort(self, nums, p, r):
        if p < r:
            q = self._partition(nums, p, r)
            self._quicksort(nums, p, q - 1)
            self._quicksort(nums, q + 1, r)

    def __call__(self, nums):
        self._quicksort(nums, 0, len(nums) - 1)
        return nums

m = QuickSort()
nums = [2, 6, 4, 0, -4]
print m.__call__(nums)
