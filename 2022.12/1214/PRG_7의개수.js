function solution(array) {
  let str = ""
  array.forEach((element) => {
    str += String(element)
  })
  const cnt = str.split("7").length - 1
  return cnt
}
console.log(solution([7, 77, 17]))
console.log(solution([10, 29]))
