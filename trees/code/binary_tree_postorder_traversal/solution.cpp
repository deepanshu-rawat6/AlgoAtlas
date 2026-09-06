// LC 145 - Binary Tree Postorder Traversal
// Recursive and iterative (two-stack) approaches.
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
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

// Recursive
void post_rec(TreeNode* node, std::vector<int>& res) {
    if (!node) return;
    post_rec(node->left, res);
    post_rec(node->right, res);
    res.push_back(node->val);
}
std::vector<int> postorderTraversal_recursive(TreeNode* root) {
    std::vector<int> res; post_rec(root, res); return res;
}

// Iterative: push to stack2 in reverse preorder, then reverse
std::vector<int> postorderTraversal(TreeNode* root) {
    if (!root) return {};
    std::stack<TreeNode*> s1;
    std::vector<int> s2;
    s1.push(root);
    while (!s1.empty()) {
        auto* node = s1.top(); s1.pop();
        s2.push_back(node->val);
        if (node->left)  s1.push(node->left);
        if (node->right) s1.push(node->right);
    }
    std::reverse(s2.begin(), s2.end());
    return s2;
}

int main() {
    assert((postorderTraversal(build({1,-1,2,3})) == std::vector<int>{3,2,1}));
    assert((postorderTraversal(nullptr) == std::vector<int>{}));
    assert((postorderTraversal(build({1})) == std::vector<int>{1}));

    assert((postorderTraversal_recursive(build({1,-1,2,3})) == std::vector<int>{3,2,1}));
    assert((postorderTraversal_recursive(nullptr) == std::vector<int>{}));
    return 0;
}
