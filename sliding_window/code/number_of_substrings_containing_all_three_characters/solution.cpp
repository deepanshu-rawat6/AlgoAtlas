#include <cassert>
#include <string>

class Solution {
public:
    int numberOfSubstrings(std::string s) {
        int count[3] = {0, 0, 0};
        int left = 0, result = 0;
        for (int right = 0; right < (int)s.size(); right++) {
            count[s[right] - 'a']++;
            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                count[s[left] - 'a']--;
                left++;
            }
            result += left;
        }
        return result;
    }
};

int main() {
    Solution sol;
    assert(sol.numberOfSubstrings("abcabc") == 10);
    assert(sol.numberOfSubstrings("aaacb") == 3);
    assert(sol.numberOfSubstrings("abc") == 1);
    return 0;
}
