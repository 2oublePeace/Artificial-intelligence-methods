from timeit import default_timer as timer


def linear_search(data, search_word):
    isFound = False
    for word in data:
        if search_word == word:
            isFound = True
            break

    return isFound


def linear_search_analyzer(data, search_word):
    start = timer()
    isFound = linear_search(data=data, search_word=search_word)
    if isFound:
        result = f"Линейный поиск: {search_word} существует\n"
    else:
        result = f"{search_word} не существует\n"
    end = timer()

    result += f"Потрачено: {(end - start):.6f} секунд\n\n"
    return result
