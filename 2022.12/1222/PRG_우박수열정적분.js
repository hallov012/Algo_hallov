function collatz(k) {
  const points = [k]
  let num = k
  while (num !== 1) {
    if (num % 2) {
      num = num * 3 + 1
    } else {
      num = parseInt(num / 2)
    }
    points.push(num)
  }
  return points
}

function solution(k, ranges) {
  const answer = []
  points = collatz(k)
  ranges.forEach(([a, b]) => {
    const c = points.length + b - 1
    if (a > c) {
      answer.push(-1)
    } else {
      let cnt = 0
      for (i = a; i < c; i++) {
        cnt += (points[i] + points[i + 1]) / 2
      }
      answer.push(cnt)
    }
  })
  return answer
}

console.log(
  solution(5, [
    [0, 0],
    [0, -1],
    [2, -3],
    [3, -3],
  ])
)
