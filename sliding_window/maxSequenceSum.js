/* 
Given array arr=[1,2,6,2,4,1]
k = 3
Find maximum sum of subarray with O(N) time complexity
*/
const maxSequenceSum = (listOfItems, sequenceLength) => {
  if (sequenceLength > listOfItems.length) {
    return null;
  }

  let windowSum = 0;

  // calculate the sum of 1st window
  for (let i = 0; i < sequenceLength; i++) {
    windowSum += listOfItems[i];
  }

  let maxSum = windowSum;

  //slide the window and update the sum
  for (let i = sequenceLength; i < listOfItems.length; i++) {
    windowSum += listOfItems[i] - listOfItems[i - sequenceLength];
    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
};

console.log(maxSequenceSum([1,2,6,2,4,1], 3))
console.log(maxSequenceSum([1,4,2,10,2,3,1,0,20], 4))
