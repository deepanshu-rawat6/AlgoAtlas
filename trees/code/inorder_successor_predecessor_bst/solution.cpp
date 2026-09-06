#include <cassert>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// vals: -1 means null
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

// O(h) — BST property
TreeNode* inorderSuccessor(TreeNode* root, int pval) {
    TreeNode* succ = nullptr;
    while (root) {
        if (pval < root->val) { succ = root; root = root->left; }
        else                  { root = root->right; }
    }
    return succ;
}

TreeNode* inorderPredecessor(TreeNode* root, int pval) {
    TreeNode* pred = nullptr;
    while (root) {
        if (pval > root->val) { pred = root; root = root->right; }
        else                  { root = root->left; }
    }
    return pred;
}

int main() {
    // BST: [5,3,6,2,4,null,null,1]
    TreeNode* root = build({5,3,6,2,4,-1,-1,1});

    assert(inorderSuccessor(root, 3)->val == 4);
    assert(inorderPredecessor(root, 3)->val == 2);

    assert(inorderSuccessor(root, 6) == nullptr);
    assert(inorderPredecessor(root, 1) == nullptr);

    assert(inorderSuccessor(root, 5)->val == 6);
    assert(inorderPredecessor(root, 5)->val == 4);

    return 0;
}
