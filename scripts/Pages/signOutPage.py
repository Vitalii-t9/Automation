from scripts.Actions import Action


class SignOutPage(Action):

    def __init__(self, driver):
        self.driver = driver
        
        self.singOut_link_linktext = "Sign out"
        self.locatorTypes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]



