function solution(elements) {
  const n = elements.length
  const sumSet = new Set()
  for (len = 1; len <= n; len++) {
    for (start = 0; start < n; start++) {
      let subSum = 0
      for (i = start; i < start + len; i++) {
        subSum += elements[i % n]
      }
      sumSet.add(subSum)
    }
  }
  const answer = sumSet.size
  return answer
}

console.log(solution([7, 9, 1, 1, 4]))
