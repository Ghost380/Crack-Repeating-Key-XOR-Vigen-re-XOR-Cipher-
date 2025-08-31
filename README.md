# Repeating-Key XOR Cipher Breaker

This project provides a Python script to break a repeating-key XOR (Vigenère) cipher, commonly encountered as a cryptopuzzle. The algorithm works by analyzing the ciphertext to estimate the likely key sizes, then cracks each key byte using frequency analysis.

## Features

- **Key Size Guessing:** Estimates the most probable key sizes using normalized Hamming distance.
- **Single-Byte XOR Cracker:** Recovers each key byte using printable ASCII scoring.
- **Repeating-Key XOR Decryption:** Decrypts the ciphertext using the recovered key.
- **Base64 Input:** Accepts ciphertext as a base64-encoded string for easy input.

## Usage

1. **Install Python 3** if not already installed.
2. **Save the script** to a file, e.g. `break_xor.py`.
3. **Run the script:**
    ```bash
    python break_xor.py
    ```
4. **Paste your base64-encoded ciphertext** when prompted.

The script will:
- Guess likely key sizes,
- Attempt to recover the key,
- Output the candidate key and a plaintext sample for each key size.

## Example

```
Paste your base64-encoded ciphertext: HUIfTQsPAh9PE048GmllH0kc...
Candidate key size: 29
Recovered key: b'SECRETKEY'
Plaintext sample: b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal..."
```

## Dependencies

- Standard Python 3 library only (`base64`).

## How It Works

- **Key size estimation**: The script computes normalized Hamming distances between chunks of the ciphertext for each key size in a given range. The smallest averages are chosen as likely candidates.
- **Key recovery**: For each key byte position, the script solves a single-byte XOR problem using English character frequency.
- **Decryption**: The recovered key is used to decrypt the full ciphertext.


## License

MIT License 

