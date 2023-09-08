/**
 * Counting sort algorithm
 * Time complexity O(n + k) , where k is the range
 * of non-negative key values
 * Space complexity O(n + k)
 * @param {Array} array - array of integers
 * @returns {Array} - a matrix of two arrays one sorted
 * in ascending order and the other in descending order
 */
function countingSort(array) {
  const arraySize = array.length;
  const lastIndex = arraySize - 1;
  const max = Math.max(...array);
  const ascSortedArray = new Array(arraySize);
  const descSortedArray = new Array(arraySize);
  const count = new Array(max + 1).fill(0);

  // Get frequency of elements
  array.forEach((element) => { count[element] += 1; });

  // Get prefix-sum of the keys
  for (let index = 1; index < max + 1; index += 1) count[index] += count[index - 1];
  console.log(count);
  // Fill sorted arrays
  for (let index = arraySize - 1; index >= 0; index -= 1) {
    const key = array[index];
    count[key] -= 1;
    const ascSortedIndex = count[key];
    const descSortedIndex = lastIndex - count[key];
    ascSortedArray[ascSortedIndex] = array[index];
    descSortedArray[descSortedIndex] = array[index];
  }
  return [ascSortedArray, descSortedArray];
}

/**
 * Main function
 */
function main() {
  const array = [19, 48, 13, 99, 71, 13, 52, 96, 96, 73, 86, 7];
  const sortedArrays = countingSort(array);
  console.log('Ascending count sort:\n', sortedArrays[0]);
  console.log('Descending count sort:\n', sortedArrays[1]);
}

main();
