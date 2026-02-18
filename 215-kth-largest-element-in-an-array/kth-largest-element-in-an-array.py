class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[l]

            # 3-way partition
            lt = l          # nums[l:lt] < pivot
            i = l           # current index
            gt = r          # nums[gt:r] > pivot

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            # Now:
            # nums[l:lt] < pivot
            # nums[lt:gt+1] == pivot
            # nums[gt+1:r] > pivot

            if k < lt:
                return quickSelect(l, lt - 1)
            elif k > gt:
                return quickSelect(gt + 1, r)
            else:
                return nums[k]

        return quickSelect(0, len(nums) - 1)