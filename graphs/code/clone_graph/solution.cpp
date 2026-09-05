// LC 133: Clone Graph
// DFS with an unordered_map<Node*, Node*> to track cloned nodes.
// Time: O(V+E), Space: O(V)
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <algorithm>
#include <cassert>
#include <iostream>
using namespace std;

struct Node {
    int val;
    vector<Node*> neighbors;
    Node(int v) : val(v) {}
};

class Solution {
    unordered_map<Node*, Node*> visited;
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        if (visited.count(node)) return visited[node];
        Node* clone = new Node(node->val);
        visited[node] = clone;
        for (Node* nb : node->neighbors)
            clone->neighbors.push_back(cloneGraph(nb));
        return clone;
    }
};

// Build a simple graph: nodes 1-4 with adjacency list
// 1--2, 2--3, 3--4, 4--1 (the LC example)
Node* buildExample() {
    vector<Node*> nodes;
    for (int i = 1; i <= 4; i++) nodes.push_back(new Node(i));
    nodes[0]->neighbors = {nodes[1], nodes[3]};
    nodes[1]->neighbors = {nodes[0], nodes[2]};
    nodes[2]->neighbors = {nodes[1], nodes[3]};
    nodes[3]->neighbors = {nodes[2], nodes[0]};
    return nodes[0];
}

// BFS collect all node vals to verify clone is deep
vector<int> bfsVals(Node* root) {
    if (!root) return {};
    unordered_set<Node*> seen;
    queue<Node*> q;
    q.push(root);
    seen.insert(root);
    vector<int> vals;
    while (!q.empty()) {
        Node* n = q.front(); q.pop();
        vals.push_back(n->val);
        for (Node* nb : n->neighbors)
            if (!seen.count(nb)) { seen.insert(nb); q.push(nb); }
    }
    sort(vals.begin(), vals.end());
    return vals;
}

int main() {
    Solution s;
    // Test 1: 4-node cycle
    Node* orig = buildExample();
    Node* clone = s.cloneGraph(orig);
    assert(clone != orig);
    assert(clone->val == orig->val);
    auto ov = bfsVals(orig), cv = bfsVals(clone);
    assert(ov == cv);

    // Test 2: null
    assert(s.cloneGraph(nullptr) == nullptr);

    // Test 3: single node, no neighbors
    Node* single = new Node(1);
    Solution s2;
    Node* sc = s2.cloneGraph(single);
    assert(sc != single && sc->val == 1 && sc->neighbors.empty());

    cout << "All tests passed." << endl;
    return 0;
}
