function solution(topping) {
  let answer = 0
  let dic = {}
  let setDic = new Set()
  topping.forEach((num) => {
    if (Object.keys(dic).includes(String(num))) {
      dic[num] += 1
    } else {
      dic[num] = 1
    }
  })

  let dicLength = Object.keys(dic).length
  topping.forEach((num) => {
    dic[String(num)] -= 1
    setDic.add(num)
    if (dic[String(num)] === 0) {
      dicLength -= 1
    }
    if (setDic.size === dicLength) {
      answer += 1
    }
  })

  return answer
}

console.log(solution([1, 2, 1, 3, 1, 4, 1, 2]))
console.log(solution([1, 2, 3, 1, 4]))
