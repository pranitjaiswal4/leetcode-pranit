class Solution {
        
    public int[] twoSum(int[] nums, int target) {
        int [] result = new int[2];
        HashMap<Integer, Integer> numsMap = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++) {
            numsMap.put(nums[i], i);
        }
        
        for(int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (numsMap.containsKey(complement) && numsMap.get(complement) != i) {
                result[0] = i;
                result[1] = numsMap.get(complement);
                break;
            }
        }
        
        return result;
    }
}