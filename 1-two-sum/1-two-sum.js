/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let newDict = {}
    
    for (let i = 0; i < nums.length; i++){
        if (target - nums[i] in newDict) {
            return [newDict[target - nums[i]], i];
            
        }
        else{
            newDict[nums[i]] = i;
        }
    }
};