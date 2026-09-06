#include <cassert>
#include <vector>

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

bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
    std::vector<int> l1, l2;
    inorder(root1, l1);
    inorder(root2, l2);
    int i = 0, j = (int)l2.size() - 1;
    while (i < (int)l1.size() && j >= 0) {
        int s = l1[i] + l2[j];
        if (s == target) return true;
        else if (s < target) ++i;
        else --j;
    }
    return false;
}

int main() {
    // [2,1,4] + [1,0,3], target=5 -> true (2+3)
    TreeNode* t1 = new TreeNode(2);
    t1->left = new TreeNode(1); t1->right = new TreeNode(4);
    TreeNode* t2 = new TreeNode(1);
    t2->left = new TreeNode(0); t2->right = new TreeNode(3);
    assert(twoSumBSTs(t1, t2, 5)  == true);
    assert(twoSumBSTs(t1, t2, 10) == false);

    // Single nodes 3+4=7
    TreeNode* a = new TreeNode(3);
    TreeNode* b = new TreeNode(4);
    assert(twoSumBSTs(a, b, 7) == true);
    assert(twoSumBSTs(a, b, 8) == false);
    return 0;
}
