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

bool isSame(TreeNode* s, TreeNode* t) {
    if (!s && !t) return true;
    if (!s || !t || s->val != t->val) return false;
    return isSame(s->left, t->left) && isSame(s->right, t->right);
}

bool isSubtree(TreeNode* root, TreeNode* sub) {
    if (!root) return false;
    if (isSame(root, sub)) return true;
    return isSubtree(root->left, sub) || isSubtree(root->right, sub);
}

int main() {
    // root=[3,4,5,1,2], subRoot=[4,1,2] -> true
    assert(isSubtree(build({3,4,5,1,2}), build({4,1,2})));

    // root=[3,4,5,1,2,null,null,null,null,0], subRoot=[4,1,2] -> false
    assert(!isSubtree(build({3,4,5,1,2,-1,-1,-1,-1,0}), build({4,1,2})));

    // null root -> false
    assert(!isSubtree(nullptr, build({1})));

    return 0;
}
