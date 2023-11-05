def diamond(n):
    if type(n) is int:
        if n<0:
            return("Please input a valid size")
        elif n%2==0:
            return("Please input a valid size")
        else:
            import math
            diamonds_on_row=1
            diamond_row=''
            diamond=''
            for row in range(1,n+1):
                gap=(int((n-diamonds_on_row)/2))
                for i in range(gap):
                    diamond+=' '
                for i in range(diamonds_on_row):
                    diamond+='*'
                diamond+='\n'
                if row<math.ceil(n/2):
                    diamonds_on_row+=2
                else:
                    diamonds_on_row-=2
            return(diamond)
    else:
        return(None)

def make_diamond(size):
    while True:
        try:
            print(diamond(int(size)))
        except ValueError:
            print("Please input a valid size")
        else:
            break
        
size=input('Input the size of the diamond:')

make_diamond(size)