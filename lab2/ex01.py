def speak_excitedly(text, exclamation_count=0, capitalize=False):
    if capitalize:
        out = text.upper()
    else:
        out = text

    for i in range(exclamation_count):
        out += '!'

    print(out)


if __name__ == '__main__':
    speak_excitedly('Let\'s go stanford', exclamation_count=2, capitalize=True)