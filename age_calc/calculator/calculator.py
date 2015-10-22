import dateutil.parser
from datetime import date


class Calculator(object):
    def __init__(self):
        today = date.today()
        self._year = today.year
        self._day = today.day
        self._month = today.month

    def age_as_of_today(self, month=None, day=None, year=None, dob=None):
        """
        Age as of Today, Method to calculate the age given the date of birth as of today.

        :param month: int
        :param day: int
        :param year: int
        :param dob: string
        :return: int
        """
        if dob:
            month, day, year = self._get_month_day_year_from_date(dob)
        return self._year - int(year) - ((self._month, self._day) < (int(month), int(day)))

    def age_as_of_date(self, dob=None, dob_month=None, dob_day=None, dob_year=None, aod=None, aod_year=None, aod_day=None, aod_month=None):
        """
        Age as of Date, Method to calculate the age given the date of birth as of a given date.

        :param dob: String
        :param dob_month: int
        :param dob_day: int
        :param dob_year: int
        :param aod: String
        :param aod_year: int
        :param aod_day: int
        :param aod_month: int
        :return: int
        """
        if dob:
            dob_month, dob_day, dob_year = self._get_month_day_year_from_date(dob)
        if aod:
            aod_month, aod_day, aod_year = self._get_month_day_year_from_date(aod)
        return int(aod_year) - int(dob_year) - ((int(aod_month), int(aod_day)) < (int(dob_month), int(dob_day)))

    @staticmethod
    def _get_month_day_year_from_date(date_string):
        """
        Get Month Day Year from Date, method to get the month, day, year values from a string date.

        :param date_string: String
        :return:tuple
        """
        date_obj = dateutil.parser.parse(date_string)
        return date_obj.month, date_obj.day, date_obj.year
