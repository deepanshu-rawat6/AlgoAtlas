// LC 124 - Binary Tree Maximum Path Sum
// DFS: at each node update global max with left_gain + node + right_gain;
// return node + max single branch gain upward.
#include <cassert>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == INT_MIN) return nullptr;
    auto* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q; q.push(root);
    for (int i = 1; i < (int)v.size(); ) {
        auto* node = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != INT_MIN) { node->left  = new TreeNode(v[i]); q.push(node->left);  } ++i;
        if (i < (int)v.size() && v[i] != INT_MIN) { node->right = new TreeNode(v[i]); q.push(node->right); } ++i;
    }
    return root;
}

int maxSum;
int dfs(TreeNode* node) {
    if (!node) return 0;
    int l = std::max(0, dfs(node->left));
    int r = std::max(0, dfs(node->right));
    maxSum = std::max(maxSum, node->val + l + r);
    return node->val + std::max(l, r);
}

int maxPathSum(TreeNode* root) {
    maxSum = INT_MIN;
    dfs(root);
    return maxSum;
}

int main() {
    assert(maxPathSum(build({1,2,3})) == 6);
    assert(maxPathSum(build({-10,9,20,INT_MIN,INT_MIN,15,7})) == 42);
    assert(maxPathSum(build({-3})) == -3);
    return 0;
}
