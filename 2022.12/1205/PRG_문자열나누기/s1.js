function solution(s) {
  let answer = 0
  const strs = Array.from(s)
  let firstStr = strs[0]
  let check1 = 0
  let check2 = 0
  for (const idx in strs) {
    firstStr === strs[idx] ? (check1 += 1) : (check2 += 1)
    if (check1 == check2) {
      answer += 1
      check1 = 0
      check2 = 0
      firstStr = strs[Number(idx) + 1]
    }
  }

  if (check1 + check2 !== 0) {
    answer += 1
  }

  return answer
}

console.log(solution("banana"))
console.log(solution("abracadabra"))
console.log(solution("aaabbaccccabba"))
