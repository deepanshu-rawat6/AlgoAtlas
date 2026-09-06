#include <cassert>
#include <string>
#include <vector>
#include <algorithm>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

void dfs(TreeNode* node, const std::string& path, std::vector<std::string>& res) {
    if (!node->left && !node->right) { res.push_back(path); return; }
    if (node->left)  dfs(node->left,  path + "->" + std::to_string(node->left->val),  res);
    if (node->right) dfs(node->right, path + "->" + std::to_string(node->right->val), res);
}

std::vector<std::string> binaryTreePaths(TreeNode* root) {
    std::vector<std::string> res;
    if (root) dfs(root, std::to_string(root->val), res);
    return res;
}

int main() {
    // [1,2,3,null,5] -> ["1->2->5","1->3"]
    TreeNode* r1 = new TreeNode(1);
    r1->left = new TreeNode(2); r1->right = new TreeNode(3);
    r1->left->right = new TreeNode(5);
    auto p1 = binaryTreePaths(r1);
    std::sort(p1.begin(), p1.end());
    assert(p1 == std::vector<std::string>({"1->2->5","1->3"}));

    // [1] -> ["1"]
    assert(binaryTreePaths(new TreeNode(1)) == std::vector<std::string>({"1"}));

    // [1,2] -> ["1->2"]
    TreeNode* r3 = new TreeNode(1);
    r3->left = new TreeNode(2);
    assert(binaryTreePaths(r3) == std::vector<std::string>({"1->2"}));

    return 0;
}
