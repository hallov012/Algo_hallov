const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filePath).toString().split("\n")

const nums = input.map((num) => Number(num))

let array = new Array(31).fill(0)
for (let i = 0; i < nums.length; i++) {
  array[nums[i]] = 1
}
for (let i = 1; i <= 30; i++) {
  if (!array[i]) {
    console.log(i)
  }
}
