/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    
    const strx = strs.map(word => word.split('').sort().join(''));
        
    const result = {};
    
    for (let i = 0; i < strs.length; i++){
        if (!result[strx[i]]){
            result[strx[i]] = [strs[i]];
        }
        else {
            result[strx[i]].push(strs[i])
        }
    }
    
    return Object.values(result)
    
};