import string, math

polymer = []
with open("day5.input") as input:
    for line in input:
        for char in line.strip():
            polymer.append(char)
    
def is_react(left, right):
    if (left.isupper() and right.islower()) or (left.islower() and right.isupper()):
        if left.lower() == right.lower():
            return True

def clean_polymer(polymer, c):
    return [s for s in polymer if s != c]

def react_polymer(polymer):
    polymer = polymer[:]
    while True:
        check_again = False
        for i in range(0, len(polymer)-1):
            while i < len(polymer)-2 and polymer[i] == ".":
                i += 1
            j = i+1
            while j < len(polymer)-1 and polymer[j] == ".":
                j += 1
            left = polymer[i]
            right = polymer[j]    
            if is_react(left, right):
                polymer[i], polymer[j] = ".", "."
                check_again = True
        if not check_again:
            break
        polymer = clean_polymer(polymer, ".")
    return polymer
        
reacted_polymer = react_polymer(polymer)
print(f"Polymer: {''.join(reacted_polymer)}, count: {len(reacted_polymer)}")

cur_min = math.inf
for char in string.ascii_lowercase:
    c_polymer = clean_polymer(polymer, char)
    c_polymer = clean_polymer(c_polymer, char.upper())
    
    r_polymer_len = len(react_polymer(c_polymer))
    print(f"Removing {char}/{char.upper()}, len: {r_polymer_len}")
    if r_polymer_len < cur_min:
        cur_min = r_polymer_len

print(cur_min) 
