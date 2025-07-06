"""
Problem: Two Sum
Link: https://workat.tech/problem-solving/practice/two-sum
Approach: Hashmap optimization
Time: O(n)
Space: O(n)
"""
from typing import List
class Solution:
	def twoSum(self, A: List[int], target: int) -> List[int]:
		seen = {}
		for i in range(len(A)):
			c= target-A[i]
			if c in seen:
				return [seen[c],i]
			seen[A[i]]=i