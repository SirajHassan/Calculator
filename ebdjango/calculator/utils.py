from simpleeval import simple_eval

#input string of arithmatic. Output string of arithmatic with answer..
# will translate common arithmatic symbols (see operator_translations)
def calculate(s):  
    operator_translations = {'x':'*', '^':'**'} #translations to python
    lst = []
    result = ''
    n = len(s)
    
    #corner cases:
    if n == 0:
        return ""

    i = 0
    while i < n:
        if s[i] in operator_translations:
            lst.append(operator_translations[lst[i]])
        else:
            lst.append(s[i])
        i+=1
        
    try:
        result = str(simple_eval(''.join(lst))) #evaluates tranlated arithmatic
        return(result)
    except:
        return ("ERROR")


        

        

        

            

        

        
            


        
                
