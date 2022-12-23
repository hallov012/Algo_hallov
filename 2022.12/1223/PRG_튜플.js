function solution(s) {
  let answer = []
  s = s.slice(2, s.length - 2)
  s = s.split("},{")
  s.sort(function (a, b) {
    return a.length - b.length
  })
  s.forEach((element) => {
    const nums = element.split(",")
    nums.forEach((num) => {
      if (!answer.includes(Number(num))) {
        answer.push(Number(num))
      }
    })
  })
  return answer
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
console.log(solution("{{20,111},{111}}"))
