function solution(number, limit, power) {
  let answer = 0
  const lvs = []
  for (i = 1; i <= number; i++) {
    let cnt = 0
    for (j = 1; j <= i / 2; j++) {
      if (i % j == 0) {
        cnt += 1
      }
    }
    lvs.push(cnt + 1)
  }
  lvs.map((lv) => {
    lv > limit ? (answer += power) : (answer += lv)
  })
  return answer
}
