import math


def main():
    try:
        n = int(input('input n = '))
    except Exception as e:
        print(f'Error: n = integer')
        print(e)
        return None

    if n > 100 or n < 2:
        print(f'Error: 2 <= n <= 100')
        return None

    P = int(n * (n - 1) / 2)

    try:
        mode = int(input(f'The answer to what question? ( 1 or 2 ): '))
    except Exception as e:
        print(f'Error: questions = integer')
        print(e)
        return None

    if 1 == mode:
        try:
            k = int(input(f'input k = '))
        except Exception as e:
            print(f'Error: k = integer')
            print(e)
            return None

        print(f'Different networks with n unique instances and k connections = {math.comb(P, k)}')

    if 2 == mode:
        try:
            p = float(input(f'input p = '))
        except Exception as e:
            print(f'Error: p = float')
            print(e)
            return None

        if p < 0 or p > 1:
            print(f'Error: 0 <= p <= 1')
            return None

        k = n - 1
        p_avg = (n ** (n - 2) / math.comb(P, k)) * p ** k * (1 - p) ** (P - k)

        print(f'The probability that the resulting network will not have cyclic connections, '
              f'but will still be connected = {p_avg}')

    else:
        return None


if __name__ == '__main__':
    main()
