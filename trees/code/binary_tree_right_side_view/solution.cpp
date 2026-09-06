// LC 199 - Binary Tree Right Side View
// BFS level-order; collect the last node of each level.
#include <cassert>
#include <vector>
#include <queue>

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

std::vector<int> rightSideView(TreeNode* root) {
    if (!root) return {};
    std::vector<int> res;
    std::queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = q.size();
        for (int i = 0; i < sz; ++i) {
            auto* node = q.front(); q.pop();
            if (i == sz - 1) res.push_back(node->val);
            if (node->left)  q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
    return res;
}

int main() {
    assert((rightSideView(build({1,2,3,-1,5,-1,4})) == std::vector<int>{1,3,4}));
    assert((rightSideView(build({1,-1,3})) == std::vector<int>{1,3}));
    assert((rightSideView(nullptr) == std::vector<int>{}));
    return 0;
}
