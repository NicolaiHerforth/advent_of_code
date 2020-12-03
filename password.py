def valid_passwords(pass_file_path):
    valid_old, valid = 0, 0
    with open(pass_file_path) as file:
        for line in file:
            line = line.strip('\n')
            # set the lower value, higher value and the letter requirement variables.
            lower, higher, letter = int(line.split()[0].split('-')[0]), int(line.split()[0].split('-')[1]), line.split()[1].strip(':')

            # count letter occurences in the password
            letter_count = 0

            for curr_letter in range(len(line.split()[2])):
                if letter == line.split()[2][curr_letter]:
                    letter_count += 1
            # if the letter occurence is between the higher and lower value, it is valid for the old company
            if letter_count >= lower and letter_count <= higher:
                valid_old += 1

            # if the letter is either in the lower value position, or in the higher value position, 
            # but not in both, then it is a valid password in the new company.
            if letter == line.split()[2][lower-1] and not letter == line.split()[2][higher-1]:
                valid += 1
            elif letter == line.split()[2][higher-1] and not letter == line.split()[2][lower-1]:
                valid += 1

    return(str(valid_old), str(valid))

password_file_name = input('What is your password file name? (file has to be in the data folder) \n')
old_company_valids, new_company_valids = valid_passwords(f'data/{password_file_name}.txt')
print(f'Valid passwords in old company: {old_company_valids} \n')
print(f'Valid passwords in new company: {new_company_valids} \n')