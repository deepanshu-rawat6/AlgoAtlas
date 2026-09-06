#include <algorithm>
#include <cassert>
#include <map>
#include <queue>
#include <tuple>
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

std::vector<std::vector<int>> verticalTraversal(TreeNode* root) {
    if (!root) return {};
    // collect (col, row, val)
    std::vector<std::tuple<int,int,int>> nodes;
    std::queue<std::tuple<TreeNode*,int,int>> q;
    q.push({root, 0, 0});
    while (!q.empty()) {
        auto [node, col, row] = q.front(); q.pop();
        nodes.push_back({col, row, node->val});
        if (node->left)  q.push({node->left,  col-1, row+1});
        if (node->right) q.push({node->right, col+1, row+1});
    }
    std::sort(nodes.begin(), nodes.end());
    std::map<int, std::vector<int>> colMap;
    for (auto& [col, row, val] : nodes) colMap[col].push_back(val);
    std::vector<std::vector<int>> res;
    for (auto& [c, vals] : colMap) res.push_back(vals);
    return res;
}

int main() {
    assert(verticalTraversal(build({3,9,20,-1,-1,15,7})) ==
           (std::vector<std::vector<int>>{{9},{3,15},{20},{7}}));
    assert(verticalTraversal(build({1,2,3,4,5,6,7})) ==
           (std::vector<std::vector<int>>{{4},{2},{1,5,6},{3},{7}}));
    assert(verticalTraversal(build({1})) ==
           (std::vector<std::vector<int>>{{1}}));
    return 0;
}
