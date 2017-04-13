import datetime

class MessageUser():
    user_details = []
    message = []
    base_message = """ Hi {name}!

    Welcome to Technical Experiment.

    Today {date}, you made a great decision to partner with our firm.
    Together we will use the lastest innovation and timeless principles to
    generate superior returns on behalf of your firm. Our sincerest aim
    is to enhance share of holder value for all of our clients and portfolio
    companies.

    Looking forward to the future,

    Michael
    """

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        detail = {
        "name": name,
        "amount": amount,
        }

        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail["email"] = email
            self.user_details.append(detail)

    def get_user_data(self):
        return self.user_details

    def make_message(self):
        if len(self.user_details) > 0:
            for detail in self.get_user_data():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                template_message = self.base_message
                formatted_msg = template_message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.message.append(formatted_msg)
                return self.message
            return[]

user = MessageUser()
user.add_user("Eric", 123.34, email='helloworld1@gmail.com')
user.add_user("Pablo", 123.35, email='helloworld2@gmail.com')
user.add_user("Niryal", 123.32, email='helloworld3@gmail.com')
user.add_user("Ramone", 123.32, email='helloworld4@gmail.com')
user.add_user("Liane", 123.32, email='helloworld25gmail.com')
user.add_user("Michael", 123.37, email='helloworld6@gmail.com')
user.add_user("Yana", 123.40, email='helloworld7@gmail.com')

print(user.make_message())
