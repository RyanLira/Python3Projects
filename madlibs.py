# madlibs via string concatonation
# Ryan Lira May 27, 2022

# if you initialize a
# a = "john"
# then You can concatonate strings in python in one of these three ways:

# ONE: print("give it to" + a)
# TWO: print("give it to {}".format(a))
# THREE: print(f"give it to {}")


adj = input("adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("famous_person: ")

madlib = f"computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)