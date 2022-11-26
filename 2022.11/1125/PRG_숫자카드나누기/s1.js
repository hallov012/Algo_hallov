const gcd = (a, b) => {
  if (b == 0) {
    return a
  } else {
    return gcd(b, a % b)
  }
}

const find = (array1, array2) => {
  let ans = 0
  array1.forEach((val) => (ans = gcd(ans, val)))
  for (const num of array2) {
    if (num % ans == 0) {
      return false
      break
    }
  }
  return ans
}

function solution(arrayA, arrayB) {
  var answer = 0

  let a = find(arrayA, arrayB)
  let b = find(arrayB, arrayA)
  answer = Math.max(a, b)
  return answer
}

console.log(solution([10, 20], [5, 17]))
