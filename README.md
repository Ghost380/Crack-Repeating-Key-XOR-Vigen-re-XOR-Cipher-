Repeating-Key XOR Cipher Breaker
This Python script performs an automated cryptanalysis of repeating-key XOR ciphers. Given a base64-encoded ciphertext, it attempts to deduce the original key and decrypt the message.

How It Works
The script follows a three-step process to break the encryption:

Guess Key Length: The program first guesses a small set of probable key lengths. It does this by calculating the normalized Hamming distance between chunks of ciphertext. The key lengths that yield the lowest distances are the most likely candidates.

Crack Key Bytes: For each guessed key length, the script transposes the ciphertext blocks. Since each transposed block is encrypted with the same single byte of the key, it can be solved using frequency analysis, just like a single-byte XOR cipher.

Display Results: After solving for each byte of the key, the script assembles the full key. It then decrypts the ciphertext and prints the resulting plaintext for each candidate key, allowing the user to identify the correct one.

Usage
Save the script as a Python file (e.g., break_xor.py).

Run it from your command line:

python break_xor.py

When prompted, paste the base64-encoded ciphertext and press Enter. The script will output its findings.

Notes & Limitations
The character scoring function (single_byte_xor_crack) is basic. Its accuracy could be improved by using a more sophisticated scoring model based on English letter frequencies (e.g., giving higher scores to e, t, a, o, i, n and lower scores to j, q, x, z).

This tool assumes the underlying plaintext is printable ASCII (e.g., standard English text). It may not work correctly on binary data or text in other encodings.
