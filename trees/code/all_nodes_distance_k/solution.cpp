// LC 863 - All Nodes Distance K in Binary Tree
// Build parent map via DFS, then BFS from target in all 3 directions.
#include <cassert>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <optional>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

// Build tree from level-order vector; -1 == null
TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == -1) return nullptr;
    auto* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    for (int i = 1; i < (int)v.size(); ) {
        auto* node = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != -1) { node->left  = new TreeNode(v[i]); q.push(node->left);  } ++i;
        if (i < (int)v.size() && v[i] != -1) { node->right = new TreeNode(v[i]); q.push(node->right); } ++i;
    }
    return root;
}

TreeNode* findNode(TreeNode* root, int val) {
    if (!root) return nullptr;
    if (root->val == val) return root;
    auto* l = findNode(root->left, val);
    return l ? l : findNode(root->right, val);
}

std::vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
    std::unordered_map<TreeNode*, TreeNode*> parent;
    // DFS to build parent map
    std::function<void(TreeNode*, TreeNode*)> buildParent = [&](TreeNode* node, TreeNode* par) {
        if (!node) return;
        parent[node] = par;
        buildParent(node->left, node);
        buildParent(node->right, node);
    };
    buildParent(root, nullptr);

    std::unordered_set<TreeNode*> visited;
    std::queue<std::pair<TreeNode*, int>> bfs;
    bfs.push({target, 0});
    visited.insert(target);
    std::vector<int> result;
    while (!bfs.empty()) {
        auto [node, dist] = bfs.front(); bfs.pop();
        if (dist == k) { result.push_back(node->val); continue; }
        for (TreeNode* nb : {node->left, node->right, parent[node]}) {
            if (nb && !visited.count(nb)) {
                visited.insert(nb);
                bfs.push({nb, dist + 1});
            }
        }
    }
    return result;
}

int main() {
    // Test 1: [3,5,1,6,2,0,8,null,null,7,4], target=5, k=2 -> [7,4,1]
    auto* root = build({3,5,1,6,2,0,8,-1,-1,7,4});
    auto res = distanceK(root, findNode(root, 5), 2);
    std::sort(res.begin(), res.end());
    assert((res == std::vector<int>{1,4,7}));

    // Test 2: k=0 -> [5]
    auto res2 = distanceK(root, findNode(root, 5), 0);
    assert((res2 == std::vector<int>{5}));

    // Test 3: single node, k=0
    auto* single = new TreeNode(42);
    auto res3 = distanceK(single, single, 0);
    assert((res3 == std::vector<int>{42}));

    return 0;
}
