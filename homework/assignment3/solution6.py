def acronym(phrase):
    words = phrase.split()
    return "".join(word[0].upper() for word in words)

print(acronym("unidentified foreign object"))   # UFO
print(acronym("national aeronautics space administration"))   # NASA
print(acronym("world health organization"))   # WHO
