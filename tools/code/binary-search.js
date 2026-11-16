function binarySearch(items, target) {     // O(log n); items must be sorted
  let lo = 0, hi = items.length - 1;
  while (lo <= hi) {
    const mid = lo + Math.floor((hi - lo) / 2);
    if (items[mid] === target) return mid;
    if (items[mid] < target) lo = mid + 1; // target is in the right half
    else hi = mid - 1;                     // target is in the left half
  }
  return -1;
}

// First index whose value is >= target (the insertion point).
function lowerBound(items, target) {
  let lo = 0, hi = items.length;           // note: hi is one past the end
  while (lo < hi) {
    const mid = lo + Math.floor((hi - lo) / 2);
    if (items[mid] < target) lo = mid + 1;
    else hi = mid;
  }
  return lo;
}

const nums = [3, 8, 15, 15, 15, 23, 42, 57];
console.log(binarySearch(nums, 23));       // 5
console.log(binarySearch(nums, 9));        // -1
console.log(lowerBound(nums, 15));         // 2  (first 15)
