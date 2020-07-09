from collections import Counter

def word_count(s):
    wc = Counter()
    punct = '":;,.-+=/\|[]{(})*^&'
    for p in punct:
        s = s.replace(p, '')
    if s == '':
        return {}
    for word in s.lower().split():
        wc[word] += 1
    return wc


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))