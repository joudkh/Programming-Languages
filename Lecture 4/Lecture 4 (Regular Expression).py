
text="Hello 9 99 100"
words= text.split();
print (words)

# Regular Expresion

import re
rule1="[a-z]+"
rule2="[a-zA-Z]+"
rule3="[a-zA-Z0-9]+"
rule4="[a-zA-Z][a-zA-Z0-9]+"
rule5="[0-9]"
rule6="[0-9]+"
rule7="[0-9][0-9]"
p=re.compile(rule6)
result=p.findall(text)
print(result)
