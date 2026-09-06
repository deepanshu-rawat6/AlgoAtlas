// LC 1448: Count Good Nodes in Binary Tree
#include <cassert>
#include <queue>
#include <algorithm>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

static TreeNode* build(const vector<int*>& vals) { return nullptr; } // unused

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

static int dfs(TreeNode* node, int maxSoFar) {
    if (!node) return 0;
    int good = node->val >= maxSoFar ? 1 : 0;
    int newMax = max(maxSoFar, node->val);
    return good + dfs(node->left, newMax) + dfs(node->right, newMax);
}

static int goodNodes(TreeNode* root) {
    return dfs(root, root->val);
}

int main() {
    // [3,1,4,3,null,1,5] -> 4
    const int N = INT_MIN;
    assert(goodNodes(buildV({3,1,4,3,N,1,5})) == 4);
    // [3,3,null,4,2] -> 3
    assert(goodNodes(buildV({3,3,N,4,2})) == 3);
    // [1] -> 1
    assert(goodNodes(buildV({1})) == 1);
    return 0;
}
