/**
 * Bucket sort algorithm
 * Place elements in buckets and sort each bucket
 * Worst-case: O(n^2) - when most element are in the same bucket
 * Best-case: O(n + k) - when elements are uniformly distributed
 * Average-case: O(n + k + (n^2)/k) - when elements are uniformly distributed
 *  - Might change based on sorting algorithm used for sorting buckets
 * Best-case space complexity: O(n) auxillary
 * Worst-case space complexity: O(n + k) auxillary
 */

/**
 * Merge the left and right arrays
 * @param {number[]} arr - original array
 * @param {number[]} leftArray - left subarray
 * @param {number[]} rightArray - right subarray
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
  while (i < leftArray.length) {
    arr[k] = leftArray[i];
    i += 1;
    k += 1;
  }
  while (j < rightArray.length) {
    arr[k] = rightArray[j];
    j += 1;
    k += 1;
  }
}

/**
 * Implementation of merge sort algorithm
 * @param {number[]} arr - array to be sorted
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

/**
 * Hash the value to a bucket
 * @param {number} value - value to be hashed
 * @param {number} maxValue - maximum value
 * @param {number} bucketSize - size of the bucket
 * @returns {number} - hashed value
 */
function bucketHash(value, maxValue, bucketSize) {
  return Math.floor((value / (maxValue + 1)) * bucketSize);
}

/**
 * Implementation of bucket sort algorithm
 * @param {number[]} arr - array to be sorted
 * @param {number} bucketSize - size of the bucket
 * @returns {[]} - sorted array
 */
function bucketSort(arr, bucketSize = 5) {
  if (!arr.length) return arr;
  const max = Math.max(...arr);
  const buckets = [];

  for (let i = 0; i < bucketSize; i += 1) buckets.push([]);
  for (const i of arr) {
    const index = bucketHash(i, max, bucketSize);
    buckets[index].push(i);
  }
  for (const bucket of buckets) mergeSort(bucket);
  return buckets.flat();
}

/**
 * Entry point
 */
function main() {
  const arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  console.log('Original array:', arr);
  console.log('Ascending bucket sort:', bucketSort(arr));
}

module.exports = { bucketSort, main };
