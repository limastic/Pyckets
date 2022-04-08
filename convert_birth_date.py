from datetime import date

def convertBirthDate(birth_date : str) -> str:
    today = date.today().strftime("%Y/%m/%d")

    # On regarde si la date de naissance est déjà passée cette année
    birthDatePassed = False
    if int(today[5:7]) == int(birth_date[5:7]) and int(today[8:]) >= int(birth_date[8:]):
        birthDatePassed = True
    if int(today[5:7]) > int(birth_date[5:7]):
        birthDatePassed = True 
    
    age = int(today[:3]) - int(birth_date[:3])
    if not birthDatePassed:
        age -= 1
    
    return age

if __name__ == "__main__":
    print(convertBirthDate('2004-04-30'))