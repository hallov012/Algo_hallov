function solution(cards) {
  let answer = 0
  const n = cards.length
  const data = [0, ...cards]
  firstPlay()

  function firstPlay() {
    for (i = 1; i < n + 1; i++) {
      const fisrt = [i]
      const checked = new Array(n + 1).fill(0)
      checked[i] = 1
      let idx = data[i]
      while (!checked[idx]) {
        checked[idx] = 1
        fisrt.push(idx)
        idx = data[idx]
      }
      secondPlay(fisrt, checked)
    }
  }

  function secondPlay(fisrt, checked) {
    for (j = 1; j < n + 1; j++) {
      if (!checked[j]) {
        const checkedCopy = [...checked]
        const second = [j]
        checkedCopy[j] = 1
        let idx = data[j]
        while (!checkedCopy[idx]) {
          checkedCopy[idx] = 1
          second.push(idx)
          idx = data[idx]
        }
        answer = Math.max(answer, fisrt.length * second.length)
      }
    }
  }

  return answer
}

console.log(solution([8, 6, 3, 7, 2, 5, 1, 4]))
