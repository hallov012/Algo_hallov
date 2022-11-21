const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filePath).toString().split("\n")

const num = input[0]
const scores = input[1].split(" ")
const max = Math.max(...scores)
let sum = 0
for (let i = 0; i < num; i++) {
  sum += (scores[i] / max) * 100
}
console.log(sum / num)
