from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None, homepage=None,
                 day_of_birth=None,
                 month_of_birth=None, year_of_birth=None, id=None):

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.title = title
        self.nickname = nickname
        self.company = company
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.homepage = homepage
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s: %s, %s " % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
