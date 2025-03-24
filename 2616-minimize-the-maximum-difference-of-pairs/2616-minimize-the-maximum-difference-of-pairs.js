/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minimizeMax = function(nums, p) {

    const n = nums.length
    nums.sort((a,b) => a-b)
    const can_make = (target) => {
        let pair = 0 
        let i = 0

        while (i < (nums.length-1)){
            if ((nums[i+1]-nums[i]) <= target){
                pair += 1
                i += 2
            }
            else {
                i += 1
            }
        }
        if (pair >= p){
            return true  
        }
        return false
    }


    let left = 0
    let right = nums[n-1] - nums[0]
    console.log(right)

    while (left <= right){
        let mid = Math.floor((left + right) / 2)
        if (can_make(mid)){
            right = mid - 1
        }
        else
            left = mid + 1
    }
    return left

};

