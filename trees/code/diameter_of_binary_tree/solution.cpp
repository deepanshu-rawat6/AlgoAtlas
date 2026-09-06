// LC 543: Diameter of Binary Tree
#include <cassert>
#include <queue>
#include <algorithm>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

static TreeNode* buildV(const vector<int>& vals, int nil = INT_MIN) {
    if (vals.empty() || vals[0] == nil) return nullptr;
    TreeNode* root = new TreeNode(vals[0]);
    queue<TreeNode*> q; q.push(root);
    for (int i = 1; i < (int)vals.size(); ) {
        TreeNode* n = q.front(); q.pop();
        if (i < (int)vals.size() && vals[i] != nil) { n->left  = new TreeNode(vals[i]); q.push(n->left); } i++;
        if (i < (int)vals.size() && vals[i] != nil) { n->right = new TreeNode(vals[i]); q.push(n->right); } i++;
    }
    return root;
}

static int diameter;

static int depth(TreeNode* node) {
    if (!node) return 0;
    int l = depth(node->left), r = depth(node->right);
    diameter = max(diameter, l + r);
    return 1 + max(l, r);
}

static int diameterOfBinaryTree(TreeNode* root) {
    diameter = 0;
    depth(root);
    return diameter;
}

int main() {
    assert(diameterOfBinaryTree(buildV({1,2,3,4,5})) == 3);
    assert(diameterOfBinaryTree(buildV({1,2}))        == 1);
    assert(diameterOfBinaryTree(buildV({1}))           == 0);
    return 0;
}
