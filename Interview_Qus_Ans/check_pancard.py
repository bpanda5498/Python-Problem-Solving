import re
pancard=input('Enter your pancard number:')
match_pc=re.fullmatch('[A-Z]{5}\d{4}[A-Z]{1}',pancard)
if match_pc != None:
    print(pancard,'Valid Pan Card')
else:
    print(pancard,'Invalid Pan Card')