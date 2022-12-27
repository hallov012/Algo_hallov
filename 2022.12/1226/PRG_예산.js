function solution(d, budget) {
  let answer = 0
  d.sort(function (a, b) {
    return Number(a) - Number(b)
  })
  for (num of d) {
    if (budget >= num) {
      budget -= num
      answer += 1
    } else {
      break
    }
  }
  return answer
}

console.log(solution([1, 3, 2, 5, 12], 9))
console.log(solution([2, 2, 3, 3], 10))
