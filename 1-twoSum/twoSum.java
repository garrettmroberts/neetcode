import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
      HashMap<Integer, Integer> obj = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
          int remainder = target - nums[i];
          if (obj.get(remainder) != null) {
            int[] res = { i, obj.get(remainder)};
            return res;
          }
          obj.put(nums[i], i);
        }
        return null;
    }
}