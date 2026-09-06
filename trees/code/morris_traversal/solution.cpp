#include <cassert>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

std::vector<int> morrisInorder(TreeNode* root) {
    std::vector<int> res;
    TreeNode* curr = root;
    while (curr) {
        if (!curr->left) {
            res.push_back(curr->val);
            curr = curr->right;
        } else {
            // find inorder predecessor
            TreeNode* pred = curr->left;
            while (pred->right && pred->right != curr)
                pred = pred->right;
            if (!pred->right) {
                pred->right = curr; // thread
                curr = curr->left;
            } else {
                pred->right = nullptr; // unthread
                res.push_back(curr->val);
                curr = curr->right;
            }
        }
    }
    return res;
}

std::vector<int> morrisPreorder(TreeNode* root) {
    std::vector<int> res;
    TreeNode* curr = root;
    while (curr) {
        if (!curr->left) {
            res.push_back(curr->val);
            curr = curr->right;
        } else {
            TreeNode* pred = curr->left;
            while (pred->right && pred->right != curr)
                pred = pred->right;
            if (!pred->right) {
                res.push_back(curr->val); // record before going left
                pred->right = curr;
                curr = curr->left;
            } else {
                pred->right = nullptr;
                curr = curr->right;
            }
        }
    }
    return res;
}

int main() {
    // [1,2,3,4,5]: inorder=[4,2,5,1,3], preorder=[1,2,4,5,3]
    TreeNode* r = new TreeNode(1);
    r->left = new TreeNode(2); r->right = new TreeNode(3);
    r->left->left = new TreeNode(4); r->left->right = new TreeNode(5);
    assert(morrisInorder(r)  == std::vector<int>({4,2,5,1,3}));
    assert(morrisPreorder(r) == std::vector<int>({1,2,4,5,3}));

    // single node
    TreeNode* s = new TreeNode(1);
    assert(morrisInorder(s)  == std::vector<int>({1}));
    assert(morrisPreorder(s) == std::vector<int>({1}));

    // right-skewed [1,null,2,null,3]: inorder=[1,2,3], preorder=[1,2,3]
    TreeNode* rs = new TreeNode(1);
    rs->right = new TreeNode(2);
    rs->right->right = new TreeNode(3);
    assert(morrisInorder(rs)  == std::vector<int>({1,2,3}));
    assert(morrisPreorder(rs) == std::vector<int>({1,2,3}));

    return 0;
}
