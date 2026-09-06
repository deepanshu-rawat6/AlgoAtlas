#include <cassert>
#include <climits>
#include <queue>
#include <tuple>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* build(const std::vector<int>& vals) {
    if (vals.empty() || vals[0] == -1) return nullptr;
    TreeNode* root = new TreeNode(vals[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)vals.size()) {
        TreeNode* node = q.front(); q.pop();
        if (vals[i] != -1) { node->left = new TreeNode(vals[i]); q.push(node->left); }
        ++i;
        if (i < (int)vals.size() && vals[i] != -1) { node->right = new TreeNode(vals[i]); q.push(node->right); }
        ++i;
    }
    return root;
}

int maxSize;

// Returns {is_bst, size, min_val, max_val}
std::tuple<bool,int,int,int> dfs(TreeNode* node) {
    if (!node) return {true, 0, INT_MAX, INT_MIN};
    auto [lb, ls, lmin, lmax] = dfs(node->left);
    auto [rb, rs, rmin, rmax] = dfs(node->right);
    if (lb && rb && lmax < node->val && node->val < rmin) {
        int size = ls + rs + 1;
        maxSize = std::max(maxSize, size);
        return {true, size, std::min(lmin, node->val), std::max(rmax, node->val)};
    }
    return {false, 0, 0, 0};
}

int largestBSTSubtree(TreeNode* root) {
    maxSize = 0;
    dfs(root);
    return maxSize;
}

int main() {
    assert(largestBSTSubtree(build({10,5,15,1,8,-1,7})) == 3);
    assert(largestBSTSubtree(build({4,2,6,1,3,5,7})) == 7);
    assert(largestBSTSubtree(build({1})) == 1);
    return 0;
}
