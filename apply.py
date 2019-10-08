from selenium import webdriver
from field import FieldPom
from button import ButtonPom

class apply():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='./Apply/Drivers/chromedriver.exe')
        self.driver.set_page_load_timeout(10)
        self.Button = ButtonPom(self.driver)
        self.Field = FieldPom(self.driver)

    def get_url(self):
        self.driver.get(
            "https://hire.withgoogle.com/public/jobs/philosophieis/view/P_AAAAAADAAApI383ti6ZMHa?trackingTag=glassdoorFeed")

    def submit(self):
        Buttons = self.Button.get_buttons()
        submit_Button = next((b for b in Buttons if "submit" in b.text.lower()), None)
        if submit_Button is None:
            raise Exception("Submit Button Not Found")
        submit_Button.click()

    def run(self):
        self.get_url()
        self.Field.fill_out_required_inputs()
        self.submit()
        self.Button.this_is_error()


def main():
    app = apply()
    app.run()


main()

