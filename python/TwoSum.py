""" 
    given a list find the values which sum are equal to a target
"""


# class Solution:
    # def twoSum(self, nums, target):
    #     returnList = []
    #     for i, val in enumerate(nums):
    #         find = target - val
    #         # print(i)
    #         # print(nums[i])
    #         # print(val)
    #         # print(target)
    #         # print(find)
    #         # print(nums)
    #         # if(nums.index(find) == i):
    #         #     returnList.extend([i])
    #         if(find in nums and nums.index(find) != i):
    #             returnList.extend([i])
    #     return returnList
class Solution:
    def twoSum(self, nums, target):
        h = {}
        print(nums)
        for i, num in enumerate(nums):
            n = target - num
            print("i: ", i)
            print("h: ", h)
            print("n: ", n)
            if n not in h:
                h[num] = i
            elif n in h:
                print("n: ", n)
                return [h[n], i]

                
            

def main():
    NewInstance = Solution();
    print(NewInstance.twoSum([11,15,1,2,7,5,3,6], 9))



if __name__ == "__main__":
    main()

"""

"""