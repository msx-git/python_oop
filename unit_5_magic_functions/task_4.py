from string import ascii_lowercase


class CeaserCipher:
    def __init__(self, key):
        self.key = key
        inputAlphabet = ascii_lowercase
        encryptedAlphabet = inputAlphabet[-key:] + inputAlphabet[: -key]
        self.mapping = dict(zip(inputAlphabet, encryptedAlphabet))
        self.reverseMapping = dict(zip(encryptedAlphabet, inputAlphabet))

    def printMapping(self):
        for key, value in self.mapping.items():
            print(f'{key} -> {value}')

    def __call__(self, text):
        encryptedText = ''
        for letter in text:
            encryptedText += self.mapping.get(letter, '')
        return encryptedText

    def decrypt(self, text):
        decryptedText = ''
        for letter in text:
            decryptedText += self.reverseMapping.get(letter, '')
        return decryptedText


c1 = CeaserCipher(3)

text = 'hello'

# encrypt
print(c1(text))

# decrypt
print(c1.decrypt(text))
