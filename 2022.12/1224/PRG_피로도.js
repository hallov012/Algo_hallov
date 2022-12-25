function solution(k, dungeons) {
  let answer = -1
  const n = dungeons.length
  const visited = new Array(n).fill(0)
  function dfs(t, cnt) {
    if (cnt > answer) {
      answer = cnt
    }
    for (let i = 0; i < n; i++) {
      if (!visited[i] && t >= dungeons[i][0]) {
        visited[i] = 1
        dfs(t - dungeons[i][1], cnt + 1)
        visited[i] = 0
      }
    }
  }
  dfs(k, 0)
  return answer
}

console.log(
  solution(80, [
    [80, 20],
    [50, 40],
    [30, 10],
  ])
)
