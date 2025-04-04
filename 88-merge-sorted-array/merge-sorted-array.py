class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length = len(nums1)
        zerocount = 0
        nums1.reverse()
        for i in range(length):
            if zerocount < n:
                if nums1[0] == 0:
                    nums1.pop(0)
                    zerocount += 1
                elif nums1[0] !=0:
                    break
        nums1.reverse()      
        i=0
        while i < len(nums1):
            if nums2:
                if nums1[i] > nums2[0]:
                    nums1.insert(i, nums2[0])
                    nums2.pop(0)
                    i -=1
            else:
                break
            i+=1
        nums1.extend(nums2)


                
        