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

TreeNode* find(TreeNode* root, int val) {
    if (!root) return nullptr;
    if (root->val == val) return root;
    TreeNode* l = find(root->left, val);
    return l ? l : find(root->right, val);
}

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left  = lowestCommonAncestor(root->left,  p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}

int main() {
    // [3,5,1,6,2,0,8,null,null,7,4]
    TreeNode* root = build({3,5,1,6,2,0,8,-1,-1,7,4});

    assert(lowestCommonAncestor(root, find(root,5), find(root,1))->val == 3);
    assert(lowestCommonAncestor(root, find(root,5), find(root,4))->val == 5);
    assert(lowestCommonAncestor(root, find(root,6), find(root,2))->val == 5);

    return 0;
}
