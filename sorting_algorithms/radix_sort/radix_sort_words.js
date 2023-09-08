const { insertionSort } = require('../insertion_sort/insertion_sort');

/**
 * Bucket sort sub-routine implementation for strings
 * @param {str[]} arr - array of strings to be sorted
 * @param {number} index - index of the character to be sorted
 * @param {number} bucketSize - size of the bucket
 * @returns - sorted array
 */

function bucketSort(arr, index = 0, bucketSize = 256) {
  let buckets = Array(bucketSize).fill().map(() => []);

  // Hash current character to a bucket
  for (const i of arr) {
    const bucketIndex = i[index] ? i.charCodeAt(index) : 0;
    buckets[bucketIndex].push(i);
  }

  // Recursively sort buckets
  buckets = buckets.map((bucket) => {
    // If bucket has more than one element, sort it recursively
    insertionSort(bucket);
    if (bucket.length > 1 && index < bucket[0].length - 1) {
      return bucketSort(bucket, index + 1, bucketSize);
    }
    return bucket;
  });
  return buckets.flat();
}

/**
 * Radix sort implementation using most significant digit (MSD)
 * @param {str[]} arr - array to be sorted
 * @returns {str[]} - sorted array
 */
function radixSort(arr) {
  if (!arr || arr.length < 2) return [];
  return bucketSort(arr);
}

function main() {
  let arr = [
    '01', '1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010',
    '2', '20', '21', '200', '201', '210', '3', '30', '31', '300', '301', '310',
    'apple',
    'banana',
    'application',
    'apricot',
    'banana split',
    'apartment',
    'candy',
    'application form',
    'apron',
    'candy apple',
    'banana bread',
    'april',
    'apple pie',
    'apartment complex',
    'banana cream pie',
    'candy bar',
    'apex',
    'apple cider',
    'banana smoothie',
    'candy cane',
  ];
  arr = arr.concat(arr.slice(0, arr.length).reverse());
  console.log('Array length: ', arr.length);
  console.time('radixSort');
  arr = radixSort(arr);
  console.timeEnd('radixSort');
  console.log(arr);
}

main();
