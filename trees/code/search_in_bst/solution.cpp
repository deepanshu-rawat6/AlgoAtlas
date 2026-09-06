#include <cassert>
#include <queue>
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
        TreeNode* n = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != -1) { n->left  = new TreeNode(v[i]); q.push(n->left);  } i++;
        if (i < (int)v.size() && v[i] != -1) { n->right = new TreeNode(v[i]); q.push(n->right); } i++;
    }
    return root;
}

TreeNode* searchBST(TreeNode* root, int val) {
    while (root) {
        if (root->val == val) return root;
        root = (val < root->val) ? root->left : root->right;
    }
    return nullptr;
}

int main() {
    TreeNode* root = build({4, 2, 7, 1, 3});

    // val=2 -> subtree rooted at 2
    assert(searchBST(root, 2) != nullptr && searchBST(root, 2)->val == 2);

    // val=5 -> null
    assert(searchBST(root, 5) == nullptr);

    // val=4 -> root itself
    assert(searchBST(root, 4) == root);

    return 0;
}
