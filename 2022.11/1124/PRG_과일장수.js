function solution(k, m, score) {
  let answer = 0
  score.sort(function (a, b) {
    return b - a
  })
  for (i = 0; i < score.length; i += m) {
    const arr = score.slice(i, i + m)
    if (arr.length == m) {
      answer += arr[m - 1] * m
    }
  }
  return answer
}
