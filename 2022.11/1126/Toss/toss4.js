function solution(id) {
  const n = id.length
  const m = parseInt(n / 2)
  const start = parseInt((n - m) / 2)

  let answer = ""
  answer += id.substring(0, start)
  answer += "*".repeat(m)
  answer += id.slice(start + m)
  return answer
}

console.log(solution("k9t0nio7e"))
