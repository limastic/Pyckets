from datetime import date

def convertBirthDate(birth_date : str) -> str:
    today = date.today().strftime("%d/%m/%Y")

    # On regarde si la date de naissance est déjà passée cette année
    birthDatePassed = False
    if int(today[3:5]) == int(birth_date[3:5]) and int(today[:1]) >= int(birth_date[:1]):
        birthDatePassed = True
    if int(today[3:5]) > int(birth_date[3:5]):
        birthDatePassed = True 
    
    age = int(today[6:]) - int(birth_date[6:])
    if not birthDatePassed:
        age -= 1
    
    return age

if __name__ == "__main__":
    