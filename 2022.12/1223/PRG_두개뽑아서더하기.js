function solution(numbers) {
  const sumSet = new Set()
  for (i = 0; i < numbers.length; i++) {
    for (j = 0; j < numbers.length; j++) {
      if (i !== j) {
        sumSet.add(numbers[i] + numbers[j])
      }
    }
  }
  const answer = Array.from(sumSet)
  answer.sort(function (a, b) {
    return a - b
  })
  return answer
}

console.log(solution([2, 1, 3, 4, 1]))
console.log(solution([5, 0, 2, 7]))
