function solution(X, Y) {
  let answer = ""
  let cnt1 = new Array(10).fill(0)
  let cnt2 = new Array(10).fill(0)

  Array.from(X).forEach((num) => {
    cnt1[Number(num)] += 1
  })

  Array.from(Y).forEach((num) => {
    cnt2[Number(num)] += 1
  })

  for (i = 9; i >= 0; i--) {
    const temp = Math.min(cnt1[i], cnt2[i])
    for (j = 0; j < temp; j++) {
      answer += String(i)
    }
  }

  if (answer === "") {
    answer = "-1"
  } else if (Number(answer) === 0) {
    answer = "0"
  }

  return answer
}

console.log(solution("100", "2345"))
console.log(solution("100", "203045"))
console.log(solution("100", "123450"))
console.log(solution("12321", "42531"))
