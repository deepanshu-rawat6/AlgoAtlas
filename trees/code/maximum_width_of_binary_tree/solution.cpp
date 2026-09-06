#include <cassert>
#include <queue>
#include <vector>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Build tree from level-order vector (0 = null sentinel)
TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == 0) return nullptr;
    TreeNode* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)v.size()) {
        TreeNode* node = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != 0) { node->left = new TreeNode(v[i]); q.push(node->left); }
        i++;
        if (i < (int)v.size() && v[i] != 0) { node->right = new TreeNode(v[i]); q.push(node->right); }
        i++;
    }
    return root;
}

int widthOfBinaryTree(TreeNode* root) {
    if (!root) return 0;
    int maxW = 0;
    // queue of (node, index); use long long to hold large indices before normalization
    std::queue<std::pair<TreeNode*, long long>> q;
    q.push({root, 0});
    while (!q.empty()) {
        int sz = q.size();
        long long first = q.front().second;
        long long last = first;
        for (int i = 0; i < sz; i++) {
            auto [node, idx] = q.front(); q.pop();
            idx -= first; // normalize to prevent overflow
            last = idx;
            if (node->left)  q.push({node->left,  2 * idx});
            if (node->right) q.push({node->right, 2 * idx + 1});
        }
        maxW = std::max(maxW, (int)(last + 1));
    }
    return maxW;
}

int main() {
    // [1,3,2,5,3,null,9] -> 4
    // Using 0 as null sentinel in build helper
    // Build manually for clarity
    TreeNode* r1 = new TreeNode(1);
    r1->left = new TreeNode(3); r1->right = new TreeNode(2);
    r1->left->left = new TreeNode(5); r1->left->right = new TreeNode(3);
    r1->right->right = new TreeNode(9);
    assert(widthOfBinaryTree(r1) == 4);

    // [1] -> 1
    assert(widthOfBinaryTree(new TreeNode(1)) == 1);

    // null -> 0
    assert(widthOfBinaryTree(nullptr) == 0);

    // Deeper skewed: width at level with 7 wide
    // [1,3,2,5,null,null,9,6,null,7]
    TreeNode* r3 = new TreeNode(1);
    r3->left = new TreeNode(3); r3->right = new TreeNode(2);
    r3->left->left = new TreeNode(5);
    r3->right->right = new TreeNode(9);
    r3->left->left->left = new TreeNode(6);
    r3->right->right->left = new TreeNode(7);
    assert(widthOfBinaryTree(r3) == 7);

    return 0;
}
