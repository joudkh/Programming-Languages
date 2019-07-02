
text="H5i 9 99 100"
words= text.split();
print (words)

# Regular Expresion

import re
rule1="[a-zA-Z].[a-zA-Z]"
rule2="[0-9]{2,5}"
rule3="\d"
rule4="\D"
rule5="\w"
rule6="\W"
rule7="\s"
rule8="\S"
rule9="[^0-9]+"
rule10="[^0-9A-Z]+"
rule11="^a[0-9]+b$"
p=re.compile(rule1)
result=p.findall(text)
print(result)

# Find Email
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|sy)')
# Find Website
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
