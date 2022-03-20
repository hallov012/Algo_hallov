import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
pokemon_name = {}
pokemon_num = {}
for i in range(n):
    pokemon = input().strip()
    pokemon_name[pokemon] = i+1
    pokemon_num[i+1] = pokemon
for _ in range(m):
    question = input().strip()
    try:
        print(pokemon_name[question])
    except:
        print(pokemon_num[int(question)])