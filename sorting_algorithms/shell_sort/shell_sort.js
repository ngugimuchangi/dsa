/**
 * Shell sort algorithm
 * Worst-case: O(n^2)
 * Best-case: O(n log(n))
 * Average performance: depends on gap
 *  - Knuth sequence avg performance = O(n ^ 3/2)
 * Space complexity: O(1)
 */

/**
 * Computes maximum gap using Knuth sequence
 * @param {number} size - array size
 * @returns - maximum gap in Knuth sequence
 */
function knuthSequenceGap(size) {
  let gap = 1;
  while (gap < size) gap = (gap * 3) + 1;
  return gap;
}

/**
 * Shell sort algorithm
 * @param {number[]} arr - array of integers
 */
function shellSort(arr) {
  let gap = knuthSequenceGap(arr.length);

  while (gap) {
    for (let i = gap; i < arr.length; i += 1) {
      const temp = arr.at(i);
      let j = i;
      while (j >= gap && arr[j - gap] < temp) {
        arr[j] = arr[j - gap];
        j -= gap;
      }
      arr[j] = temp;
    }
    gap = Math.floor(gap / 3);
  }
}

/**
 * Entry point
 */
function main() {
  const arr = [101, 102, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  shellSort(arr);
  console.log('Descending shell sort:\n', arr);
}

main();
