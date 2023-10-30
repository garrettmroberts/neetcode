/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
  if (s.length !== t.length) return false;

  let used  = new Int16Array(26);

  for(let i = 0; i < s.length; i++) {
    used[s.charCodeAt(i) - 97]++;
    used[t.charCodeAt(i) - 97]--;
  }

  for (let i = 0; i < used.length; i++) {
    if (used[i] !== 0) return false;
  }

  return true;
};


console.log(isAnagram("anagram", "nagaram"))