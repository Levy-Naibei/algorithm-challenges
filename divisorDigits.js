// Given an integer, for each digit that makes up the integer determine 
// whether it is a divisor. 
// Count the number of divisors occurring within the integer.


function findDigits(n) {
    let divisorCount = 0;

    for (let num of n.toString()) {
        let digit = Number(num);
        if (digit !== 0 && n % digit === 0) {
            divisorCount++;
        }
    }
    return divisorCount;
}
