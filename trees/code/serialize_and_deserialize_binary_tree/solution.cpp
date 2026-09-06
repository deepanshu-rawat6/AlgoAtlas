#include <cassert>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

std::string serialize(TreeNode* root) {
    if (!root) return "";
    std::string out;
    std::queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* n = q.front(); q.pop();
        if (!out.empty()) out += ',';
        if (n) {
            out += std::to_string(n->val);
            q.push(n->left);
            q.push(n->right);
        } else {
            out += "null";
        }
    }
    return out;
}

TreeNode* deserialize(const std::string& data) {
    if (data.empty()) return nullptr;
    std::vector<std::string> tokens;
    std::stringstream ss(data);
    std::string tok;
    while (std::getline(ss, tok, ',')) tokens.push_back(tok);

    TreeNode* root = new TreeNode(std::stoi(tokens[0]));
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)tokens.size()) {
        TreeNode* n = q.front(); q.pop();
        if (tokens[i] != "null") { n->left  = new TreeNode(std::stoi(tokens[i])); q.push(n->left);  } i++;
        if (i < (int)tokens.size() && tokens[i] != "null") { n->right = new TreeNode(std::stoi(tokens[i])); q.push(n->right); } i++;
    }
    return root;
}

// Collect inorder for comparison
void inorder(TreeNode* n, std::vector<int>& out) {
    if (!n) return;
    inorder(n->left, out);
    out.push_back(n->val);
    inorder(n->right, out);
}

TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == -1) return nullptr;
    TreeNode* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < (int)v.size()) {
        TreeNode* n = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != -1) { n->left  = new TreeNode(v[i]); q.push(n->left);  } i++;
        if (i < (int)v.size() && v[i] != -1) { n->right = new TreeNode(v[i]); q.push(n->right); } i++;
    }
    return root;
}

int main() {
    // [1,2,3,null,null,4,5] roundtrip
    TreeNode* root = build({1, 2, 3, -1, -1, 4, 5});
    std::vector<int> before, after;
    inorder(root, before);
    TreeNode* restored = deserialize(serialize(root));
    inorder(restored, after);
    assert(before == after);

    // null roundtrip
    assert(serialize(nullptr).empty());
    assert(deserialize("") == nullptr);

    // single node [42]
    TreeNode* single = new TreeNode(42);
    TreeNode* r = deserialize(serialize(single));
    assert(r != nullptr && r->val == 42 && r->left == nullptr && r->right == nullptr);

    return 0;
}
