class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> map = new HashMap();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        
        Stack <Character> stack = new Stack();
        
        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                if (!stack.isEmpty()) {
                    if (map.get(s.charAt(i)) == stack.peek()) stack.pop();
                    else return false;
                } else return false;
            } else {
                stack.add(s.charAt(i));
            }
        }
        
        return stack.isEmpty();
    }
}