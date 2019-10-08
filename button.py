class ButtonPom():
    def __init__(self, driver):
        self.driver = driver

    def get_buttons(self):
        return self.driver.find_elements_by_css_selector('button')

