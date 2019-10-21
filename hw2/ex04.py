def get_most_frequent(words, k):
    unique_words = set(words)
    main_list = []
    for word in unique_words:
        main_list.append([word, words.count(word)])
    main_list.sort(key=lambda x: x[1], reverse=True)
    return [main_list[i][0] for i in range(k)]


if __name__ == '__main__':
    print(get_most_frequent(["hello", "world", "hello", "my", "dear", "world", "hello"], 3))
