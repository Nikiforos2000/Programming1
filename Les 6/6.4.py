def new_password(oldpassword,newpassword):
    for cijfers in newpassword:
        if cijfers in '0123456789':
            cijfergevonden = True
        else:
            cijfergevonden = False
    if newpassword != oldpassword and len(newpassword) >= 6 and cijfergevonden:
        return ('Je wachtwoord is gewijzigd')
    else:
        return ('Sorry jouw wachtwoord voldoet niet aan de eisen')


oldpassword = input('Wat is je oude password: ')
newpassword = input('Wat is je nieuwe password: ')
print(new_password(oldpassword, newpassword))