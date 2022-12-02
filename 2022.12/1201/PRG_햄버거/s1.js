function solution(ingredient) {
  let answer = 0
  const stack = []
  ingredient.map((num) => {
    stack.push(num)
    if (stack.length >= 4) {
      if (JSON.stringify(stack.slice(-4)) == JSON.stringify([1, 2, 3, 1])) {
        answer += 1
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
      }
    }
  })
  return answer
}

console.log(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
console.log(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
