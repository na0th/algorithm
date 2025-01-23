'''
N개의 단어 정렬.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기기.

'''
import sys
input = sys.stdin.readline

n = int(input())

words = set()
for _ in range(n):
    words.add(input().strip())
words = list(words)
# print(words)
words.sort(key=lambda x:(len(x),x))
for word in words:
    print(word)
# print(words)