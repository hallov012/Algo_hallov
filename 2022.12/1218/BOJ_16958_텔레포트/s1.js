const fs = require("fs")
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"
const input = fs.readFileSync(filePath).toString().trim().split("\n")

const [n, t] = input[0].split(" ").map((element) => Number(element))
const city = input
  .slice(1, n + 1)
  .map((data) => data.split(" ").map((element) => Number(element)))

const g = new Array(n)
for (i = 0; i < n; i++) {
  g[i] = new Array(n).fill(0)
}

for (i = 0; i < n - 1; i++) {
  const [s1, x1, y1] = city[i]
  for (j = i + 1; j < n; j++) {
    const [s2, x2, y2] = city[j]
    const dist = Math.abs(x1 - x2) + Math.abs(y1 - y2)
    if (s1 === 1 && s2 === 1 && dist > t) {
      g[i][j] = t
      g[j][i] = t
    } else {
      g[i][j] = dist
      g[j][i] = dist
    }
  }
}

for (k = 0; k < n; k++) {
  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
      g[i][j] = Math.min(g[i][j], g[i][k] + g[k][j])
    }
  }
}

const m = Number(input[n + 1])
const question = input
  .slice(n + 2)
  .map((data) => data.split(" ").map((element) => Number(element)))

question.forEach(([x, y], idx) => {
  console.log(g[x - 1][y - 1])
})
