from selenium.webdriver import ActionChains
from webdriverExtension import webdriverExtension

class FieldPom():
    def __init__(self, driver):
        self.driver = driver

    def get_inputs(self):
        return self.driver.find_elements_by_css_selector('input[type="text"]')

    def get_required_inputs(self):
        required_inputs = []
        inputs = self.get_inputs()
        for input in inputs:
            if ("required" in input.text.lower()) or \
                    (input.get_attribute("required") is not None) or \
                    ("*" in input.text.lower()):
                required_inputs.append(input)
        return required_inputs

    def fill_out_form(self, element, value):
        action = ActionChains(self.driver)
        #webdriver_extension.scroll_to_element(element)
        action.move_to_element(element).click().perform()
        action.send_keys(value).perform()

    def fill_out_required_inputs(self):
        required_inputs = self.get_required_inputs()
        for input in required_inputs:
            search_string = webdriverExtension(self.driver).get_search_string(input)
            if "newsletter" in search_string:
                self.fill_out_form(input, "No")
                continue
            if "name" in search_string:
                if "first" in search_string:
                    self.fill_out_form(input, "Jae")
                    continue
                elif "last" in search_string:
                    self.fill_out_form(input, "Yim")
                    continue
            if "email" in search_string:
                self.fill_out_form(input, "jaehyunyim1997@gmail.com")
                continue
            if "phonenumber" in search_string:
                self.fill_out_form(input, "8189678929")
                continue
            if "linkedin" in search_string:
                self.fill_out_form(input, "https://www.linkedin.com/in/jae-hyun-yim-902702162/")
                continue

