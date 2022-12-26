function solution(maps) {
  let answer = 0
  const n = maps.length
  const m = maps[0].length
  const visited = new Array(n)
  for (let i = 0; i < n; i++) {
    visited[i] = new Array(m).fill(-1)
  }
  visited[0][0] = 1
  const que = [[0, 0]]
  const dx = [1, -1, 0, 0]
  const dy = [0, 0, 1, -1]

  while (que.length !== 0) {
    const [x, y] = que.pop(0)
    if (x === n - 1 && y === m - 1) {
      break
    }
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i]
      const ny = y + dy[i]
      if (0 <= nx && nx < n && 0 <= ny && ny < m) {
        if (visited[nx][ny] === -1 && maps[nx][ny] === 1) {
          visited[nx][ny] = visited[x][y] + 1
          que.push([nx, ny])
        }
      }
    }
  }
  answer = visited[n - 1][m - 1]
  return answer
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
)
console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1],
  ])
)
