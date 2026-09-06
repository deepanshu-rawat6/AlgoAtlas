// LC 110 - Balanced Binary Tree
// DFS returning height; return -1 to signal imbalance, propagate upward.
#include <cassert>
#include <queue>
#include <vector>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == -1) return nullptr;
    auto* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q; q.push(root);
    for (int i = 1; i < (int)v.size(); ) {
        auto* node = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != -1) { node->left  = new TreeNode(v[i]); q.push(node->left);  } ++i;
        if (i < (int)v.size() && v[i] != -1) { node->right = new TreeNode(v[i]); q.push(node->right); } ++i;
    }
    return root;
}

// Brute-force O(n^2): compute height at every node
int height(TreeNode* node) {
    if (!node) return 0;
    return 1 + std::max(height(node->left), height(node->right));
}
bool isBalanced_brute(TreeNode* root) {
    if (!root) return true;
    return std::abs(height(root->left) - height(root->right)) <= 1
        && isBalanced_brute(root->left)
        && isBalanced_brute(root->right);
}

// Optimal O(n): return -1 on imbalance
int check(TreeNode* node) {
    if (!node) return 0;
    int l = check(node->left);
    if (l == -1) return -1;
    int r = check(node->right);
    if (r == -1) return -1;
    if (std::abs(l - r) > 1) return -1;
    return 1 + std::max(l, r);
}
bool isBalanced(TreeNode* root) { return check(root) != -1; }

int main() {
    assert(isBalanced(build({3,9,20,-1,-1,15,7})) == true);
    assert(isBalanced(build({1,2,2,3,3,-1,-1,4,4})) == false);
    assert(isBalanced(nullptr) == true);

    assert(isBalanced_brute(build({3,9,20,-1,-1,15,7})) == true);
    assert(isBalanced_brute(build({1,2,2,3,3,-1,-1,4,4})) == false);
    return 0;
}
