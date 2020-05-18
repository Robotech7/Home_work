def stronger(scores):
    result = 0
    for x, item in enumerate(scores):
        try:
            if item < scores[x+1]:
                result += 1
        except IndexError:
            break
    return result

stronger([10, 5, 20, 20, 4, 5, 2, 25, 1,])