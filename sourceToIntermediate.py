c=1 
def g(e): 
    global c 
    e=e.strip() 
    if e.isalnum(): return e 
    for o in '+-*/': 
        d=0 
        for i in range(len(e)-1,-1,-1): 
            if e[i]==')': d+=1 
            elif e[i]=='(': d-=1 
            elif d==0 and e[i]==o: 
                l,r=g(e[:i]),g(e[i+1:]) 
                t=f"t{c}"; print(f"{t}={l}{o}{r}"); c+=1 
                return t 
    return g(e[1:-1]) 
 
x,y=input("Enter Source Code: ").split('=',1) 
print("Three Address Code:") 
print(f"{x}={g(y)}") 