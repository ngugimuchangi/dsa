/**
 * Cocktail shaker sort aka bi-directional bubble sort
 * Helps move turtles in bubble sort
 * Worst-case: O(n^2)
 * Best-case: O(n)
 * Average-case: O(n^2)
 * Space-complexity: O(1)
 */

/**
 * Cocktail shaker sort
 * @param {number[]} arr - arr of integers
 */
function cocktailShakerSort(arr) {
  let swapped = true;
  let firstIndex = 0;
  let lastIndex = arr.length;
  let lastSwapIndex = 0;
  while (swapped) {
    swapped = false;
    for (let i = firstIndex + 1; i < lastIndex; i += 1) {
      const currentNum = arr.at(i);
      const prevNum = arr.at(i - 1);
      if (prevNum < currentNum) {
        [arr[i], arr[i - 1]] = [prevNum, currentNum];
        swapped = true;
        lastSwapIndex = i;
      }
    }
    lastIndex = lastSwapIndex;

    if (!swapped) break;

    for (let i = lastIndex - 1; i > firstIndex; i -= 1) {
      const currentNum = arr.at(i);
      const nextNum = arr.at(i - 1);
      if (currentNum > nextNum) {
        [arr[i], arr[i - 1]] = [nextNum, currentNum];
        swapped = true;
        lastSwapIndex = i - 1;
      }
    }
    firstIndex = lastSwapIndex;
  }
}

/**
 * Entry point
 */
function main() {
  const arr = [101, 102, 19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7, 99, 100];
  cocktailShakerSort(arr);
  console.log('Descending cocktail shaker sort:\n', arr);
}

main();
