import java.util.*;

public class Solution {
    // DFS approach: build email→account index map, DFS to collect connected emails
    public List<List<String>> accountsMergeDfs(List<List<String>> accounts) {
        Map<String, List<Integer>> emailToIdx = new HashMap<>();
        for (int i = 0; i < accounts.size(); i++)
            for (int j = 1; j < accounts.get(i).size(); j++)
                emailToIdx.computeIfAbsent(accounts.get(i).get(j), k -> new ArrayList<>()).add(i);

        Set<Integer> visited = new HashSet<>();
        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < accounts.size(); i++) {
            if (visited.contains(i)) continue;
            Set<String> emails = new TreeSet<>();
            dfs(i, accounts, emailToIdx, visited, emails);
            List<String> merged = new ArrayList<>();
            merged.add(accounts.get(i).get(0));
            merged.addAll(emails);
            result.add(merged);
        }
        return result;
    }

    private void dfs(int idx, List<List<String>> accounts,
                     Map<String, List<Integer>> emailToIdx,
                     Set<Integer> visited, Set<String> emails) {
        if (visited.contains(idx)) return;
        visited.add(idx);
        for (int j = 1; j < accounts.get(idx).size(); j++) {
            String email = accounts.get(idx).get(j);
            emails.add(email);
            for (int neighbor : emailToIdx.get(email))
                dfs(neighbor, accounts, emailToIdx, visited, emails);
        }
    }

    // Union-Find approach
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, String> parent = new HashMap<>();
        Map<String, String> emailToName = new HashMap<>();

        for (List<String> account : accounts) {
            String name = account.get(0);
            String first = account.get(1);
            for (int j = 1; j < account.size(); j++) {
                String email = account.get(j);
                parent.putIfAbsent(email, email);
                emailToName.put(email, name);
                union(parent, first, email);
            }
        }

        Map<String, TreeSet<String>> groups = new HashMap<>();
        for (String email : parent.keySet()) {
            String root = find(parent, email);
            groups.computeIfAbsent(root, k -> new TreeSet<>()).add(email);
        }

        List<List<String>> result = new ArrayList<>();
        for (Map.Entry<String, TreeSet<String>> e : groups.entrySet()) {
            List<String> merged = new ArrayList<>();
            merged.add(emailToName.get(e.getKey()));
            merged.addAll(e.getValue());
            result.add(merged);
        }
        return result;
    }

    private String find(Map<String, String> parent, String x) {
        if (!parent.get(x).equals(x))
            parent.put(x, find(parent, parent.get(x)));
        return parent.get(x);
    }

    private void union(Map<String, String> parent, String x, String y) {
        String px = find(parent, x), py = find(parent, y);
        if (!px.equals(py)) parent.put(py, px);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<String>> acc1 = Arrays.asList(
            Arrays.asList("John","johnsmith@mail.com","john_newyork@mail.com"),
            Arrays.asList("John","johnsmith@mail.com","john00@mail.com"),
            Arrays.asList("Mary","mary@mail.com"),
            Arrays.asList("John","johnnybravo@mail.com")
        );
        assert s.accountsMerge(acc1).size() == 3 : "test 1";

        List<List<String>> acc2 = Arrays.asList(
            Arrays.asList("John","j1@","j2@"),
            Arrays.asList("John","j1@","j3@")
        );
        List<List<String>> res2 = s.accountsMerge(acc2);
        assert res2.size() == 1 : "test 2";
        assert new TreeSet<>(res2.get(0).subList(1, res2.get(0).size())).equals(new TreeSet<>(Arrays.asList("j1@","j2@","j3@"))) : "test 3";

        List<List<String>> res3 = s.accountsMergeDfs(acc2);
        assert res3.size() == 1 : "test 4";

        System.out.println("All tests passed.");
    }
}
