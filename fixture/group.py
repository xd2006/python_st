class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()

        self.return_to_groups_page()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # init group edit
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group update
        wd.find_element_by_name("update").click()

        self.return_to_groups_page()

    def fill_group_form(self, group):
        # fill groups form
        wd = self.app.wd
        self.app.general.populate_by_name("group_name", group.name)
        self.app.general.populate_by_name("group_header", group.name)
        self.app.general.populate_by_name("group_footer", group.name)

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def group_count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
