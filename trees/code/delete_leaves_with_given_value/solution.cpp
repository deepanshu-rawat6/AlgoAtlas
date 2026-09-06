// LC 1325: Delete Leaves With a Given Value
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

static vector<int> bfsVals(TreeNode* root) {
    if (!root) return {};
    vector<int> res;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        auto n = q.front(); q.pop();
        res.push_back(n->val);
        if (n->left)  q.push(n->left);
        if (n->right) q.push(n->right);
    }
    return res;
}

static TreeNode* removeLeafNodes(TreeNode* root, int target) {
    if (!root) return nullptr;
    root->left  = removeLeafNodes(root->left,  target);
    root->right = removeLeafNodes(root->right, target);
    if (!root->left && !root->right && root->val == target) return nullptr;
    return root;
}

int main() {
    const int N = INT_MIN;
    // [1,2,3,2,null,2,4], target=2 -> BFS = [1,3,4]
    TreeNode* r1 = buildV({1,2,3,2,N,2,4});
    r1 = removeLeafNodes(r1, 2);
    assert(bfsVals(r1) == vector<int>({1,3,4}));

    // [1,3,3,3,2], target=3 -> root=1, left child still has val 3 with right=2
    TreeNode* r2 = buildV({1,3,3,3,2});
    r2 = removeLeafNodes(r2, 3);
    assert(r2->val == 1 && r2->left && r2->left->val == 3 && r2->left->right && r2->left->right->val == 2);

    // [1], target=1 -> nullptr
    TreeNode* r3 = buildV({1});
    r3 = removeLeafNodes(r3, 1);
    assert(r3 == nullptr);

    return 0;
}
