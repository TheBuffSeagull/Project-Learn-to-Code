import re

#change this to test effectiveness
_name = 'Trainee'

def is_Trainee(Trainee):

    if re.match("^Trainee(_\d\d)?$", Trainee):
        return True
    else:
        return False


print(is_Trainee(_name))