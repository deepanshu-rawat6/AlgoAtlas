// LC 337: House Robber III
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

// Returns {rob_this, skip_this}
static pair<int,int> dfs(TreeNode* node) {
    if (!node) return {0, 0};
    auto [lr, ls] = dfs(node->left);
    auto [rr, rs] = dfs(node->right);
    int rob_this  = node->val + ls + rs;
    int skip_this = max(lr, ls) + max(rr, rs);
    return {rob_this, skip_this};
}

static int rob(TreeNode* root) {
    auto [r, s] = dfs(root);
    return max(r, s);
}

int main() {
    const int N = INT_MIN;
    assert(rob(buildV({3,2,3,N,3,N,1})) == 7);
    assert(rob(buildV({3,4,5,1,3,N,1})) == 9);
    assert(rob(buildV({1}))             == 1);
    return 0;
}
