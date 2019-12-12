import re
from termcolor import colored
import random
from string import ascii_letters, digits

class Student():
    def __init__(self):
        self.__name = 'Alexey'
        self.__lastname = 'Silnikov'
        self.__birthday = '30.04.1990'
        self.__gender = 'male'
        self.__assessment = 5
        self.__specialty = 'test'
        self.__number = 3
        self.__student_info = None

    @property
    def student_name(self):
        if len(self.__name) > 25:
            print(colored("NAME ERROR! Only 25 characters allowed!", 'red'))
            raise ValueError

    @property
    def student_lastname(self):
        if len(self.__lastname) > 50:
            print(
                colored("LASTNAME ERROR! Only 50 characters allowed!", 'red'))
            raise ValueError

    @property
    def student_birthday(self):
        if not re.match(r'^\d{2}.\d{2}.\d{4}$', self.__birthday):
            print(
                colored("BIRTHDAY ERROR! Only input in DD.MM.YYYY format!",
                        'red'))
            raise ValueError

    @property
    def student_gender(self):
        if not re.match(r'^[mM]ale$|^[fF]emale$', self.__gender):
            print(
                colored("GENDER ERROR! Only input gender Male or Female !",
                        'red'))
            raise ValueError

    @property
    def assessment(self):
        return self.__assessment

    @assessment.setter
    def assessment(self, assessment):
        if assessment in range(1, 11):
            self.__assessment = assessment
        else:
            print(
                colored("ASSESSMENT ERROR! Only input number from 1 to 10",
                        'red'))
            raise ValueError

    @property
    def student_specialty(self):
        return self.__specialty

    @student_specialty.setter
    def student_specialty(self, specialty):
        if len(specialty) > 50:
            print(
                colored("SPECIALTY ERROR! Only 50 characters allowed!", 'red'))
            raise ValueError
        else:
            self.__specialty = specialty

    @property
    def student_course_number(self):
        return self.__number

    @student_course_number.setter
    def student_course_number(self, course_number):
        if not re.match(r'^[0-9]{,}$', str(course_number)):
            print(colored('NUMBER ERROR! Only input integer', 'red'))
            raise ValueError
        else:
            self.__number = course_number

    @property
    def student_info(self):
        print(self.__name.title() + ':' + self.__lastname.title() + ':' +
              self.__birthday + ':' + self.__gender.title()[0] + ':' +
              str(self.__assessment) + ':' + self.__specialty.title() + ':' +
              str(self.__number))
        return self.__student_info

class ExtenderStudent(Student):
  def __init__(self, logins):
    super().__init__()


  def passwords(self):
    symbol = ascii_letters + digits
    pswd = random.SystemRandom()
    password = "".join(pswd.choice(symbol) for i in range(9))  
    return password 
  
  def logins(self):
    file = open('students.dat', 'r')
    a = []
    b = []
    l = "LOGIN: "
    p = "PASSWORD: "
    for line in file:
        password = self.passwords()        
        line_info = line.split(":::")
        login = line_info[0][0] + line_info[1]
        for item in b:
          if login != item:
            if login != item.split('[')[0]:
              pass
            else:
                login += '[' + '1' + ']'
          else:
              if item[-1] == ']':
                postfix = int(item[-2])
                login = login[:-3] + '[' + str(postfix+1) + ']'
              else:
                  login += '[' + '1' + ']'
        b.append(login)
        a.append(l + login + " ; " + p + password)
    listing = "\n".join(a)
    file.close()
    ext = "".join(listing)
    with open("ext_students.dat", "w+") as f:
        f.write(ext)
        f.close()
    print(listing)    
    return listing


test = ExtenderStudent(Student)
test.logins()
test.student_name
test.student_lastname
test.student_birthday
test.assessment = 10
test.student_specialty = 'devops'
test.student_course_number = 25
test.student_info
