#include <algorithm>
#include <cassert>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == -1) return nullptr;
    TreeNode* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)v.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != -1) { node->left  = new TreeNode(v[i]); q.push(node->left); }  ++i;
        if (i < (int)v.size() && v[i] != -1) { node->right = new TreeNode(v[i]); q.push(node->right); } ++i;
    }
    return root;
}

std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root) {
    if (!root) return {};
    std::vector<std::vector<int>> res;
    std::queue<TreeNode*> q;
    q.push(root);
    bool ltr = true;
    while (!q.empty()) {
        int sz = q.size();
        std::vector<int> level;
        for (int i = 0; i < sz; ++i) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left)  q.push(node->left);
            if (node->right) q.push(node->right);
        }
        if (!ltr) std::reverse(level.begin(), level.end());
        res.push_back(level);
        ltr = !ltr;
    }
    return res;
}

int main() {
    assert(zigzagLevelOrder(build({3,9,20,-1,-1,15,7})) ==
           (std::vector<std::vector<int>>{{3},{20,9},{15,7}}));
    assert(zigzagLevelOrder(nullptr) == (std::vector<std::vector<int>>{}));
    assert(zigzagLevelOrder(build({1})) == (std::vector<std::vector<int>>{{1}}));
    return 0;
}
