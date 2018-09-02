import pymysql

from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
        try:
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, "
                       "work, fax, email, email2, email3, homepage, bday, bmonth, byear from addressbook where "
                       "deprecated = '0000-00-00 00:00:00'")
        try:
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work,
                 fax, email, email2, email3, homepage, bday, bmonth, byear) = row
                list.append(Contact(id=str(id), first_name=firstname, middle_name=middlename, last_name=lastname,
                                    nickname=nickname, title=title, company=company, address=address,
                                    homephone=home, mobilephone=mobile, workphone=work, secondaryphone=fax,
                                    email=email, email2=email2, email3=email3, homepage=homepage, day_of_birth=bday,
                                    month_of_birth=bmonth, year_of_birth=byear))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
