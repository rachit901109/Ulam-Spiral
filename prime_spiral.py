from colorama import Fore,Style
r = 100
c = 100
ri,ci = 0,0
li = [[" "]*c for i in range(r)]
k = r*c

def isprime(n)-> bool:
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i==0:
            return False
    return True

while ri<r and ci<c:
    for i in range(ri,r):
        if isprime(k):
            li[ri][i]=Fore.GREEN+'*'+Style.RESET_ALL
            # li[ri][i]=str(k)
        else:
            li[ri][i]='-'
        k-=1
    ri+=1
    for j in range(ri,c):
        if isprime(k):
            li[j][c-1] = Fore.GREEN+'*'+Style.RESET_ALL
            # li[j][c-1]=str(k)
        else:
            li[j][c-1]='|'
        k-=1
    c-=1
    if ri < r:
        for i in range(c-1,ci-1,-1):
            if isprime(k):
                li[r-1][i] = Fore.GREEN+'*'+Style.RESET_ALL
                # li[r-1][i]=str(k)
            else:
                li[r-1][i]='-'
            k-=1
    r-=1
    if ci < c:
        for j in range(r-1,ri-1,-1):
            if isprime(k):
                li[j][ci]=Fore.GREEN+'*'+Style.RESET_ALL
                # li[j][ci]=str(k)
            else:
                li[j][ci]='|'
            k-=1
    ci+=1

for i in li:
    for j in i:
        print(j,end='\t'.expandtabs(1))
    print(sep="")
