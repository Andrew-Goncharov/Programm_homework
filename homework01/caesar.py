import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range (len(plaintext)):
        text = plaintext[i]
        if (text.isalpha()):
            if (text.isupper()):
                ciphertext += chr((ord(text) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(text) + shift - 97) % 26 + 97)
        else:
            ciphertext += text
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        text=ciphertext[i]
        if (text.isalpha()):
            if (text.isupper()):
                plaintext += chr((ord(text) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(text) - shift - 97) % 26 + 97)
        else:
            plaintext += text
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
