// Bottom View of Binary Tree
// BFS with column tracking; last-seen value per column = bottom view.
#include <cassert>
#include <vector>
#include <queue>
#include <map>

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

std::vector<int> bottomView(TreeNode* root) {
    if (!root) return {};
    std::map<int, int> colMap;  // col -> last seen val
    std::queue<std::pair<TreeNode*, int>> bfs;
    bfs.push({root, 0});
    while (!bfs.empty()) {
        auto [node, col] = bfs.front(); bfs.pop();
        colMap[col] = node->val;  // overwrite = last seen
        if (node->left)  bfs.push({node->left,  col - 1});
        if (node->right) bfs.push({node->right, col + 1});
    }
    std::vector<int> res;
    for (auto& [col, val] : colMap) res.push_back(val);
    return res;
}

int main() {
    assert((bottomView(build({1,2,3,4,5,6,7})) == std::vector<int>{4,2,6,3,7}));
    assert((bottomView(build({1,2,3})) == std::vector<int>{2,1,3}));
    assert((bottomView(build({5})) == std::vector<int>{5}));
    return 0;
}
