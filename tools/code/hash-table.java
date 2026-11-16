import java.util.ArrayList;
import java.util.List;

public class HashTable<K, V> {
    private static class Entry<K, V> {
        final K key; V value;
        Entry(K key, V value) { this.key = key; this.value = value; }
    }

    private List<List<Entry<K, V>>> buckets = newBuckets(8);
    private int size = 0;

    private static <K, V> List<List<Entry<K, V>>> newBuckets(int n) {
        List<List<Entry<K, V>>> list = new ArrayList<>();
        for (int i = 0; i < n; i++) list.add(new ArrayList<>());
        return list;
    }

    private int index(K key) {
        return Math.floorMod(key.hashCode(), buckets.size());   // floorMod: never negative
    }

    public void put(K key, V value) {                  // O(1) average
        List<Entry<K, V>> bucket = buckets.get(index(key));
        for (Entry<K, V> e : bucket) {
            if (e.key.equals(key)) { e.value = value; return; }
        }
        bucket.add(new Entry<>(key, value));
        if (++size > 0.75 * buckets.size()) resize();
    }

    public V get(K key) {                              // O(1) average
        for (Entry<K, V> e : buckets.get(index(key))) {
            if (e.key.equals(key)) return e.value;
        }
        return null;
    }

    public boolean remove(K key) {                     // O(1) average
        if (buckets.get(index(key)).removeIf(e -> e.key.equals(key))) { size--; return true; }
        return false;
    }

    private void resize() {                            // O(n): every key is rehashed
        List<List<Entry<K, V>>> old = buckets;
        buckets = newBuckets(old.size() * 2);
        size = 0;
        for (List<Entry<K, V>> bucket : old) for (Entry<K, V> e : bucket) put(e.key, e.value);
    }

    public static void main(String[] args) {
        HashTable<String, Integer> table = new HashTable<>();
        for (String word : "the quick brown fox jumps over the lazy dog the end".split(" ")) {
            Integer count = table.get(word);
            table.put(word, count == null ? 1 : count + 1);
        }
        System.out.println(table.get("the") + " " + table.get("fox") + " " + table.get("cat")); // 3 1 null
    }
}
