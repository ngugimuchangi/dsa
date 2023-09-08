/**
 * Bubble sort algorithm
 * Upper-bound - O(n^2) comparisons, swaps
 * Lower-bound - O(n), O(1) swaps
 * Average performance - O(n^2) comparisons and swaps
 * Space-complexity - O(1)
 * @param {Array} arr - array of integers
 */
function bubbleSort(arr) {
  let arraySize = arr.length;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 1; i < arraySize; i += 1) {
      const prevNum = arr[i - 1];
      const currentNum = arr[i];
      if (prevNum > currentNum) {
        [arr[i - 1], arr[i]] = [currentNum, prevNum];
        swapped = true;
      }
    }
    arraySize -= 1;
  }
}

function main() {
  const array = [19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7];
  bubbleSort(array);
  console.log(array);
}
main();
