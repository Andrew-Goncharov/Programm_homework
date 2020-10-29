def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    letter_option = ""
    number_option = []
    if (len(keyword) < len(plaintext)):
        for i in range(len(plaintext)):
            letter_option += keyword[i % len(keyword)]
    else:
        letter_option = keyword
    for i in range(len(letter_option)):
        if (letter_option[i].isupper()):
            number_option.append(ord(letter_option[i]) - 65)
        if (letter_option[i].islower()):
            number_option.append(ord(letter_option[i]) - 97)

    for i in range(len(plaintext)):
        text = plaintext[i]
        if (text.isalpha()):
            if (text.isupper()):
                ciphertext += chr((ord(text) + number_option[i] - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(text) + number_option[i] - 97) % 26 + 97)
        else:
            ciphertext += text
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    letter_option = ""
    number_option = []
    if (len(keyword) < len(ciphertext)):
        for i in range(len(ciphertext)):
            letter_option += keyword[i % len(keyword)]
    else:
        letter_option = keyword
    for i in range(len(letter_option)):
        if (letter_option[i].isupper()):
            number_option.append(ord(letter_option[i]) - 65)
        if (letter_option[i].islower()):
            number_option.append(ord(letter_option[i]) - 97)

    for i in range(len(ciphertext)):
        text = ciphertext[i]
        if (text.isalpha()):
            if (text.isupper()):
                plaintext += chr((ord(text) - number_option[i] - 65) % 26 + 65)
            else:
                plaintext += chr((ord(text) - number_option[i] - 97) % 26 + 97)
        else:
            plaintext += text
    return plaintext
