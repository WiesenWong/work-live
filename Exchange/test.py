import binascii
source_path = r'C:\Users\wiwang\Downloads\python-3.8.0.exe'
target_path = r'C:\Users\wiwang\Desktop\test_case_1.txt'
target_path2 = r'C:\Users\wiwang\Desktop\test_case_2.txt'
import gzip

def main():
    '''
    f = open(source_path,"rb")
    outfile = open(target_path,"wb")
    c = f.read()
    print(binascii.b2a_hex(c))
    
    while 1:
        c = f.read(1)
        i = i + 1
        if not c:
            break
        if i%32 == 0:
            #outfile.write(b"\n")
            print("")
        else:
            if ord(c) <= 15:
                b = (hex(ord(c))[2:])[2:]
            else:
                b = (hex(ord(c)))[2:]
            a = bytes(b, 'utf-8')
            outfile.write(c)
        
    
    while 1:
        c = f.read(1)
        if not c:
            break
        else:
            print(c)
            outfile.write(c)
    outfile.close()
    f.close()
     
    b = b'\xf7'
    c = binascii.b2a_hex(b)
    print(c)
    print(binascii.a2b_hex(c))
    '''
    f = open(source_path,"rb")
    outfile = open(target_path,"wb")
    outfile2 = open(target_path2,"wb")
    i = f.read()
    o = gzip.compress(i)
    outfile.write(o)
    outfile2.write(gzip.decompress(o))
    outfile.close()
    outfile2.close()
if __name__=="__main__":
    main()