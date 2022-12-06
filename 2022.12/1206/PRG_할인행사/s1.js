function solution(want, number, discount) {
  let answer = 0
  const wishList = []

  for (i = 0; i < want.length; i++) {
    for (j = 0; j < number[i]; j++) {
      wishList.push(want[i])
    }
  }

  for (i = 0; i < discount.length - 9; i++) {
    const arr = [...wishList]

    for (j = i; j < i + 10; j++) {
      if (arr.includes(discount[j])) {
        arr.splice(arr.indexOf(discount[j]), 1)
      } else {
        continue
      }
    }

    if (arr.length === 0) {
      answer += 1
    }
  }

  return answer
}

console.log(
  solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    [
      "chicken",
      "apple",
      "apple",
      "banana",
      "rice",
      "apple",
      "pork",
      "banana",
      "pork",
      "rice",
      "pot",
      "banana",
      "apple",
      "banana",
    ]
  )
)
console.log(
  solution(
    ["apple"],
    [10],
    [
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
      "banana",
    ]
  )
)
