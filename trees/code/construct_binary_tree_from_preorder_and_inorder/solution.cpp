// LC 105 - Construct Binary Tree from Preorder and Inorder Traversal
// Hashmap for O(1) inorder lookup; maintain preorder index.
#include <cassert>
#include <vector>
#include <unordered_map>
#include <functional>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Collect inorder for verification
void inorder(TreeNode* node, std::vector<int>& res) {
    if (!node) return;
    inorder(node->left, res);
    res.push_back(node->val);
    inorder(node->right, res);
}

TreeNode* buildTree(std::vector<int>& preorder, std::vector<int>& inorder_arr) {
    std::unordered_map<int,int> idx;
    for (int i = 0; i < (int)inorder_arr.size(); ++i) idx[inorder_arr[i]] = i;
    int pre = 0;
    std::function<TreeNode*(int,int)> helper = [&](int l, int r) -> TreeNode* {
        if (l > r) return nullptr;
        int rootVal = preorder[pre++];
        auto* node = new TreeNode(rootVal);
        int mid = idx[rootVal];
        node->left  = helper(l, mid - 1);
        node->right = helper(mid + 1, r);
        return node;
    };
    return helper(0, inorder_arr.size() - 1);
}

int main() {
    std::vector<int> pre1{3,9,20,15,7}, in1{9,3,15,20,7};
    auto* t1 = buildTree(pre1, in1);
    std::vector<int> got1; inorder(t1, got1);
    assert(got1 == in1);

    std::vector<int> pre2{-1}, in2{-1};
    auto* t2 = buildTree(pre2, in2);
    assert(t2->val == -1 && !t2->left && !t2->right);

    std::vector<int> pre3{1,2,3}, in3{2,1,3};
    auto* t3 = buildTree(pre3, in3);
    assert(t3->val == 1 && t3->left->val == 2 && t3->right->val == 3);
    return 0;
}
