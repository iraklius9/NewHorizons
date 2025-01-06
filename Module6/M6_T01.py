def string_methods_demo():
    s = "veni, vidi, vici"
    t = "67890"
    u = "GUNS N' ROSES"
    v = "     "
    w = "Coding404"

    print("1. capitalize():", s.capitalize())
    print("2. casefold():", u.casefold())
    print("3. center():", s.center(30, '-'))
    print("4. count():", s.count("v"))
    print("5. encode():", s.encode("utf-8"))
    print("6. endswith():", s.endswith("vici"))
    tabbed = "veni\tvidi\tvici"
    print("7. expandtabs():", tabbed.expandtabs(4))
    print("8. find():", s.find("vidi"))
    print("9. format():", "Welcome, {}!".format("User"))
    data = {"word": "victory"}
    print("10. format_map():", "veni, vidi, {word}".format_map(data))
    print("11. index():", s.index("vidi"))
    print("12. isalnum():", w.isalnum())
    print("13. isalpha():", "veni".isalpha())
    print("14. isascii():", s.isascii())
    print("15. isdecimal():", t.isdecimal())
    print("16. isdigit():", t.isdigit())
    print("17. isidentifier():", "coding_var".isidentifier())
    print("18. islower():", s.islower())
    print("19. isnumeric():", t.isnumeric())
    print("20. isprintable():", s.isprintable())
    print("21. isspace():", v.isspace())
    print("22. istitle():", "Veni Vidi Vici".istitle())
    print("23. isupper():", u.isupper())
    print("24. join():", "|".join(["veni", "vidi", "vici"]))
    print("25. ljust():", s.ljust(40, '-'))
    print("26. lower():", u.lower())
    print("27. lstrip():", "   coding".lstrip())
    trans = str.maketrans("aeiou", "12345")
    print("28. maketrans():", s.translate(trans))
    print("29. partition():", s.partition("vidi"))
    print("30. replace():", s.replace("vici", "victory"))
    print("31. rfind():", s.rfind("i"))
    print("32. rindex():", s.rindex("v"))
    print("33. rjust():", s.rjust(40, '-'))
    print("34. rpartition():", s.rpartition("vidi"))
    print("35. rsplit():", s.rsplit(" "))
    print("36. rstrip():", "veni vici   ".rstrip())
    print("37. split():", s.split(" "))
    multiline = "Veni\nVidi\nVici"
    print("38. splitlines():", multiline.splitlines())
    print("39. startswith():", s.startswith("veni"))
    print("40. strip():", "   veni vidi vici   ".strip())
    print("41. swapcase():", s.swapcase())
    print("42. title():", s.title())
    print("43. translate():", s.translate(trans))
    print("44. upper():", s.upper())
    print("45. zfill():", t.zfill(12))


if __name__ == "__main__":
    string_methods_demo()
