import java.util.Arrays;

public class BinarySearch {
    static int binarySearch(int[] items, int target) {     // O(log n); items must be sorted
        int lo = 0, hi = items.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;                  // avoids int overflow of (lo + hi)
            if (items[mid] == target) return mid;
            if (items[mid] < target) lo = mid + 1;         // target is in the right half
            else hi = mid - 1;                             // target is in the left half
        }
        return -1;
    }

    /** First index whose value is >= target (the insertion point). */
    static int lowerBound(int[] items, int target) {
        int lo = 0, hi = items.length;                     // note: hi is one past the end
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (items[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    public static void main(String[] args) {
        int[] nums = {3, 8, 15, 15, 15, 23, 42, 57};
        System.out.println(binarySearch(nums, 23));        // 5
        System.out.println(binarySearch(nums, 9));         // -1
        System.out.println(lowerBound(nums, 15));          // 2  (first 15)
        System.out.println(Arrays.binarySearch(nums, 42)); // 6  (standard library)
    }
}
