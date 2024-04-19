def string_conversion(s,ctype="upper"):
    if ctype == "upper":
        return s.upper()
    elif ctype == "lower":
        return s.lower()
    elif ctype == "title":
        return s.title()
    elif ctype == "capitalize":
        return s.capitalize()
    else:
        return s
def main():
    str1 = string_conversion("Python")
    str2 = string_conversion("LOWER",ctype="lower")
    str3 = string_conversion("TITLE",ctype="title")
    str4 = string_conversion("capitalize",ctype="capitalize")
    print(str1,str2,str3,str4)

main()
     
