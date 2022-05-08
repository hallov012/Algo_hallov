import sys
sys.setrecursionlimit(10 ** 9)

sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
ans = []
index = [0] * (n+1)

for i in range(n):
    index[inorder[i]] = i

def preorder(si, ei, sp, ep):
    if (si > ei) or (sp > ep):
        return
    parent = postorder[ep]
    ans.append(postorder[ep])
    left = index[parent] - si
    right = ei - index[parent]

    preorder(si, si + left - 1, sp, sp + left - 1)
    preorder(ei - right + 1, ei, ep - right, ep - 1)

preorder(0, n-1, 0, n-1)
print(*ans)