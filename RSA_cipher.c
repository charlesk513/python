e, n = 17, 1271
mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,' ': 27, '.': 28, ',': 29}
text = "as kabunga charles in bcs, i love cryptography and so i rate discrete ten out of ten".lower()
cipher_texts = [pow(mapping[ch], e, n) for ch in text]
print(','.join(str(c) for c in cipher_texts))
