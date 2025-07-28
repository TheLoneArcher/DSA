class Solution {
    public static String mergeAlternately(String word1, String word2) {
        StringBuilder merged = new StringBuilder();
        int length = Math.max(word1.length(), word2.length());
        for(int i=0; i<length; i++) {
            if(i < word1.length()) {
                   merged.append(word1.charAt(i));  
            } 
            if(i < word2.length()) {
                merged.append(word2.charAt(i));
            }
        }
        return merged.toString();
    }
    public static void main (String args[]) {
        System.out.println(mergeAlternately("abc", "pqr"));
        System.out.println(mergeAlternately("ab", "pqrs"));
        System.out.println(mergeAlternately("abcd", "pq"));
    }
}