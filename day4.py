import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return ''.join([('%02x' % ord(c)) for c in m.digest()])

def mine(secret):
    i = 1
    while True:
        if md5(secret + str(i))[:6] == '000000':
            return i
        i += 1
        if i % 100000 == 0:
            print i

def main():
    #assert mine('abcdef') == 609043
    #assert mine('pqrstuv') == 1048970
    print mine('bgvyzdsv')
    
main()

'bgvyzdsv'
