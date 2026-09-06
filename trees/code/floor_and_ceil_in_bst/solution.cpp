// Floor and Ceil in BST
#include <cassert>
#include <queue>
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

static int floorBST(TreeNode* root, int key) {
    int res = -1;
    while (root) {
        if      (root->val == key) return root->val;
        else if (root->val < key) { res = root->val; root = root->right; }
        else                        root = root->left;
    }
    return res;
}

static int ceilBST(TreeNode* root, int key) {
    int res = -1;
    while (root) {
        if      (root->val == key) return root->val;
        else if (root->val > key) { res = root->val; root = root->left; }
        else                        root = root->right;
    }
    return res;
}

int main() {
    // BST [8,4,12,2,6,10,14]
    TreeNode* root = buildV({8,4,12,2,6,10,14});

    assert(floorBST(root, 5) == 4);
    assert(ceilBST(root,  5) == 6);

    assert(floorBST(root, 8) == 8);
    assert(ceilBST(root,  8) == 8);

    assert(floorBST(root, 1)  == -1);
    assert(ceilBST(root,  1)  ==  2);

    assert(floorBST(root, 15) == 14);
    assert(ceilBST(root,  15) == -1);

    assert(floorBST(nullptr, 5) == -1);
    assert(ceilBST(nullptr,  5) == -1);

    return 0;
}
