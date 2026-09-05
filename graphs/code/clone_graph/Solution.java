// LC 133: Clone Graph
// DFS with a HashMap<Node, Node> to track cloned nodes.
// Time: O(V+E), Space: O(V)
import java.util.*;

class Node {
    int val;
    List<Node> neighbors;
    Node(int v) { val = v; neighbors = new ArrayList<>(); }
}

public class Solution {
    private Map<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;
        if (visited.containsKey(node)) return visited.get(node);
        Node clone = new Node(node.val);
        visited.put(node, clone);
        for (Node nb : node.neighbors)
            clone.neighbors.add(cloneGraph(nb));
        return clone;
    }

    static Node buildExample() {
        List<Node> nodes = new ArrayList<>();
        for (int i = 1; i <= 4; i++) nodes.add(new Node(i));
        nodes.get(0).neighbors = Arrays.asList(nodes.get(1), nodes.get(3));
        nodes.get(1).neighbors = Arrays.asList(nodes.get(0), nodes.get(2));
        nodes.get(2).neighbors = Arrays.asList(nodes.get(1), nodes.get(3));
        nodes.get(3).neighbors = Arrays.asList(nodes.get(2), nodes.get(0));
        return nodes.get(0);
    }

    static List<Integer> bfsVals(Node root) {
        if (root == null) return new ArrayList<>();
        Set<Node> seen = new HashSet<>();
        Queue<Node> q = new LinkedList<>();
        q.add(root); seen.add(root);
        List<Integer> vals = new ArrayList<>();
        while (!q.isEmpty()) {
            Node n = q.poll();
            vals.add(n.val);
            for (Node nb : n.neighbors)
                if (seen.add(nb)) q.add(nb);
        }
        Collections.sort(vals);
        return vals;
    }

    public static void main(String[] args) {
        // Test 1: 4-node cycle
        Node orig = buildExample();
        Solution s = new Solution();
        Node clone = s.cloneGraph(orig);
        assert clone != orig : "Test 1a failed";
        assert clone.val == orig.val : "Test 1b failed";
        assert bfsVals(orig).equals(bfsVals(clone)) : "Test 1c failed";

        // Test 2: null
        Solution s2 = new Solution();
        assert s2.cloneGraph(null) == null : "Test 2 failed";

        // Test 3: single node
        Node single = new Node(1);
        Solution s3 = new Solution();
        Node sc = s3.cloneGraph(single);
        assert sc != single && sc.val == 1 && sc.neighbors.isEmpty() : "Test 3 failed";

        System.out.println("All tests passed.");
    }
}
