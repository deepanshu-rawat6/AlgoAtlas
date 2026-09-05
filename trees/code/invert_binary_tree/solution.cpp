// LC 226: Invert Binary Tree
// Swap left and right children recursively.
// Time: O(n), Space: O(h) recursion stack
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
    // Iterative BFS (brute in spirit — same complexity, different traversal)
    TreeNode* invertTree_iter(TreeNode* root) {
        if (!root) return nullptr;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front(); q.pop();
            swap(node->left, node->right);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return root;
    }

    // Optimal recursive DFS: O(n)
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};

// Helper: build tree from level-order vector (-1 = null)
TreeNode* build(vector<int> vals) {
    if (vals.empty() || vals[0] == -1) return nullptr;
    TreeNode* root = new TreeNode(vals[0]);
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)vals.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < (int)vals.size() && vals[i] != -1) {
            node->left = new TreeNode(vals[i]); q.push(node->left);
        }
        i++;
        if (i < (int)vals.size() && vals[i] != -1) {
            node->right = new TreeNode(vals[i]); q.push(node->right);
        }
        i++;
    }
    return root;
}

vector<int> levelOrder(TreeNode* root) {
    if (!root) return {};
    vector<int> res;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        res.push_back(n->val);
        if (n->left) q.push(n->left);
        if (n->right) q.push(n->right);
    }
    return res;
}

int main() {
    Solution s;
    // [4,2,7,1,3,6,9] inverted -> [4,7,2,9,6,3,1]
    assert((levelOrder(s.invertTree(build({4,2,7,1,3,6,9}))) == vector<int>{4,7,2,9,6,3,1}));
    // [2,1,3] inverted -> [2,3,1]
    assert((levelOrder(s.invertTree(build({2,1,3}))) == vector<int>{2,3,1}));
    // empty
    assert(s.invertTree(nullptr) == nullptr);
    // single node
    assert((levelOrder(s.invertTree(build({1}))) == vector<int>{1}));
    cout << "All tests passed." << endl;
    return 0;
}
