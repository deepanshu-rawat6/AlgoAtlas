#include <cassert>
#include <queue>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Build from level-order array (-1 = null)
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

bool isSameTree(TreeNode* p, TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q || p->val != q->val) return false;
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

int main() {
    // [1,2,3] vs [1,2,3] -> true
    assert(isSameTree(build({1,2,3}), build({1,2,3})));

    // [1,2] vs [1,null,2] -> false
    assert(!isSameTree(build({1,2,-1}), build({1,-1,2})));

    // [1,2,1] vs [1,1,2] -> false
    assert(!isSameTree(build({1,2,1}), build({1,1,2})));

    // null vs null -> true
    assert(isSameTree(nullptr, nullptr));

    return 0;
}
