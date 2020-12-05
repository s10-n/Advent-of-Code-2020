import input,re

passports = input.passports
required_fields = {'byr':r"\b(19[2-9][0-9])|(200[0-2])\b",
                   'iyr':r"\b20(1[0-9]|20)\b",
                   'eyr':r"\b20(2[0-9]|30)\b",
                   'hgt':r"\b(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)\b",
                   'hcl':r"^#[a-z0-9]{6}\b",
                   'ecl':r"\b(amb|blu|brn|gry|grn|hzl|oth)\b",
                   'pid':r"\b\d{9}\b"}
invalid_passports = 0

for passport in passports:
    for field in required_fields.keys():
        try:
            if not re.search(required_fields[field],passport[field]):
                invalid_passports += 1
                break
                
        except:
            invalid_passports += 1
            break
        
valid_passports = len(passports) - invalid_passports
print(valid_passports)
