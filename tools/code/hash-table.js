// In real code use Map. This class shows how one works inside.
class HashTable {
  #buckets = Array.from({ length: 8 }, () => []);
  #size = 0;

  #hash(key) {                             // simple string hash
    let h = 0;
    for (const ch of String(key)) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
    return h % this.#buckets.length;
  }

  put(key, value) {                        // O(1) average
    const bucket = this.#buckets[this.#hash(key)];
    const pair = bucket.find(p => p[0] === key);
    if (pair) { pair[1] = value; return; } // key exists: overwrite
    bucket.push([key, value]);
    if (++this.#size > 0.75 * this.#buckets.length) this.#resize();
  }

  get(key) {                               // O(1) average
    const pair = this.#buckets[this.#hash(key)].find(p => p[0] === key);
    return pair ? pair[1] : undefined;
  }

  remove(key) {                            // O(1) average
    const bucket = this.#buckets[this.#hash(key)];
    const i = bucket.findIndex(p => p[0] === key);
    if (i < 0) return false;
    bucket.splice(i, 1);
    this.#size--;
    return true;
  }

  #resize() {                              // O(n): every key is rehashed
    const old = this.#buckets;
    this.#buckets = Array.from({ length: old.length * 2 }, () => []);
    this.#size = 0;
    for (const bucket of old) for (const [k, v] of bucket) this.put(k, v);
  }
}

const table = new HashTable();
for (const word of 'the quick brown fox jumps over the lazy dog the end'.split(' ')) {
  table.put(word, (table.get(word) ?? 0) + 1);
}
console.log(table.get('the'), table.get('fox'), table.get('cat')); // 3 1 undefined
