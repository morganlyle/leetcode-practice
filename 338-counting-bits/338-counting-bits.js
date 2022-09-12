/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function(n) {
    
    const ans = [0];
    
    for (let i = 1; i < n+ 1; i++){
        ans.push(ans[i >> 1] + (i & 1));
    }
    return ans;
};