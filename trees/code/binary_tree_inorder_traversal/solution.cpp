// LC 94 - Binary Tree Inorder Traversal
// Recursive and iterative (stack) approaches.
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
void inorder_rec(TreeNode* node, std::vector<int>& res) {
    if (!node) return;
    inorder_rec(node->left, res);
    res.push_back(node->val);
    inorder_rec(node->right, res);
}
std::vector<int> inorderTraversal_recursive(TreeNode* root) {
    std::vector<int> res;
    inorder_rec(root, res);
    return res;
}

// Iterative
std::vector<int> inorderTraversal(TreeNode* root) {
    std::vector<int> res;
    std::stack<TreeNode*> st;
    TreeNode* curr = root;
    while (curr || !st.empty()) {
        while (curr) { st.push(curr); curr = curr->left; }
        curr = st.top(); st.pop();
        res.push_back(curr->val);
        curr = curr->right;
    }
    return res;
}

int main() {
    assert((inorderTraversal(build({1,-1,2,3})) == std::vector<int>{1,3,2}));
    assert((inorderTraversal(nullptr) == std::vector<int>{}));
    assert((inorderTraversal(build({1})) == std::vector<int>{1}));

    assert((inorderTraversal_recursive(build({1,-1,2,3})) == std::vector<int>{1,3,2}));
    assert((inorderTraversal_recursive(nullptr) == std::vector<int>{}));
    return 0;
}
