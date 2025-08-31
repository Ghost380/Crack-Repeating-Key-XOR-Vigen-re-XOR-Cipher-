import base64

def hamming_distance(b1, b2):
    """Compute the Hamming distance (number of differing bits) between two byte strings."""
    return sum(bin(x ^ y).count('1') for x, y in zip(b1, b2))

def guess_key_sizes(cipher_bytes, min_size=2, max_size=40, num_candidates=3):
    """Guess likely key sizes by comparing normalized distances between blocks"""
    averages = []
    for key_size in range(min_size, max_size + 1):
        blocks = [cipher_bytes[i:i+key_size] for i in range(0, len(cipher_bytes), key_size)]
        num_blocks = min(4, len(blocks) - 1)
        if num_blocks <= 1:
            continue
        distances = [
            hamming_distance(blocks[i], blocks[i+1])/key_size
            for i in range(num_blocks)
        ]
        avg = sum(distances) / len(distances)
        averages.append((key_size, avg))
    # Return key sizes with the lowest distances
    return sorted(averages, key=lambda x: x[1])[:num_candidates]

def single_byte_xor_crack(block):
    """Find the most likely single-byte key by scoring decoded block"""
    candidates = []
    for k in range(256):
        decoded = bytes([b ^ k for b in block])
        score = sum(chr(b).isprintable() and chr(b).isascii() for b in decoded)
        candidates.append((k, score))
    return max(candidates, key=lambda x: x[1])[0]

def break_repeating_key_xor(cipher_bytes, key_size):
    """Recover the full key by solving each key byte independently"""
    blocks = [cipher_bytes[i::key_size] for i in range(key_size)]
    key = bytes([single_byte_xor_crack(block) for block in blocks])
    return key

def xor_decrypt(cipher_bytes, key):
    """Decrypt ciphertext with repeating key"""
    return bytes([c ^ key[i % len(key)] for i, c in enumerate(cipher_bytes)])

def main():
    # Example: ciphertext as base64 string
    base64_ciphertext = input("Paste your base64-encoded ciphertext: ")
    cipher_bytes = base64.b64decode(base64_ciphertext)

    # Guess best key sizes
    key_sizes = guess_key_sizes(cipher_bytes)
    for key_size, _ in key_sizes:
        key = break_repeating_key_xor(cipher_bytes, key_size)
        plaintext = xor_decrypt(cipher_bytes, key)
        print(f"\nCandidate key size: {key_size}")
        print(f"Recovered key: {key}")
        print(f"Plaintext sample: {plaintext[:200]}\n")
        # Optionally: present the full decoded text if desired

if __name__ == '__main__':
    main()
