function solution(N, road, K) {
  const dist = new Array(N + 1).fill(Number.MAX_SAFE_INTEGER)
  const g = Array.from(new Array(N + 1), () => [])
  let answer = 0
  road.forEach((element) => {
    const [a, b, c] = element
    g[a].push([b, c])
    g[b].push([a, c])
  })
  const que = [[1, 0]]
  dist[1] = 0
  while (que.length) {
    let [now, d] = que.pop()
    g[now].forEach(([next, cost]) => {
      if (dist[next] > dist[now] + cost) {
        dist[next] = dist[now] + cost
        que.push([next, dist[now] + cost])
      }
    })
  }
  for (let i = 1; i < N + 1; i++) {
    if (dist[i] <= K) {
      answer++
    }
  }
  return answer
}

console.log(
  solution(
    5,
    [
      [1, 2, 1],
      [2, 3, 3],
      [5, 2, 2],
      [1, 4, 2],
      [5, 3, 1],
      [5, 4, 2],
    ],
    3
  )
)
console.log(
  solution(
    6,
    [
      [1, 2, 1],
      [1, 3, 2],
      [2, 3, 2],
      [3, 4, 3],
      [3, 5, 2],
      [3, 5, 3],
      [5, 6, 1],
    ],
    4
  )
)
