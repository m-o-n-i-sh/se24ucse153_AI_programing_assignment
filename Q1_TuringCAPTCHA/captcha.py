import random
import string
class CaptchaSystem:
    def generate_captcha(self, length=6):
        characters = string.ascii_letters + string.digits
        captcha = ''.join(random.choice(characters) for _ in range(length))
        return captcha
    def present_captcha(self, captcha):
        print("\n------ CAPTCHA VERIFICATION ------")
        print("Enter the characters shown below")
        print("CAPTCHA:", captcha)
    def verify_captcha(self, captcha, user_input):
        return captcha == user_input
    def run(self):
        while True:
            captcha = self.generate_captcha()
            self.present_captcha(captcha)
            user_input = input("Enter CAPTCHA: ")
            if self.verify_captcha(captcha, user_input):
                print("\nAccess Granted")
                break
            else:
                print("\nIncorrect CAPTCHA. Generating a new one...")
if __name__ == "__main__":
    system = CaptchaSystem()
    system.run()