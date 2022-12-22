function solution(t, p) {
  let answer = 0
  for (i = 0; i < t.length - p.length + 1; i++) {
    const temp = t.slice(i, i + p.length)
    if (Number(temp) <= Number(p)) {
      answer++
    }
  }
  return answer
}

console.log(solution("3141592", "271"))
console.log(solution("500220839878", "7"))
console.log(solution("10203", "15"))
