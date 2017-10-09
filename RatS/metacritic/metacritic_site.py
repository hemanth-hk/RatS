from RatS.base.base_site import Site


class Metacritic(Site):
    def __init__(self, args):
        self.LOGIN_PAGE = "https://secure.metacritic.com/login"
        login_form_selector = "//form"
        self.LOGIN_USERNAME_SELECTOR = login_form_selector + "//input[@id='login_email']"
        self.LOGIN_PASSWORD_SELECTOR = login_form_selector + "//input[@id='login_password']"
        self.LOGIN_BUTTON_SELECTOR = login_form_selector + "//button[@type='submit']"
        super(Metacritic, self).__init__(args)
        self.MY_RATINGS_URL = ''
