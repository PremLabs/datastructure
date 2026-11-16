import java.util.Arrays;

public class Sorting {
    static void bubbleSort(int[] a) {                  // O(n^2), stable, in place
        for (int i = 0; i < a.length; i++) {
            boolean swapped = false;
            for (int j = 0; j < a.length - i - 1; j++) {
                if (a[j] > a[j + 1]) { swap(a, j, j + 1); swapped = true; }
            }
            if (!swapped) break;                       // already sorted: stop early
        }
    }

    static void selectionSort(int[] a) {               // O(n^2), not stable, in place
        for (int i = 0; i < a.length - 1; i++) {
            int smallest = i;
            for (int j = i + 1; j < a.length; j++) if (a[j] < a[smallest]) smallest = j;
            swap(a, i, smallest);
        }
    }

    static void insertionSort(int[] a) {               // O(n^2) worst, O(n) if nearly sorted
        for (int i = 1; i < a.length; i++) {
            int key = a[i], j = i - 1;
            while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
            a[j + 1] = key;
        }
    }

    static void mergeSort(int[] a) {                   // O(n log n) always, stable, O(n) space
        if (a.length <= 1) return;
        int[] left = Arrays.copyOfRange(a, 0, a.length / 2);
        int[] right = Arrays.copyOfRange(a, a.length / 2, a.length);
        mergeSort(left);
        mergeSort(right);
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) a[k++] = left[i] <= right[j] ? left[i++] : right[j++];
        while (i < left.length) a[k++] = left[i++];
        while (j < right.length) a[k++] = right[j++];
    }

    static void quickSort(int[] a, int lo, int hi) {   // O(n log n) average, O(n^2) worst
        if (lo >= hi) return;
        int pivot = a[hi], i = lo;
        for (int j = lo; j < hi; j++) {                // Lomuto partition
            if (a[j] < pivot) swap(a, i++, j);
        }
        swap(a, i, hi);
        quickSort(a, lo, i - 1);
        quickSort(a, i + 1, hi);
    }

    private static void swap(int[] a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }

    public static void main(String[] args) {
        int[] data = {38, 27, 43, 3, 9, 82, 10};
        int[] a = data.clone(); bubbleSort(a);              System.out.println(Arrays.toString(a));
        a = data.clone(); selectionSort(a);                 System.out.println(Arrays.toString(a));
        a = data.clone(); insertionSort(a);                 System.out.println(Arrays.toString(a));
        a = data.clone(); mergeSort(a);                     System.out.println(Arrays.toString(a));
        a = data.clone(); quickSort(a, 0, a.length - 1);    System.out.println(Arrays.toString(a));
    }
}
