def response(hey_bob):
    w = hey_bob.strip()
    ans = "Whatever."
    if (w == ""):
        ans = "Fine. Be that way!"
    elif w.isupper():
        if w.endswith("?"):
            ans = "Calm down, I know what I'm doing!"
        else:
            ans = "Whoa, chill out!"
    elif w.endswith("?"):
        ans = "Sure."
        
    return ans