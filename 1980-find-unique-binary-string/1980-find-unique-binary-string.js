/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {
    
    const dictionary = {};
    for (const num of nums) {
        dictionary[num] = true;
    }

    for (let i = 0; i <= nums.length; i++) {
        const binary = i.toString(2).padStart(nums[0].length, '0');
        if (!(binary in dictionary)) {
            return binary;
        }
    }
};