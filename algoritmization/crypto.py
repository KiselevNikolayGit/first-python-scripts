from Crypto.Cipher import XOR

key = input('The key: ')
cipher = XOR.new(key)
text = input('The text: ')

cipher.encrypt('.res: ' + text)