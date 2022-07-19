from dis import show_code
from webbrowser import get


def get_skills():
    skills = ["Python","C++","Javascript","Juggling","Running","Easting"]
    return skills


def show_skills(skills):
    print("Skills: ")
    for count, value in enumerate(skills):
        print(f"{count+1}. {value}")
    

    
 
   

def get_user_skills(skills):
    
    userSkill = []
    skill1 = int(input("Choose a skill from above by entering its number:"))
    userSkill.append(skills[skill1-1])
    
    skill2 = int(input("Choose a skill from above by entering its number:"))
    userSkill.append(skills[skill2-1])
    
    #print(userSkill)
    return userSkill




def get_user_cv(userSkill):
    # Get the users CV from their inputs
    # Write your code here
    user_cv= {}
    user_name = input("please enter your name:  ")
    user_cv.update({"name":user_name})
    user_age=int(input("Please enter you age: "))
    user_cv.update({"age":user_age})
    user_experience = int(input("Please enter your years of experiance: "))
    user_cv.update({"experience":user_experience})
    user_cv.update({"skills": userSkill})
    print("This Your CV: ")
    for x,y in user_cv.items():
        print(f"{x} : {y}")

    return user_cv




    


def check_acceptance(user_cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    if user_cv.get("age")>= 25 and user_cv.get("age")<= 40 and user_cv.get("experience")>3 :
        for x in user_cv.get("skills"):
            if user_cv.get("skills")==desired_skill:
                return True
            else:
                return False 


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions: ")
    print(show_skills(get_skills()))
    print(get_user_skills(get_skills()))
    # print(get_user_cv(get_skills()))
    cv =  get_user_cv(get_skills)
    check_acceptance(cv,"Python")
   

if __name__ == "__main__":
    main()

