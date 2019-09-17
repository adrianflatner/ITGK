import binascii
import random

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)


def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def binary(msg):
    msg = bytes(msg, encoding = 'ascii')
    return msg

def encrypt(message,key):
    m = toHex(binary(message))
    k = toHex(binary(key))
    c = m^k
    return c


def decrypt(code,key):
    k = toHex(binary(key))
    m = code^k
    return toString(m)


def main():

    message = input("Melding: ")
    #key = input("Nøkkel: ")
    word = "abcdefghijklmnopqrstuvwxyz "
    key = ''.join(random.sample(word,len(word)))
    key = (key[:len(message)])

    print("Random nøkkel:", key)
    print("Kryptert:",encrypt(message,key))
    print("Dekryptert:",decrypt(encrypt(message,key),key))

main()

