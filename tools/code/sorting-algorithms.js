function bubbleSort(a) {                   // O(n^2), stable, in place
  for (let i = 0; i < a.length; i++) {
    let swapped = false;
    for (let j = 0; j < a.length - i - 1; j++) {
      if (a[j] > a[j + 1]) { [a[j], a[j + 1]] = [a[j + 1], a[j]]; swapped = true; }
    }
    if (!swapped) break;                   // already sorted: stop early
  }
  return a;
}

function selectionSort(a) {                // O(n^2), not stable, in place
  for (let i = 0; i < a.length - 1; i++) {
    let smallest = i;
    for (let j = i + 1; j < a.length; j++) if (a[j] < a[smallest]) smallest = j;
    [a[i], a[smallest]] = [a[smallest], a[i]];
  }
  return a;
}

function insertionSort(a) {                // O(n^2) worst, O(n) if nearly sorted, stable
  for (let i = 1; i < a.length; i++) {
    const key = a[i];
    let j = i - 1;
    while (j >= 0 && a[j] > key) { a[j + 1] = a[j]; j--; }
    a[j + 1] = key;
  }
  return a;
}

function mergeSort(a) {                    // O(n log n) always, stable, O(n) extra space
  if (a.length <= 1) return a;
  const mid = a.length >> 1;
  const left = mergeSort(a.slice(0, mid)), right = mergeSort(a.slice(mid));
  const merged = [];
  let i = 0, j = 0;
  while (i < left.length && j < right.length) merged.push(left[i] <= right[j] ? left[i++] : right[j++]);
  return merged.concat(left.slice(i), right.slice(j));
}

function quickSort(a, lo = 0, hi = a.length - 1) {   // O(n log n) average, O(n^2) worst
  if (lo < hi) {
    const pivot = a[hi];
    let i = lo;
    for (let j = lo; j < hi; j++) {        // Lomuto partition
      if (a[j] < pivot) { [a[i], a[j]] = [a[j], a[i]]; i++; }
    }
    [a[i], a[hi]] = [a[hi], a[i]];
    quickSort(a, lo, i - 1);
    quickSort(a, i + 1, hi);
  }
  return a;
}

const data = [38, 27, 43, 3, 9, 82, 10];
for (const sort of [bubbleSort, selectionSort, insertionSort, mergeSort, quickSort]) {
  console.log(sort.name, sort([...data])); // each prints [3, 9, 10, 27, 38, 43, 82]
}
// Note: the built-in a.sort() compares as strings unless you pass (x, y) => x - y.
