morse_base = [
    ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
    "..-","...-",".--","-..-","-.--","--.."
]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
morse_dict = dict(zip(alphabet,  morse_base))


def count_unique_codes(words):
    encrypted_message = set()
    for word in words:
        code = ''
        for c in word:
            code += morse_dict[c]
        encrypted_message.add(code)

    return len(encrypted_message)


if __name__ == '__main__':
    print(count_unique_codes(["gin", "zen", "gig", "msg"]))
