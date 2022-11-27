function solution(paths) {
  let ans = []
  paths.map((str) => {
    if (str == "..") {
      ans.pop()
    } else if (str == "...") {
      ans.pop()
      ans.pop()
    } else {
      if (str[str.length - 1] == "/") {
        str = str.substring(0, str.length - 1)
      }
      if (str[0] == "/") {
        ans.push(str)
      } else {
        ans.push(`/${str}`)
      }
    }
  })
  let answer = ans.join("")
  if (answer == "") {
    answer = "/"
  }
  return answer
}

console.log(solution(["/foo", "bar", "/baz", "...", "ab/"]))
