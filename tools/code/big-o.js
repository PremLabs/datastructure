const firstItem = items => items[0];              // O(1)

function contains(items, target) {                // O(n)
  for (const item of items) {
    if (item === target) return true;
  }
  return false;
}

function hasDuplicate(items) {                    // O(n^2)
  for (let i = 0; i < items.length; i++) {
    for (let j = i + 1; j < items.length; j++) {
      if (items[i] === items[j]) return true;
    }
  }
  return false;
}

function hasDuplicateFast(items) {                // O(n) time, O(n) space
  const seen = new Set();
  for (const item of items) {
    if (seen.has(item)) return true;
    seen.add(item);
  }
  return false;
}

function halvings(n) {                            // O(log n)
  let steps = 0;
  while (n > 1) { n = Math.floor(n / 2); steps++; }
  return steps;
}

console.log(halvings(1_000_000));                 // 19
console.log(hasDuplicateFast([3, 1, 4, 1]));      // true
