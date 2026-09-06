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

bool contains(TreeNode* root, int val) {
    while (root) {
        if (root->val == val) return true;
        root = (val < root->val) ? root->left : root->right;
    }
    return false;
}

TreeNode* insertIntoBST(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);
    if (val < root->val) root->left  = insertIntoBST(root->left,  val);
    else                 root->right = insertIntoBST(root->right, val);
    return root;
}

int main() {
    TreeNode* r1 = build({4,2,7,1,3});
    insertIntoBST(r1, 5);
    assert(contains(r1, 5));

    assert(insertIntoBST(nullptr, 42)->val == 42);

    TreeNode* r2 = build({40,20,60,10,30,50,70});
    insertIntoBST(r2, 25);
    assert(contains(r2, 25));

    return 0;
}
