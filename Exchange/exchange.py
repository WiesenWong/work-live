import binascii
import gzip
import Huffman
'''
def a2b(source_path,target_path):
    infile = open(source_path,"rb")
    outfile = open(target_path,"wb")
    
    while 1:
        i = infile.read(2)
        if not i:
            break
        else:
            o = binascii.a2b_hex(i)
            outfile.write(o)
    outfile.close()
    infile.close()

def b2a(source_path,target_path):
    infile = open(source_path,"rb")
    outfile = open(target_path,"wb")
    
    while 1:
        i = infile.read(1)
        if not i:
            break
        else:
            o = binascii.b2a_hex(i)
            outfile.write(o)
    outfile.close()
    infile.close()
'''


def b2a_fast(open_file):
    infile = open_file[0]
    outfile = open_file[1]
    i = infile.read()
    o = binascii.b2a_hex(gzip.compress(i))
    print(len(i))
    print(len(o))
    outfile.write(o)
    outfile.close()
    infile.close()

def a2b_fast(open_file):
    infile = open_file[0]
    outfile = open_file[1]
    i = infile.read()
    o = gzip.decompress(binascii.a2b_hex(i))
    outfile.write(o)
    outfile.close()
    infile.close()

def open_file(source_path,target_path):
    infile = open(source_path,"rb")
    outfile = open(target_path,"wb")
    return [infile,outfile]  
    
if __name__=="__main__":
    source_path = r'C:\Users\wiwang\Desktop\File\UDM-pic\test_case_1.png'
    target_path = r'C:\Users\wiwang\Desktop\est_case_1.txt'
    h = Huffman.Huffman()
    h.compress(source_path,target_path)
    #b2a_fast(open_file(source_path,target_path))
    
    #source_path = r'C:\Users\wiwang\Desktop\python-3.8.0.txt'
    #target_path = r'C:\Users\wiwang\Desktop\python-3.8.0.exe'
    #a2b_fast(open_file(source_path,target_path))