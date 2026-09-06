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

bool isMirror(TreeNode* l, TreeNode* r) {
    if (!l && !r) return true;
    if (!l || !r || l->val != r->val) return false;
    return isMirror(l->left, r->right) && isMirror(l->right, r->left);
}

bool isSymmetric(TreeNode* root) {
    return root && isMirror(root->left, root->right);
}

int main() {
    // [1,2,2,3,4,4,3] -> true
    assert(isSymmetric(build({1,2,2,3,4,4,3})));

    // [1,2,2,null,3,null,3] -> false
    assert(!isSymmetric(build({1,2,2,-1,3,-1,3})));

    // [1] -> true
    assert(isSymmetric(build({1})));

    return 0;
}
