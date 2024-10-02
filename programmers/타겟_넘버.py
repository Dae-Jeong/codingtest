from collections import deque


def target_number(numbers, target):
    count = 0  # count 변수를 선언하고 초기화

    def dfs(idx, value):
        nonlocal count
        if (idx == len(numbers)) and (value == target):
            count += 1
            return

        elif idx == len(numbers):
            return

        dfs(idx=idx+1, value=value+numbers[idx])
        dfs(idx=idx+1, value=value-numbers[idx])

    dfs(idx=0, value=0)
    return count


print(target_number(numbers=[1, 1, 1, 1, 1], target=3))


