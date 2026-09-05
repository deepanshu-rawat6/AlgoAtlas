// LC 102: Binary Tree Level Order Traversal
// BFS with a queue, collect each level into a separate list.
// Time: O(n), Space: O(n)
#include <vector>
#include <queue>
#include <cassert>
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    // Only one natural approach: BFS level by level
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> res;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            vector<int> level;
            while (sz--) {
                TreeNode* n = q.front(); q.pop();
                level.push_back(n->val);
                if (n->left) q.push(n->left);
                if (n->right) q.push(n->right);
            }
            res.push_back(level);
        }
        return res;
    }
};

TreeNode* build(vector<int> vals) {
    if (vals.empty() || vals[0] == -1) return nullptr;
    TreeNode* root = new TreeNode(vals[0]);
    queue<TreeNode*> q; q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)vals.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < (int)vals.size() && vals[i] != -1) { node->left = new TreeNode(vals[i]); q.push(node->left); } i++;
        if (i < (int)vals.size() && vals[i] != -1) { node->right = new TreeNode(vals[i]); q.push(node->right); } i++;
    }
    return root;
}

int main() {
    Solution s;
    assert((s.levelOrder(build({3,9,20,-1,-1,15,7})) == vector<vector<int>>{{3},{9,20},{15,7}}));
    assert((s.levelOrder(build({1})) == vector<vector<int>>{{1}}));
    assert(s.levelOrder(nullptr).empty());
    assert((s.levelOrder(build({1,2,3,4,5})) == vector<vector<int>>{{1},{2,3},{4,5}}));
    cout << "All tests passed." << endl;
    return 0;
}
