from datetime import date, timedelta
import requests


class Student:
    """A student class as a base for method testing"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def alert_santa(self):
        self.naughty_list = True


    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"


    def apply_extention(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        response = requests.get(f"http://company.com/course-schedule/{self.last_name}/{self.first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"