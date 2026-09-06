#include <cassert>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

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

TreeNode* findNode(TreeNode* root, int val) {
    while (root) {
        if (root->val == val) return root;
        root = (val < root->val) ? root->left : root->right;
    }
    return nullptr;
}

// O(h) iterative — BST property narrows the split point
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    while (root) {
        if (p->val < root->val && q->val < root->val) root = root->left;
        else if (p->val > root->val && q->val > root->val) root = root->right;
        else return root;
    }
    return nullptr;
}

int main() {
    // [6,2,8,0,4,7,9,null,null,3,5]
    TreeNode* root = build({6,2,8,0,4,7,9,-1,-1,3,5});

    assert(lowestCommonAncestor(root, findNode(root,2), findNode(root,8))->val == 6);
    assert(lowestCommonAncestor(root, findNode(root,2), findNode(root,4))->val == 2);
    assert(lowestCommonAncestor(root, findNode(root,0), findNode(root,5))->val == 2);

    return 0;
}
