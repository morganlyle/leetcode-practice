/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    
    let max = 0;
    const set = new Set(nums);
    
    for (let num of set){
        if (set.has(num - 1)) continue;
        
        let curr = num
        let currMax = 1
        
        while (set.has(curr + 1)){
            curr++
            currMax++
        }
        max = Math.max(max, currMax)
    }
    
    return max
};