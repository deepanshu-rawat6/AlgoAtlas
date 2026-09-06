// Boundary Traversal of Binary Tree
// root + left_boundary(excl leaves) + leaves + right_boundary_reversed(excl leaves)
#include <cassert>
#include <vector>
#include <queue>
#include <functional>

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

bool isLeaf(TreeNode* n) { return !n->left && !n->right; }

// Left boundary top-down (excluding leaf)
void leftBoundary(TreeNode* node, std::vector<int>& res) {
    while (node) {
        if (!isLeaf(node)) res.push_back(node->val);
        node = node->left ? node->left : node->right;
    }
}

// All leaves left-to-right
void leaves(TreeNode* node, std::vector<int>& res) {
    if (!node) return;
    if (isLeaf(node)) { res.push_back(node->val); return; }
    leaves(node->left, res);
    leaves(node->right, res);
}

// Right boundary bottom-up (excluding leaf)
void rightBoundary(TreeNode* node, std::vector<int>& res) {
    std::vector<int> tmp;
    while (node) {
        if (!isLeaf(node)) tmp.push_back(node->val);
        node = node->right ? node->right : node->left;
    }
    for (int i = tmp.size() - 1; i >= 0; --i) res.push_back(tmp[i]);
}

std::vector<int> boundaryOfBinaryTree(TreeNode* root) {
    if (!root) return {};
    std::vector<int> res;
    res.push_back(root->val);
    if (!isLeaf(root)) {
        leftBoundary(root->left, res);
        leaves(root->left, res);
        leaves(root->right, res);
        rightBoundary(root->right, res);
    }
    return res;
}

int main() {
    assert((boundaryOfBinaryTree(build({1,2,3,4,5,6,7})) == std::vector<int>{1,2,4,5,6,7,3}));
    assert((boundaryOfBinaryTree(build({1})) == std::vector<int>{1}));
    // [1,2,null,3,null,4]: left boundary 2,3 (non-leaves); leaf 4; right boundary none
    assert((boundaryOfBinaryTree(build({1,2,-1,3,-1,4})) == std::vector<int>{1,2,3,4}));
    return 0;
}
