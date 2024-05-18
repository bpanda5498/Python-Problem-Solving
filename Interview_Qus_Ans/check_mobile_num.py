import re
mob_num=input('Enter your mobile number:')
match_mob=re.fullmatch('[6-9]\d{9}',mob_num)
if match_mob != None:
    print(mob_num,'Valid Mobile Number')
else:
    print(mob_num,'Invalid Mobile Number')