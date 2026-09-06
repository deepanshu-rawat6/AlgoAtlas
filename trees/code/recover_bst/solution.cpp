#include <cassert>
#include <functional>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

void recoverTree(TreeNode* root) {
    TreeNode* first = nullptr;
    TreeNode* second = nullptr;
    TreeNode* prev = nullptr;
    // inorder traversal; find the two nodes that violate BST order
    std::function<void(TreeNode*)> dfs = [&](TreeNode* node) {
        if (!node) return;
        dfs(node->left);
        if (prev && prev->val > node->val) {
            second = node;
            if (!first) first = prev;
        }
        prev = node;
        dfs(node->right);
    };
    dfs(root);
    if (first && second) std::swap(first->val, second->val);
}

std::vector<int> toInorder(TreeNode* root) {
    std::vector<int> res;
    std::function<void(TreeNode*)> dfs = [&](TreeNode* n) {
        if (!n) return;
        dfs(n->left); res.push_back(n->val); dfs(n->right);
    };
    dfs(root);
    return res;
}

int main() {
    // [1,3,null,null,2] -> recover -> inorder [1,2,3]
    TreeNode* r1 = new TreeNode(1);
    r1->left = new TreeNode(3);
    r1->left->right = new TreeNode(2);
    recoverTree(r1);
    assert(toInorder(r1) == std::vector<int>({1,2,3}));

    // [3,1,4,null,null,2] -> recover -> inorder [1,2,3,4]
    TreeNode* r2 = new TreeNode(3);
    r2->left = new TreeNode(1); r2->right = new TreeNode(4);
    r2->right->left = new TreeNode(2);
    recoverTree(r2);
    assert(toInorder(r2) == std::vector<int>({1,2,3,4}));

    // [2,3,1] -> recover -> inorder [1,2,3]
    TreeNode* r3 = new TreeNode(2);
    r3->left = new TreeNode(3); r3->right = new TreeNode(1);
    recoverTree(r3);
    assert(toInorder(r3) == std::vector<int>({1,2,3}));

    return 0;
}
