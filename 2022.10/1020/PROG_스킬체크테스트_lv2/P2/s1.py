from itertools import product

char = ["A", "E", "I", "O", "U"]
word_lst = []
for i in range(1, 6):
    for words in product(char, repeat=i):
        word_lst.append("".join(words))
word_lst.sort()

def solution(word):
    answer = word_lst.index(word)
    return answer + 1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))