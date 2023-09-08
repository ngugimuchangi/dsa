/**
 * Bitonic sort is a comparison-based sorting algorithm that can be run in parallel.
 * It focuses on converting a random sequence of numbers into a bitonic sequence,
 * one that monotonically increases, then decreases.
 * The algorithm consists of two parts:
 *  1. Creating a bitonic sequence
 *  2. Sorting it
 * The first part is done recursively, and the second part is done iteratively.
 * Length of the input array must be a power of 2.
 * The algorithm is O(n log^2 n) in all cases.
 * Space complexity is O(n log^2 n) due to the recursive nature of the algorithm.
 */

/**
 * Bitonic merge subroutine.
 * @param {number[]} arr - array to be sorted
 * @param {number} lowIndex - starting index
 * @param {number} count - length of the array
 * @param {boolean} direction - direction of sorting, false for ascending, true for descending
 */
function bitonicMerge(arr, lowIndex, count, direction) {
  if (count <= 1) return;
  const length = count / 2;
  for (let i = lowIndex; i < lowIndex + length; i += 1) {
    if (arr[i] < arr[i + length] === direction) {
      [arr[i], arr[i + length]] = [arr[i + length], arr[i]];
    }
  }
  bitonicMerge(arr, lowIndex, length, direction);
  bitonicMerge(arr, lowIndex + length, length, direction);
}

/**
 * Bitonic sort algorithm.
 * @param {number[]} arr - array to be sorted
 * @param {number} lowIndex - starting index
 * @param {number} count - length of the array
 * @param {boolean} reversed - direction of sorting, true for ascending, false for descending
 */
function bitonicSort(arr, lowIndex, count, reversed = false) {
  if (count <= 1) return;
  const length = count / 2;

  // Split array into two parts
  bitonicSort(arr, lowIndex, length);
  bitonicSort(arr, lowIndex + length, length, true);

  // Merge the results
  bitonicMerge(arr, lowIndex, count, reversed);
}

/**
 * Sort function
 * @param {number[]} arr - array to be sorted
 * @param {boolean} reversed - direction of sorting
 */
function sort(arr, reversed = false) {
  bitonicSort(arr, 0, arr.length, reversed);
}

/**
 * Entry point.
 */
function main() {
  const arr = [1, 5, 2, 4, 3, 6, 8, 7];
  console.log('Array:', arr);
  sort(arr);
  console.log('Ascending bitonic sort:', arr);
  sort(arr, true);
  console.log('Descending bitonic sort:', arr);
}

main();
