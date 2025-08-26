//https://leetcode.com/problems/valid-parentheses/

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack();
        int size = s.length();
        if (size == 1)
            return false;
        for (int i = 0; i < size; i++) {

            if (s.charAt(i) == '[' || s.charAt(i) == '(' || s.charAt(i) == '{') {
                st.push(s.charAt(i));
                continue;
            }

            if (!st.isEmpty() && st.peek() == '(') {
                if (s.charAt(i) == ')')
                    st.pop();
                continue;
            }
            if (!st.isEmpty() && st.peek() == '{') {
                if (s.charAt(i) == '}')
                    st.pop();
                continue;
            }
            if (!st.isEmpty() && st.peek() == '[') {
                if (s.charAt(i) == ']')
                    st.pop();
                continue;
            }
            if (st.isEmpty() && s.charAt(i) == ']' || s.charAt(i) == '}' || s.charAt(i) == ')') {
                return false;
            }

        }
        return st.size() == 0;
    }
}