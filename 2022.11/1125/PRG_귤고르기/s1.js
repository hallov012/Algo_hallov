function solution(k, tangerine) {
  let answer = 0
  let cnt = {}
  tangerine.map((num) => {
    if (cnt[num]) {
      cnt[num] += 1
    } else {
      cnt[num] = 1
    }
  })
  let sorted = []
  for (let num in cnt) {
    sorted.push([num, cnt[num]])
  }
  sorted.sort((a, b) => b[1] - a[1])
  let box = 0
  for (const idx in sorted) {
    box += sorted[idx][1]
    answer += 1
    if (box >= k) {
      break
    }
  }
  return answer
}

console.log(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
