class TrieNode {
  children = new Map();
  isWord = false;
}

class Trie {
  root = new TrieNode();

  insert(word) {                           // O(L), L = word.length
    let node = this.root;
    for (const ch of word) {
      if (!node.children.has(ch)) node.children.set(ch, new TrieNode());
      node = node.children.get(ch);
    }
    node.isWord = true;
  }

  #find(prefix) {
    let node = this.root;
    for (const ch of prefix) {
      node = node.children.get(ch);
      if (!node) return null;
    }
    return node;
  }

  search(word) {                           // O(L): whole word stored?
    const node = this.#find(word);
    return node !== null && node.isWord;
  }

  startsWith(prefix) {                     // O(L)
    return this.#find(prefix) !== null;
  }

  autocomplete(prefix) {                   // every stored word under the prefix
    const results = [];
    const collect = (node, path) => {
      if (node.isWord) results.push(path);
      for (const ch of [...node.children.keys()].sort()) collect(node.children.get(ch), path + ch);
    };
    const start = this.#find(prefix);
    if (start) collect(start, prefix);
    return results;
  }
}

const trie = new Trie();
['car', 'cat', 'cart', 'do', 'dog'].forEach(word => trie.insert(word));
console.log(trie.search('car'), trie.search('ca'));  // true false
console.log(trie.startsWith('ca'));                  // true
console.log(trie.autocomplete('ca'));                // [ 'car', 'cart', 'cat' ]
