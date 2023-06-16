from datetime import date
from random import randint
import database as db


class User:
    all_users = []

    def __init__(self, first_name: str, last_name: str, year_of_birth: int, country: str, email: str, password: str):

        assert len(first_name) < 25, "String length exceeded, max length is 25"
        assert len(last_name) < 25, "String length exceeded, max length is 25"
        assert 0 < year_of_birth < date.today().year, "Must input a valid year"
        # assert country #TODO: make the attribute country check wether your country initials exists or not and is supported, using a dictionary
        # assert email #TODO: check if email is valid and is not already taken
        # assert password #TODO: Check if password length is good enough, and if it has the requisites like special characters, uppers and lowers, etc...

        self.first_name = first_name
        self.last_name = last_name
        self._full_name = f"{first_name} {last_name}"  # Property TODO: chequear por que esto da error si le quito la _
        self.year_of_birth = year_of_birth
        self._age = date.today().year - year_of_birth
        self.country = country
        self.email = email
        self._password = password
        self.is_logged = False

        # Actions

        User.all_users.append(self)  # Creates a list with all user objects, must be handy to something I guess

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return self._age

    @full_name.setter
    def full_name(self, name):
        first, *last = name.split()
        self.first_name = first
        self.last_name = " ".join(last)

    # TODO: Create a Constructor Method to initialize the Users from a CSV file, later migrate it to a SQL database

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.first_name}", "{self.last_name}", {self.year_of_birth}, "{self.country}", "{self.email}", "{self._password}")'

    @staticmethod
    def logging(email: str, password: str):
        if (email, password) in db.return_loggins():
            return True
        else:
            return False

    @staticmethod
    def signing(email: str, password: str):
        # TODO: Make the logic to create a new user in the database
        return True


class Admin(User):
    all_admins = []

    def __init__(self, first_name: str, last_name: str, year_of_birth: int, country: str, email: str, password: str):
        super().__init__(first_name, last_name, year_of_birth, country, email, password)

        # Actions
        Admin.all_admins.append(self)


class Bank_account:  # Uses a User object and assign him an ID to make bank transactions

    @staticmethod
    def generate_id():
        # TODO: check wether the ID is in use or not
        return randint(100000000,
                       999999999)  # gives the bank account a random ID, capacity for 8.999.999.999 users, expandible if necessary

    def __init__(self, bank_user: User):
        self.bank_user = bank_user
        self._bank_ID = Bank_account.generate_id()

    @property
    def user_ID(self):
        return self._bank_ID


def main():
    Juan = Admin("Juan Manuel", "González Vega", 1998, "CUB", "juanmgv98@gmail.com", "QWERTY")
    Dorian = User("Dorian", "Gay Perez", 1998, "CUB", "dorianperez@gmail.com", "12345")
    Alejandro = User("Alejandro", "Marrero Garcia", 1997, "CUB", "manko@gmail.com", "axax")
    Andy = User("Andy Daniel", "Matamoros", 1998, "CUB", "rata@gmail.com", "menores13")

    for i in User.all_users:
        print(i)

    main_account = Bank_account(Juan)
    print(main_account.user_ID)
    print(main_account.bank_user.full_name)


if __name__ == "__main__":
    main()
