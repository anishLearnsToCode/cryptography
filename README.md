# Cryptography & Network Security 
__~Behrouz A. Forouzan__ 

![made-with-python](https://img.shields.io/badge/Made%20with-Python%203-1f425f.svg)

Algorithms from the book Cryptography & Network Security ~Behrouz A. Forouzan. See book 📗
[here](https://github.com/anishLearnsToCode/books/blob/master/cryptography/Cryptography-and-Network-Security-Forouzan.pdf).

## 📖 Index
- [Mathematics of Cryptography](#-mathematics-of-cryptography)
- [Traditional Symmetric-Key Ciphers](#-traditional-symmetric-key-ciphers)
- [Mathematics of Cryptography: Algebraic Structures](#-mathematics-of-cryptography-algebraic-structures)
- [Introduction to Modern Symmetric Key Ciphers](#-introduction-to-modern-symmetric-key-ciphers)
- [Data Encryption Standard (DES)](#-data-encryption-standard-des)

## 🧮 [Mathematics of Cryptography](notebooks/2-mathematics-of-cryptography.ipynb)
1. Euclid's Algorithm
1. Extended Euclid's Algorithm
1. Diophantine's Equation
1. Additive Inverse
1. Multiplicative Inverse
1. Solutions to Single Variable Linear Equations

## 🔑 [Traditional Symmetric Key Ciphers](notebooks/3-symmetric-key-ciphers.ipynb)
1. Monoalphabetic Ciphers
    1. [Caesar Shift Cipher](ciphers/CaesarShiftCipher.py)
    1. [Multiplicative Cipher](ciphers/MultiplicativeCipher.py)
    1. [Affine Cipher](ciphers/AffineCipher.py)
1. Polyalphabetic Ciphers
    1. [Autokey Cipher](ciphers/AutoKeyCipher.py)
    1. [Playfair Cipher](ciphers/PlayfairCipher.py)
    1. [Vignere Cipher](ciphers/VignereCipher.py)
    1. [Hill Cipher](ciphers/HillCipher.py)
    1. [One Time Pad Cipher](ciphers/OneTimePadCipher.py)
1. Transposition Ciphers
    1. Keyless Transposition Ciphers 
        1. [Column Transposition Cipher](ciphers/ColumnTranspositionCipher.py)
        1. [Row Transposition Cipher](ciphers/RowTranspositionCipher.py)
        1. [Rail Fence Transposition Cipher](ciphers/RailFenceCipher.py)
    1. Key Based Transposition Ciphers
        1. [Keyed Transposition Cipher](ciphers/KeyedTranspositionCipher.py)
        1. [Columnar Transposition Cipher](ciphers/ColumnarTranspositionCipher.py)
    
## ➕ [Mathematics Of Cryptography: Algebraic Structures](notebooks/4-mathematics-cryptography-algebraic-structures.ipynb)
1. [The Permutation Group](mathematics/permutation.py)
1. [The Galois Field GF(2^n)](mathematics/Polynomial.py)

## 🔐 [Introduction To Modern Symmetric Key Ciphers](notebooks/5-introduction-to-modern-symmetric-key-ciphers.ipynb)
1. [P Boxes](mathematics/PBox.py)
1. [Feistel Mixer Cipher](ciphers/FiestelMixerCipher.py)
1. [One Round of a Feistel Cipher](ciphers/Round.py)
1. [Multiple Round Fiestel Cipher](ciphers/FiestelCipher.py)

## 💳 [Data Encryption Standard (DES)](notebooks/6-data-encryption-standard-des.ipynb)
1. [Permutation Box](mathematics/PBox.py)
1. [Substitution Box](mathematics/SBox.py)
1. [Swapper](des/Swapper.py)
1. [Mixer](des/Mixer.py)
1. [Single Fiestel Round](des/Round.py)
1. [DES - Data Encryption Standad Algorithm](des/DES.py)
