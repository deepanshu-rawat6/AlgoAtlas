// LC 106: Construct Binary Tree from Inorder and Postorder Traversal
#include <cassert>
#include <vector>
#include <unordered_map>
using namespace std;

struct TreeNode { int val; TreeNode *left, *right; TreeNode(int v):val(v),left(nullptr),right(nullptr){} };

static vector<int> post;
static unordered_map<int,int> idxMap;

static TreeNode* helper(int inL, int inR) {
    if (inL > inR) return nullptr;
    int rootVal = post.back(); post.pop_back();
    TreeNode* root = new TreeNode(rootVal);
    int mid = idxMap[rootVal];
    root->right = helper(mid + 1, inR);   // right before left
    root->left  = helper(inL, mid - 1);
    return root;
}

static TreeNode* buildTree(vector<int> inorder, vector<int> postorder) {
    idxMap.clear();
    for (int i = 0; i < (int)inorder.size(); i++) idxMap[inorder[i]] = i;
    post = postorder;
    return helper(0, (int)inorder.size() - 1);
}

int main() {
    // Test 1
    TreeNode* r1 = buildTree({9,3,15,20,7}, {9,15,7,20,3});
    assert(r1->val == 3);
    assert(r1->left->val == 9);
    assert(r1->right->val == 20);

    // Test 2: single node
    TreeNode* r2 = buildTree({-1}, {-1});
    assert(r2->val == -1 && !r2->left && !r2->right);

    // Test 3
    TreeNode* r3 = buildTree({2,1,3}, {2,3,1});
    assert(r3->val == 1 && r3->left->val == 2 && r3->right->val == 3);

    return 0;
}
