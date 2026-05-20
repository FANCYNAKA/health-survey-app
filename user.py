class User:

    def __init__(
        self,
        age,
        gender,
        income,
        utilities_amount,
        entertainment_amount,
        school_fees_amount,
        shopping_amount,
        healthcare_amount
    ):

        self.age = age
        self.gender = gender
        self.income = income

        self.utilities_amount = utilities_amount
        self.entertainment_amount = entertainment_amount
        self.school_fees_amount = school_fees_amount
        self.shopping_amount = shopping_amount
        self.healthcare_amount = healthcare_amount


    def display_user_info(self):

        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Income:", self.income)

        print("Utilities:", self.utilities_amount)
        print("Entertainment:", self.entertainment_amount)
        print("School Fees:", self.school_fees_amount)
        print("Shopping:", self.shopping_amount)
        print("Healthcare:", self.healthcare_amount)