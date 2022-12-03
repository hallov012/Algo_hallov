function solution(a, b, n) {
  let ans = 0
  let cnt = n
  while (cnt >= a) {
    const temp = parseInt(cnt / a) * b
    ans += temp
    cnt = (cnt % a) + temp
  }
  return ans
}
