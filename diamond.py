def diamond(n):
    if type(n) is int:
        if n<0:
            return(None)
        elif n%2==0:
            return(None)
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






    




print(diamond(13))
