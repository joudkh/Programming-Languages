emoji={}
emoji[":-)"]="happy"
emoji[":)"]="happy"
emoji[":o)"]="happy"
emoji[":-}"]="happy"
emoji[";-}"]="happy"
emoji[":->"]="happy"
emoji[";-)"]="happy"

emoji[":-("]="sad"
emoji[":("]="sad"
emoji[":-|"]="sad"
emoji[";-("]="sad"
emoji[";-<"]="sad"
emoji["|-{"]="sad"


#THE INPUT TEXT#
text="I like YPU :-) :o)" 
ls=text.split()

newtxt=""
for value in ls:
    if value in emoji:
        newtxt=newtxt+emoji[value]
    else:
        newtxt=newtxt+value
    newtxt=newtxt+' '

print(newtxt)
