/**
 * Radix sort algorithm
 * - LSD implementation is stable
 * - MSD implementation is unstable
 * Time complexity:
 * - Worst case:
 *     => O(w.n) where:
 *          1. n is the number of keys
 *          2. w is the key length
 *     => Also O(d.(n + b)) where:
 *          1. d is the number of keys
 *          2. n is the number of elements
 *          3. b is the base of the number system being used
 * Space complexity:
 * - Worst case: O(w.n)
 */

/**
 * Count sort subroutine
 * @param {number[]} arr - array of integers
 * @param {number} tense - current tense
 */
function countSort(arr, tense) {
  const tempArr = Array(arr.length).fill(0);
  const countArr = Array(10).fill(0);

  // frequency of current significant digits
  arr.forEach((num) => {
    const significantDigit = Math.floor(num / tense) % 10;
    countArr[significantDigit] += 1;
  });

  // prefix sum
  for (let i = 1; i < countArr.length; i += 1) countArr[i] += countArr[i - 1];

  // place elements in the right place
  for (let i = arr.length - 1; i >= 0; i -= 1) {
    const significantDigit = Math.floor(arr.at(i) / tense) % 10;
    countArr[significantDigit] -= 1;
    const index = countArr[significantDigit];
    tempArr[index] = arr[i];
  }

  // copy items to original array
  for (let i = 0; i < arr.length; i += 1) arr[i] = tempArr[i];
}

/**
 * Radix sort implementation using least significant
 * digit
 * @param {number[]} arr - array of integers
 */
function radixSort(arr) {
  const max = Math.max(...arr);
  let tense = 1;

  while ((max / tense) > 0) {
    countSort(arr, tense);
    tense *= 10;
  }
}

/**
 * Entry point
 */
function main() {
  const arr = [102, 101, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  radixSort(arr);
  console.log(arr);
}

main();
