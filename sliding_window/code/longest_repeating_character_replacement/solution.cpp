#include <cassert>
#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int characterReplacement(std::string s, int k) {
        std::unordered_map<char,int> freq;
        int left = 0, maxFreq = 0, best = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            freq[s[right]]++;
            maxFreq = std::max(maxFreq, freq[s[right]]);
            if (right - left + 1 - maxFreq > k) {
                freq[s[left]]--;
                left++;
            }
            best = std::max(best, right - left + 1);
        }
        return best;
    }
};

int main() {
    Solution sol;
    assert(sol.characterReplacement("ABAB", 2) == 4);
    assert(sol.characterReplacement("AABABBA", 1) == 4);
    assert(sol.characterReplacement("A", 0) == 1);
    return 0;
}
