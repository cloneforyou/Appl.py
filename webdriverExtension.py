class webdriverExtension():
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def get_parent_element(self, element):
        return element.find_element_by_xpath('..')

    def get_parent_search_string(self, element):
        parent_element = self.get_parent_element(element)
        labels = parent_element.find_elements_by_css_selector('label')
        if labels is None:
            raise Exception("Could not find any labels")
        search_text = ""
        for label in labels:
            search_text = label.text + label.get_attribute("for")
        return search_text.lower()

    def get_search_string(self, element):
        return (self.get_parent_search_string(element) + (element.text + element.get_attribute("id")) + (
            element.get_attribute("name"))).lower()
