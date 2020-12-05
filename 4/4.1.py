import input

passports = input.passports
required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
invalid_passports = 0

for passport in passports:
    for field in required_fields:
        try:
            passport[field]
        except:
            invalid_passports += 1
            break
        
valid_passports = len(passports) - invalid_passports
print(valid_passports)
