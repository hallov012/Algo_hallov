function solution(s) {
  let answer = []
  const cnt = {}
  const str = [...s]
  str.forEach((char) => {
    if (Object.keys(cnt).includes(char)) {
      cnt[char] += 1
    } else {
      cnt[char] = 1
    }
  })

  for (const char in cnt) {
    if (cnt[char] === 1) {
      answer.push(char)
    }
  }
  answer.sort()
  const ans = answer.join("")
  return ans
}

console.log(solution("abcabcadc"))
console.log(solution("abdc"))
