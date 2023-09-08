/** *
 * Quick sort algorithm
 * Worst-case: O(n^2)
 * Best-case: O(n(log(n)))
 * Average-case: O(n(log(n)))
 * Worst-case space complexity: O(n) auxillary
 * Best-case space complexity: O(log(n)) Hoare
 *  - Recursive nature of the algo is responsible
 *    for the auxillary space
 * Unstable
 */

/**
 * Median of three pivot selection - selects median value between
 * first, middle and last elements and moves it to the end of the array
 * @param {Array} arr - array of integers
 * @param {number} firstIndex - starting index of array/subarray
 * @param {number} lastIndex  - last index of array/subarray
 * @returns {number} - pivot value
 */

// eslint-disable-next-line no-unused-vars
function medianOfThreePivotSelection(arr, firstIndex, lastIndex) {
  const midIndex = Math.floor((firstIndex + lastIndex) / 2);
  if (arr.at(midIndex) < arr.at(firstIndex)) {
    [arr[firstIndex], arr[midIndex]] = [arr[midIndex], arr[firstIndex]];
  }
  if (arr.at(lastIndex) < arr.at(firstIndex)) {
    [arr[firstIndex], arr[lastIndex]] = [arr[lastIndex], arr[firstIndex]];
  }
  if (arr.at(midIndex) < arr.at(lastIndex)) {
    [arr[midIndex], arr[lastIndex]] = [arr[lastIndex], arr[midIndex]];
  }
  return arr[lastIndex];
}

/**
 * Hoare's partitioning scheme
 * @param {Array} arr - array of integers
 * @param {number} firstIndex - starting index of array/subarray
 * @param {number} lastIndex  - last index of array/subarray
 * @returns {number} - pivot index
 */
function hoarePartitioning(arr, firstIndex, lastIndex) {
  const pivot = arr[Math.floor((firstIndex + lastIndex) / 2)];
  let left = firstIndex - 1;
  let right = lastIndex + 1;

  while (left < right) {
    do {
      left += 1;
    } while (arr[left] > pivot);
    do {
      right -= 1;
    } while (arr[right] < pivot);

    if (left >= right) break;
    [arr[left], arr[right]] = [arr[right], arr[left]];
  }
  return right;
}

/**
 * Merge sort
 * @param {Array} arr - array of integers
 * @param {number} firstIndex - starting index of array/subarray
 * @param {number} lastIndex  - last index of array/subarray
 * @returns {void}
 */
function quickSort(arr, firstIndex, lastIndex) {
  if (firstIndex >= lastIndex) return;
  const pivot = hoarePartitioning(arr, firstIndex, lastIndex);
  quickSort(arr, firstIndex, pivot);
  quickSort(arr, pivot + 1, lastIndex);
}

function main() {
  const arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  console.time('quickSort');
  quickSort(arr, 0, arr.length - 1);
  console.timeEnd('quickSort');
  console.log('Ascending quick sort:\n', arr);
}

main();
