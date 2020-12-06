# # part one
# def password_is_valid(password, character, min, max):
#     num_occurrences = 0
#     for c in password:
#         if c == character:
#             num_occurrences += 1

#     return min <= num_occurrences and max >= num_occurrences

# part two
def password_is_valid(password, character, min, max):
    num_occurrences = 0

    if password[min-1] == character:
        num_occurrences += 1

    if password[max-1] == character:
        if num_occurrences > 0:
            return False
        
        num_occurrences += 1

    return num_occurrences > 0

def main():
    password_list = open("./input.txt", "r")
    lines = password_list.readlines()
    valid_passwords = []

    for line in lines:
        segments = line.split(' ')
        min = int(segments[0].split('-')[0])
        max = int(segments[0].split('-')[1])
        character = segments[1].split(':')[0]
        password = segments[2]

        if password_is_valid(password, character, min, max):
            valid_passwords.append(password)

    
    print(len(valid_passwords))

    

if __name__ == '__main__':
    main()