/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const obj = {}
    for (let i = 0; i < nums.length; i++) {
      const remainder = target - nums[i];
      if (obj[remainder] !== undefined) {
        return [i, obj[remainder]]
      }

      obj[nums[i]] = i;
    }
};