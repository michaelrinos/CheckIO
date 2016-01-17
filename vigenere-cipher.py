"""
 The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

In the Vigenère cipher each letter of a message is shifted along some number of places with different shift values. To encrypt, a table of alphabets can be used, termed a tabula recta, Vigenère square, or Vigenère table. It consists of the alphabet written out 26 times in different rows, each version of the alphabet is shifted cyclically to the left compared to the previous alphabet. At different points in the encryption process, the cipher uses a different alphabet from one of the rows. The alphabet used at each point depends on a repeating keyword.

To see how this works, lets take, the message "DONTWORRYBEHAPPY" and the keyword "CHECKIO". Write the message and the keyword below, then shift each letter in the message related by corresponded letter in the repeating keyword.

Message:   DONTWORRYBEHAPPY
Key:       CHECKIOCHECKIOCH
Encrypted: FVRVGWFTFFGRIDRF

Vigenère can also be viewed algebraically. If the letters A–Z are taken to be the numbers 0–25, and addition is performed modulo 26, then Vigenère encryption E using the key K can be written as:
Ci = Ek(Mi) = (Mi + Ki) % 26

Now, consider the following scenario: you and your friend use that cipher for correspondence and you've forgot the key. But, to your luck, you have an archive with encrypted and decrypted message. With that you can find the key and decrypt the new fresh message from your friend.

Input: Three arguments. An old decrypted message, an old encrypted message and a new encrypted message as strings (unicode for py2).

Output: The new decrypted message as a string.

Precondition:
all(re.match("[A-Z]+\Z", text) for text in args)
len(key) ≤ len(old_encrypted)
2 * len(key) <= len(old_encrypted) < len(new_encrypted) or len(new_encrypted) <= len(old_encrypted)
"""

from string import *
def convert(string):
    x = []
    for i in string:
        x.append(str(ascii_uppercase.index(i)))
    return x
    

def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    x = convert(old_encrypted)          #converts letters to numbers
    y = convert(old_decrypted)
    z = convert(new_encrypted)
    
    a = ""                              #gets the unfiltered key
    for i in range(len(x)):
        a += ascii_uppercase[int(x[i])-int(y[i])]
    
    
    
    mod = len(a)                        #gets the length of the key
    for i in range(len(a)-2, 1 , -1):
        if a.count(a[i+1])==1:
            mod = len(a)
            break
        if a[i] == a[0]:
            if a[i+1] == a[1]:
                mod = i
                break
    
    result = "" 
    for i in range(len(z)):             #decodes the new message
        result+=ascii_uppercase[int(z[i])-ascii_uppercase.index(a[i%mod])]
    
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
    
    assert decode_vigenere(u"AAAAAAAAA", u"ABABABABC", u"ABABABABC") == "AAAAAAAAA"
                           
    assert decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT", u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI", u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL") == "IMALUMBERJACKANDIMOKISLEEPALLNIGHTANDIWORKALLDAYICUTDOWNTREESISKIPANDJUMPILIKETOPRESSWILDFLOWERSIPUTONWOMENSCLOTHINGANDHANGAROUNDINBARS" 
    
    
    assert decode_vigenere("NOBODYEXPECTSTHESPANISHINQUISITION", "PVFQNGSZWIEDAHJLWRKVWUOMPACWUPXKYV", "QBVGHXSTAWFOAQTPFGIWICZEPKXDCSPKXOZAKYNVNSNSSYEVWOHKKXIHKCIVSUWFSEEUQBIPRKXQHKHXKFMGRPRGVMGULEUSTMFVQKXIHGKRQCMBULSHRCAQBVVOLWQBWEYUDCUCCXLWTYIRBMGUPFNILFCIEPNIKHBPCXLKJLVGKAWPTSUDXFQMIUCQCPZXJOASYVYNNJSEVRUSLSTHFNOLFCDFCMSGKUGJKZHGYIFKKQQBRVKVQAALGIIFGHTQCQHKCIDYWB") == "OUREXPERTSDESCRIBEYOUASANAPPALLINGLYDULLFELLOWUNIMAGINATIVETIMIDLACKINGININITIATIVESPINELESSEASILYDOMINATEDNOSENSEOFHUMOURTEDIOUSCOMPANYANDIRREPRESSIBLYDRABANDAWFULANDWHEREASINMOSTPROFESSIONSTHESEWOULDBECONSIDERABLEDRAWBACKSINCHARTEREDACCOUNTANCYTHEYAREAPOSITIVEBOON"
     
