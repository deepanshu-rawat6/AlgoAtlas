// LC 104: Maximum Depth of Binary Tree
// Recursive DFS: 1 + max(left depth, right depth).
// Time: O(n), Space: O(h) recursion stack
#include <vector>
#include <queue>
#include <algorithm>
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
    // Iterative BFS (level count)
    int maxDepth_iter(TreeNode* root) {
        if (!root) return 0;
        int depth = 0;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            depth++;
            while (sz--) {
                TreeNode* n = q.front(); q.pop();
                if (n->left) q.push(n->left);
                if (n->right) q.push(n->right);
            }
        }
        return depth;
    }

    // Optimal recursive DFS: O(n)
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
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
    assert(s.maxDepth(build({3, 9, 20, -1, -1, 15, 7})) == 3);
    assert(s.maxDepth(build({1, -1, 2})) == 2);
    assert(s.maxDepth(nullptr) == 0);
    assert(s.maxDepth(build({1})) == 1);
    assert(s.maxDepth(build({1, 2, 3, 4, 5})) == 3);
    cout << "All tests passed." << endl;
    return 0;
}
