# Crypto Challenge - XOR Encryption Binary

Analysis of a basic cryptography challenge binary implementing XOR encryption.

## Binary Information

**File:** crypto_challenge  
**Type:** ELF 64-bit LSB executable  
**Stripped:** No  
**Security:** Partial RELRO, NX enabled, No PIE

## Functionality Overview

The binary implements a simple XOR-based encryption scheme. It reads input from the user and encrypts it using a repeating key.

## Key Findings

### 1. Encryption Algorithm

The binary uses a simple XOR cipher with a repeating key:

```c
void encrypt(char* data, int len, char* key, int keylen) {
    for (int i = 0; i < len; i++) {
        data[i] ^= key[i % keylen];
    }
}
```

### 2. Hardcoded Key

The encryption key is hardcoded in the binary at address `0x402020`:

```
Key: "SecretKey123"
Length: 12 bytes
```

### 3. Vulnerable Functions

The binary contains several potentially vulnerable functions:

- `gets()` - Buffer overflow vulnerability
- `strcpy()` - No bounds checking
- Stack-based buffer (256 bytes) without protection

## Exploitation Notes

### Buffer Overflow

The use of `gets()` allows for a classic buffer overflow:

1. Input buffer is 256 bytes
2. No bounds checking on input
3. Return address can be overwritten

### Proof of Concept

```bash
python -c 'print("A" * 264 + "\x41\x42\x43\x44")' | ./crypto_challenge
```

## Decryption

Since the key is known, encrypted data can be easily decrypted:

```python
def decrypt(data, key):
    result = []
    for i, byte in enumerate(data):
        result.append(byte ^ ord(key[i % len(key)]))
    return bytes(result)

encrypted = b"\x17\x00\x1d\x12..."
key = "SecretKey123"
plaintext = decrypt(encrypted, key)
```

## Recommendations

1. Replace `gets()` with `fgets()` or safer alternatives
2. Implement proper input validation
3. Use modern cryptographic libraries (e.g., OpenSSL)
4. Enable stack canaries and ASLR
5. Consider using a proper encryption algorithm (AES, ChaCha20)

## Conclusion

This binary demonstrates common vulnerabilities in cryptographic implementations and input handling. The combination of weak encryption and buffer overflow vulnerabilities makes it an excellent learning example for security researchers.

---

*Analysis date: 2025-11-02*
