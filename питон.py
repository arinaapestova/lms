def solution(n: int):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if max(a, b, c) + min(a, b, c) == 2 * \
    ((a + b + c) - max(a, b, c) - min(a, b, c)):
        print('YES')
    else:
        print('NO')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
