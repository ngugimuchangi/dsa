/**
 * Binary search algorithm
 * Worst-case: O(log(n))
 * Best-case: O(1) - item at the beginning of array
 * Average-case: O(log(n))
 * Space complexity: O(1)
 */

/**
 * Binary search algorithm
 * @param {Array} arr - array of integers
 * @param {number} num - search term
 * @returns {(number | null)} - index of search term
 * or null if not found
 */
function binarySearch(arr, num) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] < num) left = mid + 1;
    else if (arr[mid] > num) right = mid - 1;
    else return mid;
  }
  return null;
}

/**
 * Entry point
 */
function main() {
  const arr = Array(52).fill(0).map((_el, index) => index);
  const num = 0;
  const index = binarySearch(arr, num);
  console.log(index);
}

main();
