from collections import deque


def convert_words(begin, target, words):
    if target not in words:
        return 0

    word_length = len(target)

    def count_duplicate_words(word, change):
        diff = 0

        for i in range(word_length):
            if word[i] != change[i]:
                diff += 1

        if diff == 1:
            return True
        return False

    q = deque()
    q.append([begin, 0])

    while q:
        cur_word, cur_count = q.popleft()

        if cur_word == target:
            return cur_count

        for change_word in words:
            if count_duplicate_words(cur_word, change_word):
                q.append([change_word, cur_count+1])

    return 0


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]

    count = convert_words(begin, target, words)
    print(count)
