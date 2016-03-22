#!/usr/bin/env python
# coding=utf-8


class MergeSort(object):

    def _merge(self, nums, p, q, r):
        left = nums[p:q + 1]
        right = nums[q + 1: r + 1]
        for i in range(p, r + 1):
            if len(left) > 0 and len(right) > 0:
                if left[0] <= right[0]:
                    nums[i] = left.pop(0)
                else:
                    nums[i] = right.pop(0)
            elif len(right) == 0:
                nums[i] = left.pop(0)
            elif len(left) == 0:
                nums[i] = right.pop(0)

    def _merge_sort(self, nums, p, r):
        if p < r:
            q = int((p + r) / 2)
            print 'sort0: ',p,q,r,nums
            self._merge_sort(nums, p, q)
            print 'sort1: ',p,q,r,nums
            self._merge_sort(nums, q + 1, r)
            print 'sort2: ',p,q,r,nums
            self._merge(nums, p, q, r)
            print 'sort3: ',p,q,r,nums

    def __call__(self, nums):
        self._merge_sort(nums, 0, len(nums) - 1)
        return nums

m = MergeSort()
nums = [3, 2, 1]
print m.__call__(nums)
