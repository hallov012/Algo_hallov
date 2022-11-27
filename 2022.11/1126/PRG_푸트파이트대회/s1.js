function solution(food) {
  let left = ""
  for (i = 1; i < food.length; i++) {
    const m = parseInt(food[i] / 2)
    left += String(i).repeat(m)
  }
  const right = left.split("").reverse().join("")
  const ans = left + "0" + right
  return ans
}

console.log(solution([1, 3, 4, 6]))
