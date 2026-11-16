import java.util.HashSet;
import java.util.Set;

public class BigO {
    static int firstItem(int[] items) {            // O(1)
        return items[0];
    }

    static boolean contains(int[] items, int target) {  // O(n)
        for (int item : items) {
            if (item == target) return true;
        }
        return false;
    }

    static boolean hasDuplicate(int[] items) {     // O(n^2)
        for (int i = 0; i < items.length; i++) {
            for (int j = i + 1; j < items.length; j++) {
                if (items[i] == items[j]) return true;
            }
        }
        return false;
    }

    static boolean hasDuplicateFast(int[] items) { // O(n) time, O(n) space
        Set<Integer> seen = new HashSet<>();
        for (int item : items) {
            if (!seen.add(item)) return true;
        }
        return false;
    }

    static int halvings(int n) {                   // O(log n)
        int steps = 0;
        while (n > 1) { n /= 2; steps++; }
        return steps;
    }

    public static void main(String[] args) {
        System.out.println(halvings(1_000_000));                     // 19
        System.out.println(hasDuplicateFast(new int[]{3, 1, 4, 1})); // true
    }
}
