import re

def translateword(text):
    match = re.match(r"^[aeiou]", text)
    if match or text.startswith("xr") or text.startswith("yt"):
        return text + "ay"
    ## Rule 3
    match = re.match(r"^[bcdfghjklmnpqrstvwxyz]*qu", text)
    if match:
        return text[match.end():] + match.group() + "ay"
    ## Rule 4
    match = re.match(r"^[bcdfghjklmnpqrstvwxyz]+y", text)
    if match:
        return text[match.end()-1:] + match.group()[:-1] + "ay"
    ## Rule 2
    match =  re.match(r"^[bcdfghjklmnpqrstvwxyz]+", text)
    if match:
        return text[match.end():] + match.group() + "ay"
        
def translate(text):
    ans = []
    for w in text.split():
        ans.append(translateword(w))
    return ' '.join(ans)