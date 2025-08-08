#https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s,e=0,len(arr)-1
        while(s<=e):
            m=s+(e-s)//2
            if arr[m]<arr[m-1]:
                s=m
            elif arr[m]<arr[m+1]:
                e=m+1
            else:
                return s+1