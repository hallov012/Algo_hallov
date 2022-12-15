function solution(common) {
  let ans = 0
  if (common[1] - common[0] === common[2] - common[1]) {
    const d = common[1] - common[0]
    ans = common[0] + d * common.length
  } else if (common[1] / common[0] === common[2] / common[1]) {
    const r = parseInt(common[1] / common[0], 10)
    ans = common[0] * r ** common.length
  }
  return ans
}

console.log(solution([1, 2, 3, 4]))
console.log(solution([2, 4, 8]))
