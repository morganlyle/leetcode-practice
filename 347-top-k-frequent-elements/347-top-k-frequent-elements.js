/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    
    const map = new Map();
    
    for (let num of nums){
        map.set(num, map.get(num) + 1 || 1);
    }
    const result = []; 

    for (let [key, value] of map){
        result.push([key, value]);
    }
    result.sort((x, y) => y[1] - x[1]);
    return result.slice(0, k).map((a) => a[0])
    
};