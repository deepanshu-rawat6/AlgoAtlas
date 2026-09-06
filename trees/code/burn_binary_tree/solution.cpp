// LC 2385 - Amount of Time for Binary Tree to Be Infected
// DFS to build parent map and find start node; BFS spreads fire each second.
#include <cassert>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

TreeNode* build(const std::vector<int>& v) {
    if (v.empty() || v[0] == -1) return nullptr;
    auto* root = new TreeNode(v[0]);
    std::queue<TreeNode*> q; q.push(root);
    for (int i = 1; i < (int)v.size(); ) {
        auto* node = q.front(); q.pop();
        if (i < (int)v.size() && v[i] != -1) { node->left  = new TreeNode(v[i]); q.push(node->left);  } ++i;
        if (i < (int)v.size() && v[i] != -1) { node->right = new TreeNode(v[i]); q.push(node->right); } ++i;
    }
    return root;
}

int amountOfTime(TreeNode* root, int start) {
    std::unordered_map<TreeNode*, TreeNode*> parent;
    TreeNode* startNode = nullptr;

    std::function<void(TreeNode*, TreeNode*)> buildParent = [&](TreeNode* node, TreeNode* par) {
        if (!node) return;
        parent[node] = par;
        if (node->val == start) startNode = node;
        buildParent(node->left, node);
        buildParent(node->right, node);
    };
    buildParent(root, nullptr);

    std::unordered_set<TreeNode*> visited;
    std::queue<TreeNode*> bfs;
    bfs.push(startNode);
    visited.insert(startNode);
    int time = -1;
    while (!bfs.empty()) {
        ++time;
        int sz = bfs.size();
        while (sz--) {
            auto* node = bfs.front(); bfs.pop();
            for (TreeNode* nb : {node->left, node->right, parent[node]}) {
                if (nb && !visited.count(nb)) {
                    visited.insert(nb);
                    bfs.push(nb);
                }
            }
        }
    }
    return time;
}

int main() {
    assert(amountOfTime(build({1,5,3,-1,4,10,6,9,2}), 3) == 4);
    assert(amountOfTime(build({1}), 1) == 0);
    // [1,2]: start=2, fire: 2->1, total 1 second
    assert(amountOfTime(build({1,2}), 2) == 1);
    return 0;
}
