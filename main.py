from random import randrange, choice


def level_selection():
    while True:
        print('Which level do you want? Enter a number:')
        print(f'1 - {levels_dict[1]}\n2 - {levels_dict[2]}')

        try:
            answer = int(input())

            if 1 <= answer <= 2:
                return answer
            else:
                print('Incorrect format.')
        except ValueError:
            print('Incorrect format.')


def check_input():
    while True:
        try:
            your_int = int(input())
            return your_int
        except ValueError:
            print('Incorrect format.')


def first_level():
    global mark

    for _ in range(5):
        x, operation, y = randrange(2, 10), choice(['+', '-', '*']), randrange(2, 10)
        print(x, operation, y)

        answer = check_input()

        if answer == eval(f'{x} {operation} {y}'):
            mark += 1
            print('Right!')
        else:
            print('Wrong!')


def second_level():
    global mark

    for _ in range(5):
        x = randrange(11, 30)
        print(x)

        answer = check_input()

        if answer == x ** 2:
            mark += 1
            print('Right!')
        else:
            print('Wrong!')


def saving_the_result(answer, level):
    if answer in ['yes', 'YES', 'y', 'Yes']:
        user_name = input('What is your name?\n')

        with open('results.txt', 'a') as f:
            f.write(f'{user_name}: {mark}/5 in level {level} ({levels_dict[level]}).\n')

        print('The results are saved in "results.txt".')


def main():
    level = level_selection()
    first_level() if level == 1 else second_level()
    answer = input(f'Your mark is {mark}/5. Would you like to save your result to the file? Enter yes or no.\n')
    saving_the_result(answer, level)


mark = int()
levels_dict = {1: 'simple operations with numbers 2-9', 2: 'integral squares of 11-29'}


if __name__ == '__main__':
    main()
