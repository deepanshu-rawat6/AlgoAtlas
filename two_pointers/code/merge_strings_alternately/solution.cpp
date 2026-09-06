#include <cassert>
#include <string>

class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {
        std::string result;
        int i = 0, j = 0;
        while (i < (int)word1.size() && j < (int)word2.size()) {
            result += word1[i++];
            result += word2[j++];
        }
        result += word1.substr(i);
        result += word2.substr(j);
        return result;
    }
};

int main() {
    Solution sol;
    assert(sol.mergeAlternately("abc", "pqr") == "apbqcr");
    assert(sol.mergeAlternately("ab", "pqrs") == "apbqrs");
    assert(sol.mergeAlternately("abcd", "pq") == "apbqcd");
    return 0;
}
