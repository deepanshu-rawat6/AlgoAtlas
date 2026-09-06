#include <cassert>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == -1) return nullptr;
    TreeNode* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)v.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != -1) { node->left  = new TreeNode(v[i]); q.push(node->left); }  ++i;
        if (i < (int)v.size() && v[i] != -1) { node->right = new TreeNode(v[i]); q.push(node->right); } ++i;
    }
    return root;
}

void inorder(TreeNode* node, std::vector<int>& out) {
    if (!node) return;
    inorder(node->left, out);
    out.push_back(node->val);
    inorder(node->right, out);
}

bool findTarget(TreeNode* root, int k) {
    std::vector<int> nums;
    inorder(root, nums);
    int lo = 0, hi = (int)nums.size() - 1;
    while (lo < hi) {
        int s = nums[lo] + nums[hi];
        if (s == k) return true;
        else if (s < k) ++lo;
        else --hi;
    }
    return false;
}

int main() {
    // [5,3,6,2,4,null,7], k=9 -> true (2+7)
    assert(findTarget(build({5,3,6,2,4,-1,7}), 9)  == true);
    assert(findTarget(build({5,3,6,2,4,-1,7}), 28) == false);
    // [1,null,2], k=3 -> true (1+2)
    assert(findTarget(build({1,-1,2}), 3) == true);
    return 0;
}
