// LC 207: Course Schedule
// Cycle detection via DFS coloring: 0=unvisited, 1=visiting, 2=done.
// Time: O(V+E), Space: O(V+E)
#include <vector>
#include <cassert>
#include <iostream>
using namespace std;

class Solution {
    vector<int> color;
    vector<vector<int>> adj;

    bool hasCycle(int v) {
        color[v] = 1;
        for (int nb : adj[v]) {
            if (color[nb] == 1) return true;
            if (color[nb] == 0 && hasCycle(nb)) return true;
        }
        color[v] = 2;
        return false;
    }
public:
    // Brute: same DFS, just labelled separately
    bool canFinish_brute(int numCourses, vector<vector<int>>& prerequisites) {
        return canFinish(numCourses, prerequisites);
    }

    // Optimal DFS coloring: O(V+E)
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        adj.assign(numCourses, {});
        color.assign(numCourses, 0);
        for (auto& e : prerequisites) adj[e[1]].push_back(e[0]);
        for (int i = 0; i < numCourses; i++)
            if (color[i] == 0 && hasCycle(i)) return false;
        return true;
    }
};

int main() {
    Solution s;
    vector<vector<int>> p1 = {{1, 0}};
    assert(s.canFinish(2, p1) == true);

    vector<vector<int>> p2 = {{1, 0}, {0, 1}};
    assert(s.canFinish(2, p2) == false);

    vector<vector<int>> p3 = {};
    assert(s.canFinish(1, p3) == true);

    vector<vector<int>> p4 = {{1,0},{2,0},{3,1},{3,2}};
    assert(s.canFinish(4, p4) == true);

    vector<vector<int>> p5 = {{1,0},{2,1},{0,2}};
    assert(s.canFinish(3, p5) == false);

    cout << "All tests passed." << endl;
    return 0;
}
