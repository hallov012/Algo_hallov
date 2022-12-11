function solution(s) {
  const answer = []
  const cnt = {}
  const word = [...s]
  for (i = 0; i < word.length; i++) {
    const char = word[i]
    if (cnt[char] !== undefined) {
      answer.push(i - cnt[char])
    } else {
      answer.push(-1)
    }
    cnt[char] = i
  }
  return answer
}

console.log(solution("banana"))
console.log(solution("foobar"))
