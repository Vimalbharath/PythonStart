from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s,e=0,len(letters)-1
        while s<=e:
            m=s+(e-s)//2
            if letters[m]>target:
                e=m-1
            else: # letters[m] <= target
                s = m + 1
        return letters[s%len(letters)]
    
# 1. Create an instance of the Solution class.
solution_instance = Solution()

# 2. Define your inputs.
letters = ["c", "f", "j"]
target = "a"

# 3. Call the method on the instance and store the result.
result = solution_instance.nextGreatestLetter(letters, target)

# 4. Print the result to verify the output.
print(f"Input: letters = {letters}, target = '{target}'")
print(f"Output: {result}")