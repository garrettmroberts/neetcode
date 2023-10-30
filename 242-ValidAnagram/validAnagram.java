class Solution {
  public boolean isAnagram(String s, String t) {
    int[] used = new int[26];
    for (char c : s.toCharArray()) {
      used[c - 'a']++;
    }
    for (char c : t.toCharArray()) {
      used[c - 'a']--;
    }

    for (int i = 0; i < used.length; i++) {
      if (used[i] != 0) return false;
    }

    return true;
  }
}