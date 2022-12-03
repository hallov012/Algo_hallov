function solution(order) {
  let idx = 0
  const stack = []
  for (i = 1; i <= order.length; i++) {
    stack.push(i)
    while (stack.length && stack[stack.length - 1] == order[idx]) {
      stack.pop()
      idx++
    }
  }
  return idx
}

console.log(solution([4, 3, 1, 2, 5]))
