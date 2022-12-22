function solution(babbling) {
  let answer = 0
  const possible = ["aya", "ye", "woo", "ma"]
  babbling.forEach((input) => {
    const word = [...input]
    let stack = ""
    let before = ""
    word.forEach((char) => {
      stack += char
      if (possible.includes(stack) && before !== stack) {
        before = stack
        stack = ""
      }
    })
    if (!stack.length) {
      answer++
    }
  })
  return answer
}

console.log(solution(["aya", "yee", "u"]))
console.log(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
