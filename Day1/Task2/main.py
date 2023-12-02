import re
from unicodedata import name
result=0
array = []
digits = {
    k: v for v in "123456789" for k in [v, name(v).removeprefix("DIGIT ").lower()]
}
if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        for line in f:
            a, *_, b = re.findall(rf"(?=({'|'.join(digits)}))", 2 * line)
            result += int(digits[a] + digits[b])
        print(result)

