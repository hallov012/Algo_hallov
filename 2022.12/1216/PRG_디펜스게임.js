class MaxHeap {
  constructor() {
    this.heap = []
  }
  push(val) {
    this.heap.push(val)
    let idx = this.heap.length - 1
    const element = this.heap[idx]
    while (idx > 0) {
      let parIdx = Math.floor((idx - 1) / 2)
      let par = this.heap[parIdx]
      if (element <= par) break
      this.heap[parIdx] = element
      this.heap[idx] = par
      idx = parIdx
    }
  }

  pop() {
    if (!this.heap.length) return undefined
    const max = this.heap[0]
    const end = this.heap.pop()
    if (this.heap.length > 0) {
      this.heap[0] = end
      let idx = 0
      const element = this.heap[0]
      while (true) {
        const leftIdx = idx * 2 + 1
        const left = this.heap[leftIdx]
        const rightIdx = idx * 2 + 2
        const right = this.heap[rightIdx]
        if (element < left && element < right) {
          const maxIdx = left > right ? leftIdx : rightIdx
          this.heap[idx] = this.heap[maxIdx]
          this.heap[maxIdx] = element
          idx = maxIdx
        } else if (element < left) {
          this.heap[idx] = left
          this.heap[leftIdx] = element
          idx = leftIdx
        } else if (element < right) {
          this.heap[idx] = right
          this.heap[rightIdx] = element
          idx = rightIdx
        } else break
      }
    }
    return max
  }
}

function solution(n, k, enemy) {
  let answer = 0
  const maxHeap = new MaxHeap()

  for (i = 0; i < enemy.length; i++) {
    maxHeap.push(enemy[i])
    n -= enemy[i]
    if (n < 0) {
      if (k) {
        const max = maxHeap.pop()
        n += max
        k--
      } else break
    }
    answer++
  }

  return answer
}

console.log(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
console.log(solution(2, 4, [3, 3, 3, 3]))
