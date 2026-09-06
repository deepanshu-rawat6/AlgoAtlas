#include <cassert>
#include <map>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Build tree from level-order array (-1 = null)
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

std::vector<int> topView(TreeNode* root) {
    if (!root) return {};
    std::map<int, int> colMap; // col -> first-seen val
    std::queue<std::pair<TreeNode*, int>> q;
    q.push({root, 0});
    while (!q.empty()) {
        auto [node, col] = q.front(); q.pop();
        if (colMap.find(col) == colMap.end()) colMap[col] = node->val;
        if (node->left)  q.push({node->left,  col - 1});
        if (node->right) q.push({node->right, col + 1});
    }
    std::vector<int> res;
    for (auto& [c, val] : colMap) res.push_back(val);
    return res;
}

int main() {
    assert(topView(build({1,2,3,4,5,6,7})) == (std::vector<int>{4,2,1,3,7}));
    assert(topView(build({1,2,3}))          == (std::vector<int>{2,1,3}));
    assert(topView(build({1}))              == (std::vector<int>{1}));
    return 0;
}
