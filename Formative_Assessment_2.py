#!/usr/bin/env python
# coding: utf-8

# # Programming Set 2
# ## This assignment will develop your proficiency with Python's control flows.

# # Shift Letter (4/4)

# In[49]:


def shift_letter(letter, shift):
    letter = (str(letter)).upper()
    shift = int(shift)
    if letter == " ":
        result = " "
    else:
        #find ascii code then modulo for exceeding values, add to A value to find final result
        result = chr((ord(letter) - ord('A') + shift) % 26 + ord('A')) 
    return result


# # Caesar Cipher (4/4)

# In[57]:


def caesar_cipher(message, shift):
    message = (str(message)).upper()
    shift = int(shift)
    i = 0
    result = ""
    while i < len(message):
        if message[i] == " ":
            new = " "
        else:
            new = chr((ord(message[i]) - ord('A') + shift) % 26 + ord('A'))
        i += 1
        result += new
    return result


# # Shift by Letter (4/4)

# In[ ]:


def shift_by_letter(letter, letter_shift):
    letter = str(letter)
    letter_shift = str(letter_shift)
    shift_value = int(ord(letter_shift) - ord("A"))
    if letter == " ":
        result = " "
    else:
        result = chr((ord(letter) - ord("A") + shift_value) % 26 + ord("A"))
    return result


# # Vigenere Cipher (4/4)

# In[62]:


def vigenere_cipher(message, key):
    message = str(message)
    key = str(key)
    new_key = ""
    length = len(message)
    result = ""
    if len(key) < len(message):
        reruns = len(message) // len(key)
        excess = len(message) % len(key)
        for i in range(0, reruns):
            new_key += key
        if excess > 0:
            for j in range(0, excess):
                new_key += key[j]
    for k in range(0, length):
        shift_value = int(ord(new_key[k]) - ord("A"))
        if message[k] == " ":
            new = " "
            result += new
            continue
        else:
            new = chr((ord(message[k]) - ord("A") + shift_value) % 26 + ord("A"))
            result += new
            continue
    return result


# # Scytale Cipher (4/4)

# In[245]:


def scytale_cipher(message, shift):
    message = str(message)
    shift = int(shift)
    length = len(message)
    new_message = ""
    result = ""
    while length % shift != 0:
        message += "_"
        length = len(message)
    for i in range(length):
        new = message[(i // shift) + (len(message) // shift) * (i % shift)]
        result += new
    return result


# # Scytale De-cipher (4/4)

# In[247]:


def scytale_decipher(message, shift):
    num_rows = len(message) // shift
    if len(message) % shift != 0: #extra row for modulo excess
        num_rows += 1

    decoded_message = [''] * len(message) #create emptry string

    for i in range(len(message)): #find position

        row = i // shift
        col = i % shift

        original_index = col * num_rows + row

        if original_index < len(message):
            decoded_message[original_index] = message[i]

    return ''.join(decoded_message) #honestly i just learned what ' '.join was just for this item :(

