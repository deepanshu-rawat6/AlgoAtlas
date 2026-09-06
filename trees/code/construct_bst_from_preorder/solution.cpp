// LC 1008: Construct BST from Preorder Traversal
#include <cassert>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

static void inorder(TreeNode* n, vector<int>& out) {
    if (!n) return;
    inorder(n->left, out); out.push_back(n->val); inorder(n->right, out);
}

// Approach 1: recursive with upper bound — O(n)
static int idx;
static TreeNode* buildRec(const vector<int>& pre, int upper) {
    if (idx == (int)pre.size() || pre[idx] > upper) return nullptr;
    TreeNode* node = new TreeNode(pre[idx++]);
    node->left  = buildRec(pre, node->val);
    node->right = buildRec(pre, upper);
    return node;
}
static TreeNode* bstFromPreorderRec(const vector<int>& pre) {
    idx = 0;
    return buildRec(pre, INT_MAX);
}

// Approach 2: stack-based — O(n)
static TreeNode* bstFromPreorder(const vector<int>& pre) {
    if (pre.empty()) return nullptr;
    TreeNode* root = new TreeNode(pre[0]);
    stack<TreeNode*> st;
    st.push(root);
    for (int i = 1; i < (int)pre.size(); i++) {
        TreeNode* node = new TreeNode(pre[i]);
        if (pre[i] < st.top()->val) {
            st.top()->left = node;
        } else {
            TreeNode* parent = st.top();
            while (!st.empty() && st.top()->val < pre[i]) { parent = st.top(); st.pop(); }
            parent->right = node;
        }
        st.push(node);
    }
    return root;
}

int main() {
    // Test 1: standard case
    vector<int> pre1 = {8,5,1,7,10,12};
    vector<int> got1, exp1 = {1,5,7,8,10,12};
    inorder(bstFromPreorder(pre1), got1);
    assert(got1 == exp1);
    got1.clear();
    inorder(bstFromPreorderRec(pre1), got1);
    assert(got1 == exp1);

    // Test 2: single element
    TreeNode* t2 = bstFromPreorder({1});
    assert(t2->val == 1 && !t2->left && !t2->right);

    // Test 3: descending (left-skewed)
    vector<int> pre3 = {4,3,2,1};
    vector<int> got3;
    inorder(bstFromPreorder(pre3), got3);
    assert(got3 == vector<int>({1,2,3,4}));

    return 0;
}
