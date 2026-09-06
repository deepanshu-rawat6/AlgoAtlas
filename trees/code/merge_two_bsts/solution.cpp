#include <cassert>
#include <vector>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

void inorder(TreeNode* node, std::vector<int>& out) {
    if (!node) return;
    inorder(node->left, out);
    out.push_back(node->val);
    inorder(node->right, out);
}

std::vector<int> mergeSorted(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> res;
    res.reserve(a.size() + b.size());
    int i = 0, j = 0;
    while (i < (int)a.size() && j < (int)b.size())
        res.push_back(a[i] <= b[j] ? a[i++] : b[j++]);
    while (i < (int)a.size()) res.push_back(a[i++]);
    while (j < (int)b.size()) res.push_back(b[j++]);
    return res;
}

TreeNode* sortedToBST(const std::vector<int>& nums, int lo, int hi) {
    if (lo > hi) return nullptr;
    int mid = lo + (hi - lo) / 2;
    TreeNode* node = new TreeNode(nums[mid]);
    node->left  = sortedToBST(nums, lo, mid - 1);
    node->right = sortedToBST(nums, mid + 1, hi);
    return node;
}

TreeNode* mergeBSTs(TreeNode* r1, TreeNode* r2) {
    std::vector<int> a, b;
    inorder(r1, a);
    inorder(r2, b);
    auto merged = mergeSorted(a, b);
    return sortedToBST(merged, 0, (int)merged.size() - 1);
}

std::vector<int> toInorder(TreeNode* root) {
    std::vector<int> res;
    inorder(root, res);
    return res;
}

int main() {
    // [3,1,5] + [4,2,6] -> inorder [1,2,3,4,5,6]
    TreeNode* r1 = new TreeNode(3);
    r1->left = new TreeNode(1); r1->right = new TreeNode(5);
    TreeNode* r2 = new TreeNode(4);
    r2->left = new TreeNode(2); r2->right = new TreeNode(6);
    assert(toInorder(mergeBSTs(r1, r2)) == std::vector<int>({1,2,3,4,5,6}));

    // [1,null,2] + null -> inorder [1,2]
    TreeNode* r3 = new TreeNode(1);
    r3->right = new TreeNode(2);
    assert(toInorder(mergeBSTs(r3, nullptr)) == std::vector<int>({1,2}));

    // null + null -> null
    assert(mergeBSTs(nullptr, nullptr) == nullptr);

    return 0;
}
