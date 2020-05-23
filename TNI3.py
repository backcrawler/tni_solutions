from operator import sub

dataset = [574, 9320, 4547, 1237, 36]
variants = (6174, 0)


def process_number(number: [str, int]) -> int:
    s_num = str(number)
    splitted = list(s_num)
    higher = ''.join(sorted(splitted, reverse=True))
    lower = ''.join(sorted(splitted, reverse=False))
    res = sub(*map(int, [higher, lower]))
    print(f'{higher} - {lower} = {res}')
    return res


def validate(num: [str, int]) -> str:
    length = len(str(num))
    if length > 4:
        raise ValueError('Too long')
    elif length < 4:
        s_num = str(num)
        step = 4 - length
        s_num = step * '0' + s_num
    else:
        s_num = str(num)
    return s_num


def main() -> dict:
    answers = {}
    for num in dataset:
        result = validate(num)
        counter = 1
        print(num)
        while True:
            result = process_number(result)
            if result in variants:
                answers[num] = counter
                break
            counter += 1
            if counter > 1000:
                raise ArithmeticError('Something went wrong')
        print('\n')
    return answers


if __name__ == '__main__':
    answers = main()
    print(answers)