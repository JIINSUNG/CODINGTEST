/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let cnt = 0
    for (i = 0; i< nums.length-2; i++)
    {
        if (nums[i] === 0){
            cnt += 1
            for (j = i; j < i+3; j++){
                if (nums[j] == 1)
                    nums[j] = 0
                else
                    nums[j] = 1
            }
        }
    }

    for (i = nums.length-3; i < nums.length; i++){
        if (nums[i] === 0)
            return -1
    }

    return cnt




};