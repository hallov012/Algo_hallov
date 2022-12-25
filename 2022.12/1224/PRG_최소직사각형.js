function solution(sizes) {
  let answer = 0
  let a = 0
  let b = 0
  sizes.forEach((size) => {
    const [x, y] = size
    if (x >= y) {
      a = Math.max(a, x)
      b = Math.max(b, y)
    } else {
      a = Math.max(a, y)
      b = Math.max(b, x)
    }
  })
  answer = a * b
  return answer
}

console.log(
  solution([
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40],
  ])
)
console.log(
  solution([
    [10, 7],
    [12, 3],
    [8, 15],
    [14, 7],
    [5, 15],
  ])
)
console.log(
  solution([
    [14, 4],
    [19, 6],
    [6, 16],
    [18, 7],
    [7, 11],
  ])
)
