import itertools as it

def decrypt(message, key):
    message_iter = iter(message)
    key_iter = it.cycle(key)
    result = []
    for _ in message:
        result.append(exec_decrypt(next(message_iter), key_iter))
    return bytes(result)