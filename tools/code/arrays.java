import java.util.Arrays;

public class DynamicArray {
    private int[] data = new int[2];
    private int size = 0;

    public int size() { return size; }

    public int get(int index) {                    // O(1)
        if (index < 0 || index >= size) throw new IndexOutOfBoundsException();
        return data[index];
    }

    public void append(int value) {                // O(1) amortised
        if (size == data.length) resize(data.length * 2);
        data[size++] = value;
    }

    public void insert(int index, int value) {     // O(n): shifts the tail right
        if (index < 0 || index > size) throw new IndexOutOfBoundsException();
        if (size == data.length) resize(data.length * 2);
        for (int i = size; i > index; i--) data[i] = data[i - 1];
        data[index] = value;
        size++;
    }

    public int removeAt(int index) {               // O(n): shifts the tail left
        int value = get(index);
        for (int i = index; i < size - 1; i++) data[i] = data[i + 1];
        size--;
        return value;
    }

    private void resize(int capacity) {            // O(n) copy, but rare
        data = Arrays.copyOf(data, capacity);
    }

    public static void main(String[] args) {
        DynamicArray arr = new DynamicArray();
        arr.append(12); arr.append(45); arr.append(7);
        arr.insert(1, 30);                         // 12, 30, 45, 7
        arr.removeAt(0);                           // 30, 45, 7
        for (int i = 0; i < arr.size(); i++) System.out.print(arr.get(i) + " ");
    }
}
