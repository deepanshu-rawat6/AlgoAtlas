#include <cassert>
#include <queue>
#include <stack>
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

// Iterative inorder — O(h+k) time, O(h) space
int kthSmallest(TreeNode* root, int k) {
    std::stack<TreeNode*> st;
    int count = 0;
    while (root || !st.empty()) {
        while (root) { st.push(root); root = root->left; }
        root = st.top(); st.pop();
        if (++count == k) return root->val;
        root = root->right;
    }
    return -1;
}

int main() {
    assert(kthSmallest(build({3,1,4,-1,2}), 1) == 1);
    assert(kthSmallest(build({5,3,6,2,4,-1,-1,1}), 3) == 3);
    assert(kthSmallest(build({5,3,6,2,4,-1,-1,1}), 1) == 1);
    return 0;
}
