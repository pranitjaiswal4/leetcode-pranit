class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        int i = 0, j = 0;
        
        HashMap<Character, Integer> map = new HashMap();
        
        while (j < s.length()) {
            
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)) + 1, i) ;
            } 
            
            map.put(s.charAt(j), j);            
            longest = Math.max(longest, j - i + 1);
            j += 1;
        }
        
        return longest;
    }
}