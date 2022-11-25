function solution(k, score) {
  const answer = []
  const dayScore = []
  for (let i = 0; i < score.length; i++) {
    dayScore.push(score[i])
    dayScore.sort(function (a, b) {
      return b - a
    })
    if (i < k) {
      answer.push(dayScore[i])
    } else {
      answer.push(dayScore[k - 1])
    }
  }
  return answer
}
