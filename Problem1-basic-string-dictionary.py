def convert(n1,n2):
    #n1: number of sessions, n2: number of stars
    sessions={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    star={'one':1, 'two':2, 'three': 3, 'four': 4}
    sessions_number = sessions[int(n1)]
    star_number = star[str(n2)]
    print("I completed " + sessions_number + " sessions and I rated my expert " + str(star_number) + " starts")
convert(9,"two")