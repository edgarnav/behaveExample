from driver_interactions.ElementsInteractions import ElementsInteractions


class LoginPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_input_user_text = "user-name"
    id_input_password_text = "password"
    id_login_button = "login-button"

    def verify_login_page(self):
        if not self.is_element_displayed(self.id_input_user_text, "id"):
            self.log.info("No se encuentra en la pagina de inicio de sesion")
            assert False

    def send_user_password(self, user, password):
        self.send_text(user, self.id_input_user_text, "id")
        self.send_text(password, self.id_input_password_text, "id")

    def press_login_button(self):
        self.press_element(self.id_login_button, "id")
