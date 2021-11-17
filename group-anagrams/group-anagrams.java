class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> map = new HashMap();
        List<List<String>> result = new ArrayList<List<String>>();
        
        for(int i = 0; i < strs.length; i++) {
            char[] word = strs[i].toCharArray();
            Arrays.sort(word);
            String sorted = String.valueOf(word);
            
            ArrayList<String> value;
            if (map.containsKey(sorted)) {
                value = map.get(sorted);
            } else {
                value = new ArrayList();
            }
            
            value.add(strs[i]);
            map.put(sorted, value);
        }
        
        for (Map.Entry<String, ArrayList<String>> entry : map.entrySet()) {
            result.add(entry.getValue());
        }
        
        // How to sort if needed (using Comparator):
        /*
        Collections.sort(result, new Comparator<List<String>>() {
            public int compare(List<String> o1, List<String> o2) {
                return o1.get(0).compareTo(o2.get(0));
            }
        });
        */
        
        return result;
    }
}
