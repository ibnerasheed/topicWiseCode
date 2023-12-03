'''
• Each input can have multiple solutions. The output should match with either one of them.

Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)

• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()

Given an unsorted integer array, find a pair with the given sum in it.


'''


def findPair(nums, target):
 
   
    for i in range(len(nums) - 1):
 
        
        for j in range(i + 1, len(nums)):
 
            
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
   
    print('Pair not found')
 
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)