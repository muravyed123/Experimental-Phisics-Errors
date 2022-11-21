from sympy import*
from math import*
import re
def give_pogr(func,sym,pog):
    df = 0
    for i in range(len(sym)):
        list(sym)[i] = symbols(list(sym)[i])
    for i in range(len(sym)):
        expr = diff(func,list(sym)[i])
        #print(expr)
        val = expr.evalf(subs = sym)
        df += (val*pog[i])**2
    return(sqrt(df))
def give_result(func,sym):
    return(float(parse_expr(func).evalf(subs = sym)))
def rep_f(func,s,zam):
    return(func.replace(s,'('+zam+')'))
def repinst(func,sym):
    for i in range(len(sym)-1,-1,-1):
        func = rep_f(func,list(sym)[i],sym[list(sym)[i]])
    return(func)
def symbols_from_expr(expr_str: str, pattern=r"[A-Za-z]\d{,2}") -> tuple:
    symbols_set = set(re.findall(pattern, expr_str))
    symbols_set = sorted(symbols_set)
    symbols_list = tuple(symbols(symbols_set))
    return symbols_list
def check_s(func,sym):
    list_of_s = symbols_from_expr(func)
    for i in range(len(list_of_s)):
        try :
            m = sym[str(list_of_s[i])]
        except KeyError:
            return(False)
    else:
        return(True)
#un = input()
sym = {}
#1- символ,2 -значение
#1 - абсолютная погрешность
pogr = []

#n = int(input())
#for i in range(n):
    #a = list(map(str,input().split()))
    #sym[a[0]] = a[1]
    #pogr.append(float(a[2]))
#print(give_result(fun,sym),'+-',give_pogr(fun,sym,pogr))