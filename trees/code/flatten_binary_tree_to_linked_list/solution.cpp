// LC 114: Flatten Binary Tree to Linked List
#include <cassert>
#include <queue>
#include <vector>
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

static vector<int> toList(TreeNode* root) {
    vector<int> res;
    while (root) { assert(!root->left); res.push_back(root->val); root = root->right; }
    return res;
}

// Approach 1: reverse postorder with prev pointer — O(n)
static TreeNode* prev1 = nullptr;
static void flattenRec(TreeNode* node) {
    if (!node) return;
    flattenRec(node->right);
    flattenRec(node->left);
    node->right = prev1;
    node->left  = nullptr;
    prev1 = node;
}
static void flatten(TreeNode* root) { prev1 = nullptr; flattenRec(root); }

// Approach 2: Morris iterative — O(n) time, O(1) space
static void flattenIterative(TreeNode* root) {
    TreeNode* curr = root;
    while (curr) {
        if (curr->left) {
            TreeNode* rightmost = curr->left;
            while (rightmost->right) rightmost = rightmost->right;
            rightmost->right = curr->right;
            curr->right = curr->left;
            curr->left  = nullptr;
        }
        curr = curr->right;
    }
}

int main() {
    const int N = INT_MIN;
    // [1,2,5,3,4,null,6] -> [1,2,3,4,5,6]
    TreeNode* r1 = buildV({1,2,5,3,4,N,6});
    flatten(r1);
    assert(toList(r1) == vector<int>({1,2,3,4,5,6}));

    TreeNode* r2 = buildV({1,2,5,3,4,N,6});
    flattenIterative(r2);
    assert(toList(r2) == vector<int>({1,2,3,4,5,6}));

    // Single node
    TreeNode* r3 = buildV({1});
    flatten(r3);
    assert(toList(r3) == vector<int>({1}));

    // nullptr — no crash
    flatten(nullptr);
    flattenIterative(nullptr);

    return 0;
}
