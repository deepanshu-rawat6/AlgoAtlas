// LC 427: Construct Quad Tree
#include <cassert>
#include <vector>
using namespace std;

struct Node {
    bool val, isLeaf;
    Node *topLeft, *topRight, *bottomLeft, *bottomRight;
    Node(bool v, bool leaf, Node* tl=nullptr, Node* tr=nullptr, Node* bl=nullptr, Node* br=nullptr)
        : val(v), isLeaf(leaf), topLeft(tl), topRight(tr), bottomLeft(bl), bottomRight(br) {}
};

static Node* build(const vector<vector<int>>& g, int r, int c, int sz) {
    int first = g[r][c];
    bool uniform = true;
    for (int dr = 0; dr < sz && uniform; dr++)
        for (int dc = 0; dc < sz && uniform; dc++)
            if (g[r+dr][c+dc] != first) uniform = false;
    if (uniform) return new Node(first == 1, true);
    int h = sz / 2;
    return new Node(true, false,
        build(g, r,   c,   h),
        build(g, r,   c+h, h),
        build(g, r+h, c,   h),
        build(g, r+h, c+h, h));
}

static Node* construct(vector<vector<int>>& grid) {
    return build(grid, 0, 0, (int)grid.size());
}

int main() {
    // Test 1: mixed 2x2
    vector<vector<int>> g1 = {{0,1},{1,0}};
    Node* r1 = construct(g1);
    assert(!r1->isLeaf);
    assert(r1->topLeft->isLeaf  && r1->topLeft->val  == false);
    assert(r1->topRight->isLeaf && r1->topRight->val == true);

    // Test 2: uniform 2x2
    vector<vector<int>> g2 = {{1,1},{1,1}};
    Node* r2 = construct(g2);
    assert(r2->isLeaf && r2->val == true);

    // Test 3: single cell 0
    vector<vector<int>> g3 = {{0}};
    Node* r3 = construct(g3);
    assert(r3->isLeaf && r3->val == false);

    return 0;
}
