// LC 450: Delete Node in a BST
#include <cassert>
#include <queue>
#include <vector>
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

static void inorder(TreeNode* n, vector<int>& out) {
    if (!n) return;
    inorder(n->left, out); out.push_back(n->val); inorder(n->right, out);
}

static TreeNode* findMin(TreeNode* n) { while (n->left) n = n->left; return n; }

static TreeNode* deleteNode(TreeNode* root, int key) {
    if (!root) return nullptr;
    if (key < root->val)       root->left  = deleteNode(root->left,  key);
    else if (key > root->val)  root->right = deleteNode(root->right, key);
    else {
        if (!root->left)  return root->right;
        if (!root->right) return root->left;
        TreeNode* succ = findMin(root->right);
        root->val   = succ->val;
        root->right = deleteNode(root->right, succ->val);
    }
    return root;
}

int main() {
    const int N = INT_MIN;
    // Delete 3 from [5,3,6,2,4,null,7] -> 3 absent, others present
    TreeNode* r1 = buildV({5,3,6,2,4,N,7});
    r1 = deleteNode(r1, 3);
    vector<int> io1; inorder(r1, io1);
    assert(find(io1.begin(), io1.end(), 3) == io1.end());
    assert(find(io1.begin(), io1.end(), 2) != io1.end());

    // Delete 0 (absent) -> tree unchanged
    TreeNode* r2 = buildV({5,3,6,2,4,N,7});
    r2 = deleteNode(r2, 0);
    vector<int> io2; inorder(r2, io2);
    assert(io2 == vector<int>({2,3,4,5,6,7}));

    // nullptr -> nullptr
    assert(deleteNode(nullptr, 0) == nullptr);

    return 0;
}
