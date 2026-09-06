#include <cassert>
#include <string>

class Solution {
public:
    std::string minWindow(std::string s1, std::string s2) {
        int n = s1.size(), m = s2.size();
        std::string result;
        int i = 0;
        while (i < n) {
            int j = 0;
            while (i < n && j < m) {
                if (s1[i] == s2[j]) j++;
                i++;
            }
            if (j < m) break;
            int end = i - 1;
            j = m - 1;
            int k = end;
            while (k >= 0 && j >= 0) {
                if (s1[k] == s2[j]) j--;
                k--;
            }
            int start = k + 1;
            if (result.empty() || end - start + 1 < (int)result.size())
                result = s1.substr(start, end - start + 1);
            i = start + 1;
        }
        return result;
    }
};

int main() {
    Solution sol;
    assert(sol.minWindow("abcdebdde", "bde") == "bcde");
    assert(sol.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u") == "");
    assert(sol.minWindow("abcde", "ace") == "abcde");
    return 0;
}
