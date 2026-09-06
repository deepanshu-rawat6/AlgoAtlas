// LC 144 - Binary Tree Preorder Traversal
// Recursive and iterative (stack: push right then left) approaches.
#include <cassert>
#include <vector>
#include <stack>
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

// Recursive
void pre_rec(TreeNode* node, std::vector<int>& res) {
    if (!node) return;
    res.push_back(node->val);
    pre_rec(node->left, res);
    pre_rec(node->right, res);
}
std::vector<int> preorderTraversal_recursive(TreeNode* root) {
    std::vector<int> res; pre_rec(root, res); return res;
}

// Iterative
std::vector<int> preorderTraversal(TreeNode* root) {
    if (!root) return {};
    std::vector<int> res;
    std::stack<TreeNode*> st;
    st.push(root);
    while (!st.empty()) {
        auto* node = st.top(); st.pop();
        res.push_back(node->val);
        if (node->right) st.push(node->right);
        if (node->left)  st.push(node->left);
    }
    return res;
}

int main() {
    assert((preorderTraversal(build({1,-1,2,3})) == std::vector<int>{1,2,3}));
    assert((preorderTraversal(nullptr) == std::vector<int>{}));
    assert((preorderTraversal(build({1})) == std::vector<int>{1}));

    assert((preorderTraversal_recursive(build({1,-1,2,3})) == std::vector<int>{1,2,3}));
    assert((preorderTraversal_recursive(nullptr) == std::vector<int>{}));
    return 0;
}
