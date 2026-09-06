#include <cassert>
#include <algorithm>
#include <string>
#include <unordered_map>

class Solution {
public:
    int lengthOfLongestSubstringKDistinct(std::string s, int k) {
        if (k == 0) return 0;
        std::unordered_map<char,int> count;
        int left = 0, result = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            count[s[right]]++;
            while ((int)count.size() > k) {
                if (--count[s[left]] == 0) count.erase(s[left]);
                left++;
            }
            result = std::max(result, right - left + 1);
        }
        return result;
    }
};

int main() {
    Solution sol;
    assert(sol.lengthOfLongestSubstringKDistinct("eceba", 2) == 3);
    assert(sol.lengthOfLongestSubstringKDistinct("aa", 1) == 2);
    assert(sol.lengthOfLongestSubstringKDistinct("aabbcc", 2) == 4);
    return 0;
}
