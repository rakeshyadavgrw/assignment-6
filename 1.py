#***********Q1***************#
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i, n = 0, len(s)
        ans = []
        for c in s:
            if c == 'I': 
                ans.append(i)
                i+=1
            else:
                ans.append(n)
                n-=1
        ans.append(i)
        return ans
    
    #***********Q2***************#
    class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] < target: r += 1
            elif matrix[r][c] > target: c -= 1
            else: return True
        
        return False
    
    #***********Q3***************#
    class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False;
        l = 0;
        r = len(arr) - 1
        while l + 1 < len(arr) - 1 and arr[l] < arr[l + 1]: 
            l += 1
        while r - 1 > 0 and arr[r] < arr[r - 1]: 
            r -= 1
        return l == r
    
    #***********Q4***************#
    class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length =0
        hash={}
        count=0
        for i in range(len(nums)):
            current=nums[i]
            if current==0:
                count-=1 # decrement our count if our current element is 0
            else:
                # increment our count if current element is 1
             count+=1

            if count==0:
                # if count is 0, we have a new subarray with length+1
                max_length=i+1
            if count in hash:
                max_length=max(max_length,i-hash[count]) 
            else:
                hash[count]=i
        return max_length
    
     #***********Q5***************#
    class Solution:
         def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
             nums1.sort()
             nums2.sort()
             n, res = len(nums1), 0
             for i in range(n):
                 res += nums1[i] * nums2[n - i - 1]
             return res
         
         #***********Q6***************#
         class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        res = []
        for k in counter.keys():
            
            if k == 0:
                # handle zero as special case
                if counter[k] % 2 > 0:
                    return []
                res += [0] * (counter[k] // 2)
                
            elif counter[k] > 0:
                x = k
                
                # walk down the chain
                while x % 2 == 0 and x // 2 in counter:
                    x = x // 2
                    
                # walk up and process all numbers within the chain. mark the counts as 0
                while x in counter:
                    if counter[x] > 0:
                        res += [x] * counter[x]
                        if counter[x+x] < counter[x]:
                            return []
                        counter[x+x] -= counter[x]
                        counter[x] = 0
                    x += x
        return res
    
    #***********Q7***************#
    class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom, num = 0, n-1, 0, n-1, 1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                matrix[top][i] = num 
                num += 1
            top += 1
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if top <= bottom:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        return matrix
    
     #***********Q8***************#
     class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1, c1, c2 = len(mat1), len(mat1[0]), len(mat2[0])
        res = [[0] * c2 for _ in range(r1)]
        mp = defaultdict(list)
        for i in range(r1):
            for j in range(c1):
                if mat1[i][j] != 0:
                    mp[i].append(j)
        for i in range(r1):
            for j in range(c2):
                for k in mp[i]:
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res

############

class Solution(object):
  def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    ret = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    for i, row in enumerate(A):
      for k, a in enumerate(row):
        if a:
          for j, b in enumerate(B[k]):
            if b:
              ret[i][j] += a * b
    return ret



