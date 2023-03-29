def douhao(spams):
    if len(spams) == 0:
        return''
    elif len(spams) == 1:
        return spams[0]
    else:
        return ','.join(spams[:-1])+',and '+spams[-1]


spams = ['apple', 'banana', 'tofu', 'cats']
print(douhao(spams))
