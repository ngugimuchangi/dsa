/**
 * Selection sort algorithm
 * Upper bound: O(n^2), O(n) swaps
 * Lower bound: O(n^2), O(1) swaps
 * Average performance: O(n^2), O(n) swaps
 * Space complexity: O(1)
 * Unstable
 * @param {Number[]} arr - array of integers
 */
function selectionSort(arr) {
  for (let i = 0, minIndex = i; i < arr.length; i += 1) {
    for (let j = i + 1; j < arr.length; j += 1) {
      if (arr[j] < arr[minIndex]) minIndex = j;
    }
    if (minIndex !== i) [arr[minIndex], arr[i]] = [arr[i], arr[minIndex]];
  }
}

function main() {
  const arr = [19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  selectionSort(arr);
  console.log(arr);
}
main();
