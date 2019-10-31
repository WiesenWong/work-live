import sys
 
FONTCOL=6
FONTROW=7

zero=("------",
      "  **  ",
      " *  * ",
      " *  * ",
      " *  * ",
      "  **  ",
      "------")
 
one= ("------",
      "   *  ",
      "  **  ",
      "   *  ",
      "   *  ",
      "  *** ",
      "------")
 
two= ("------",
      "  **  ",
      " *  * ",
      "   *  ",
      "  *   ",
      " **** ",
      "------")
 
three=("------",
       "  **  ",
       " *  * ",
       "   ** ",
       " *  * ",
       "  **  ",
      "------")
 
four= ("------",
       "   *  ",
       "  **  ",
       " * *  ",
       " **** ",
       "   *  ",
      "------")
 
five= ("------",
       " **** ",
       " *    ",
       " **** ",
       "    * ",
       " **** ",
      "------")
 
six=  ("------",
       "  **  ",
       " *    ",
       " ***  ",
       " *  * ",
       "  **  ",
      "------")
 
seven=("------",
       "  *** ",
       " *  * ",
       "   *  ",
       "   *  ",
       "  *** ",
      "------")
 
eight=("------",
       "  **  ",
       " *  * ",
       "  **  ",
       " *  * ",
       "  **  ",
      "------")
 
nine= ("------",
       "  **  ",
       " *  * ",
       "  *** ",
       "    * ",
       "  **  ",
       "------")
	   
digits=(zero,one,two,three,four,five,six,seven,eight,nine) #将所有数字字模合成一个元组

def getDigits():
    print('')
    for digit in digits:
        for symbol in digit:
            if
def show_number(nums):
    i=0
    while i<FONTROW:
        col=0
        while col<len(nums): #此处输出全部字模
            print(digits[int(nums[col])][i],end=" ")
            col+=1
        print("") #换行，输出字模下一行
        i+=1
 
def show_usage():
    show_number('1024')
    getDigits()

if __name__ == '__main__':
    if len(sys.argv)==2:
        show_number(sys.argv[1])
    else:
        show_usage()#如果未提供参数或提供的参数过多，则输出使用说明