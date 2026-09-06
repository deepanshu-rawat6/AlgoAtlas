// LC 222: Count Complete Tree Nodes
#include <cassert>
#include <queue>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

static TreeNode* build(const vector<int>& vals) {
    if (vals.empty()) return nullptr;
    TreeNode* root = new TreeNode(vals[0]);
    queue<TreeNode*> q; q.push(root);
    for (int i = 1; i < (int)vals.size(); ) {
        TreeNode* n = q.front(); q.pop();
        if (i < (int)vals.size()) { n->left  = new TreeNode(vals[i++]); q.push(n->left); }
        if (i < (int)vals.size()) { n->right = new TreeNode(vals[i++]); q.push(n->right); }
    }
    return root;
}

// Approach 1: simple DFS — O(n)
static int countNodes(TreeNode* root) {
    if (!root) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

// Approach 2: complete-tree shortcut — O(log^2 n)
static int countNodesFast(TreeNode* root) {
    if (!root) return 0;
    int lh = 0, rh = 0;
    for (TreeNode* l = root; l; l = l->left)  lh++;
    for (TreeNode* r = root; r; r = r->right) rh++;
    if (lh == rh) return (1 << lh) - 1;
    return 1 + countNodesFast(root->left) + countNodesFast(root->right);
}

int main() {
    assert(countNodes(build({1,2,3,4,5,6})) == 6);
    assert(countNodesFast(build({1,2,3,4,5,6})) == 6);
    assert(countNodesFast(nullptr) == 0);
    assert(countNodesFast(build({1})) == 1);
    return 0;
}
