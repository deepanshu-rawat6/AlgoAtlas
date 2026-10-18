import java.util.*;

public class Solution {
    public List<List<Integer>> permuteSwap(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        recurseSwap(nums, 0, result);
        return result;
    }

    private void recurseSwap(int[] nums, int start, List<List<Integer>> result) {
        if (start == nums.length) {
            List<Integer> perm = new ArrayList<>();
            for (int x : nums) perm.add(x);
            result.add(perm);
            return;
        }
        for (int i = start; i < nums.length; i++) {
            int tmp = nums[start]; nums[start] = nums[i]; nums[i] = tmp;
            recurseSwap(nums, start + 1, result);
            tmp = nums[start]; nums[start] = nums[i]; nums[i] = tmp;
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> remaining = new ArrayList<>();
        for (int x : nums) remaining.add(x);
        recursePick(new ArrayList<>(), remaining, result);
        return result;
    }

    private void recursePick(List<Integer> current, List<Integer> remaining, List<List<Integer>> result) {
        if (remaining.isEmpty()) {
            result.add(new ArrayList<>(current));
            return;
        }
        for (int i = 0; i < remaining.size(); i++) {
            current.add(remaining.get(i));
            List<Integer> next = new ArrayList<>(remaining);
            next.remove(i);
            recursePick(current, next, result);
            current.remove(current.size() - 1);
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<List<Integer>> r1 = sol.permuteSwap(new int[]{1, 2, 3});
        List<List<Integer>> r2 = sol.permute(new int[]{1, 2, 3});
        assert r1.size() == 6 : "test failed";
        assert r2.size() == 6 : "test failed";
        List<List<Integer>> s1 = new ArrayList<>(r1); Collections.sort(s1, Comparator.comparing(Object::toString));
        List<List<Integer>> s2 = new ArrayList<>(r2); Collections.sort(s2, Comparator.comparing(Object::toString));
        assert s1.equals(s2) : "test failed";
        assert sol.permute(new int[]{1}).equals(Arrays.asList(Arrays.asList(1))) : "test failed";
        System.out.println("All tests passed.");
    }
}
