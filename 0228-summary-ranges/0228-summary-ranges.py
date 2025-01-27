class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        last_value = nums[0]
        temp = [nums[0]]
        answer = []
        for i in range(1, len(nums)):
            if nums[i] == last_value+1:
                temp.append(nums[i])
                last_value = nums[i]
            else:
                if len(temp) == 1:
                    answer.append(str(temp[0]))
                else:
                    answer.append(str(temp[0])+'->'+str(temp[-1]))
                last_value = nums[i]
                temp = [nums[i]]
        if temp:
            if len(temp) == 1:
                answer.append(str(temp[0]))
            else:
                answer.append(str(temp[0])+'->'+str(temp[-1]))

        return answer 
            

            
