// LC 49: Group Anagrams
// Group strings that are anagrams of each other.
// Time: O(n * k * log k), Space: O(n * k)
#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
public:
    // Brute: O(n^2 * k) time — compare each pair
    vector<vector<string>> groupAnagrams_brute(vector<string>& strs) {
        int n = strs.size();
        vector<bool> used(n, false);
        vector<vector<string>> res;
        for (int i = 0; i < n; i++) {
            if (used[i]) continue;
            vector<string> group = {strs[i]};
            string si = strs[i]; sort(si.begin(), si.end());
            for (int j = i + 1; j < n; j++) {
                if (used[j]) continue;
                string sj = strs[j]; sort(sj.begin(), sj.end());
                if (si == sj) { group.push_back(strs[j]); used[j] = true; }
            }
            res.push_back(group);
        }
        return res;
    }

    // Optimal: sort each word as key, group in HashMap — O(n * k * log k)
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (auto& w : strs) {
            string key = w;
            sort(key.begin(), key.end());
            mp[key].push_back(w);
        }
        vector<vector<string>> res;
        for (auto& [k, v] : mp) res.push_back(v);
        return res;
    }
};

int main() {
    Solution s;
    // Sort inner groups for comparison
    auto normalize = [](vector<vector<string>> v) {
        for (auto& g : v) sort(g.begin(), g.end());
        sort(v.begin(), v.end());
        return v;
    };

    vector<string> a = {"eat", "tea", "tan", "ate", "nat", "bat"};
    auto res1 = normalize(s.groupAnagrams(a));
    vector<vector<string>> exp1 = {{"ate","eat","tea"}, {"bat"}, {"nat","tan"}};
    assert(res1 == exp1);

    vector<string> b = {""};
    auto res2 = s.groupAnagrams(b);
    assert(res2.size() == 1 && res2[0] == vector<string>{""});

    vector<string> c = {"a"};
    auto res3 = s.groupAnagrams(c);
    assert(res3.size() == 1 && res3[0] == vector<string>{"a"});

    vector<string> d = {"ab", "ba", "abc", "bca", "cab"};
    auto res4 = normalize(s.groupAnagrams(d));
    vector<vector<string>> exp4 = {{"ab","ba"}, {"abc","bca","cab"}};
    assert(res4 == exp4);

    cout << "All tests passed." << endl;
    return 0;
}
