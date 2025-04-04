class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst_result = []

        if (len(nums) == 0): return []
        if (len(nums) == 1): return [str(nums[0])]

        lst_add = []
        for i in range(len(nums)):
            n = nums[i]
            if (len(lst_add) == 0):
                lst_add.append(n)
            else:
                if (n-1) == lst_add[-1]:
                    lst_add.append(n)
                else:
                    if (len(lst_add) == 1):
                        lst_result.append(str(lst_add[0]))
                    else:
                        lst_result.append(f"{lst_add[0]}->{lst_add[-1]}")    
                    lst_add = [n]

            if (len(lst_add) > 0) and (i == len(nums) -1):
                if (len(lst_add) == 1):
                    lst_result.append(str(lst_add[0]))
                else:
                    lst_result.append(f"{lst_add[0]}->{lst_add[-1]}")    

        return lst_result