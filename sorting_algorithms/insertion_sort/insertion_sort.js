/**
 * Swap optimized implementation of insertion sort
 * Time complexity: O(n^2) comparisons and swaps
 * Best-case: O(n) list is already sorted and therefore
 * the inner loop doesn't run all, O(1)swaps
 * Average performance: O(n^2) comparisons and swaps
 * Space complexity: O(1)
 * @param {number[]} arr - unsorted array of integers
 */
function insertionSort(arr) {
  const arraySize = arr.length;
  for (let i = 1; i < arraySize; i += 1) {
    const currentNum = arr[i];
    let j = i - 1;
    for (; j >= 0 && arr[j] > currentNum; j -= 1) arr[j + 1] = arr[j];
    arr[j + 1] = currentNum;
  }
}

/**
 * Entry point
 */
function main() {
  const arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  insertionSort(arr);
  console.log(arr);
}

module.exports = { insertionSort, main };
