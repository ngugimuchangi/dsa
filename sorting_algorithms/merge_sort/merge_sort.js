/**
 * Merge sort algorithm
 * Worst-case: O(n(log(n)))
 * Best-case: O(n(log(n)))
 * Average-case: O(n(log(n)))
 * Worst-case-space-complexity:
 *     - O(n) auxillary space
 *     - O(1) with linked list
 *     - Stack size is O(log(n))
 * Characteristics:
 *   - Stable
 *   - Not adaptive
 */

/**
 * Merges the right and left arrays
 * @param {Array} arr - original array
 * @param {Array} leftArray - left subarray
 * @param {Array} rightArray - right subarray
 */
function merge(arr, leftArray, rightArray) {
  let i = 0;
  let j = 0;
  let k = 0;
  while (i < leftArray.length && j < rightArray.length) {
    if (leftArray[i] <= rightArray[j]) {
      arr[k] = leftArray[i];
      i += 1;
      k += 1;
    } else {
      arr[k] = rightArray[j];
      j += 1;
      k += 1;
    }
  }

  // place remaining item on left array
  // into the original array
  while (i < leftArray.length) {
    arr[k] = leftArray[i];
    i += 1;
    k += 1;
  }

  // place remaining item on right array
  // into the original array
  while (j < rightArray.length) {
    arr[k] = rightArray[j];
    j += 1;
    k += 1;
  }
}

/**
 * Merge sort algorithm
 * @param {Array} arr - array of integers
 */
function mergeSort(arr) {
  if (arr.length <= 1) return;
  const mid = Math.floor(arr.length / 2);
  const leftArray = arr.slice(0, mid);
  const rightArray = arr.slice(mid);
  mergeSort(leftArray);
  mergeSort(rightArray);
  merge(arr, leftArray, rightArray);
}

function main() {
  const arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  console.time('mergeSort');
  mergeSort(arr);
  console.timeEnd('mergeSort');
  console.log('Ascending merge sort:\n', arr);
}

main();
