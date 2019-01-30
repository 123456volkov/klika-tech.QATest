import unittest
import allure
from selenium import webdriver
import dop

class Testing(unittest.TestCase):
    def setUp(self):
        executable_path = "C:\Python37-32\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path)
        self.driver.get('url')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)

    @allure.feature('Test title on page')
    def test_title(self):
        dop.check_title_name(self)

    @allure.feature('Test button 1')
    def test_is_button_1_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[7]", "1", self)
        dop.check_input_field("1", self, False)

    @allure.feature('Test button 2')
    def test_is_button_2_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[8]", "2", self)
        dop.check_input_field("2", self, False)

    @allure.feature('Test button 3')
    def test_is_button_3_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[9]", "3", self)
        dop.check_input_field("3", self, False)

    @allure.feature('Test button 4')
    def test_is_button_4_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[4]", "4", self)
        dop.check_input_field("4", self, False)

    @allure.feature('Test button 5')
    def test_is_button_5_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[5]", "5", self)
        dop.check_input_field("5", self, False)

    @allure.feature('Test button 6')
    def test_is_button_6_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[6]", "6", self)
        dop.check_input_field("6", self, False)

    @allure.feature('Test button 7')
    def test_is_button_7_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[1]", "7", self)
        dop.check_input_field("7", self, False)

    @allure.feature('Test button 8')
    def test_is_button_8_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[2]", "8", self)
        dop.check_input_field("8", self, False)

    @allure.feature('Test button 9')
    def test_is_button_9_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[3]", "9", self)
        dop.check_input_field("9", self, False)

    @allure.feature('Test button 0')
    def test_is_button_0_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[@class='double']", "0", self)
        dop.check_input_field("0", self, False)

    @allure.feature('Test button "."')
    def test_is_button_DotButton_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='digits']/li[11]", ".", self)
        dop.check_input_field("", self, False)
        dop.check_button_DotButton(self)

    @allure.feature('Test button AC')
    def test_is_button_AC_valid(self):
        dop.check_button_AC(self)

    @allure.feature('Test button C')
    def test_is_button_C_valid(self):
        dop.check_button_C(self)

    @allure.feature('Test button X')
    def test_is_button_X_is_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='operations']/li[3]", "x", self)

    @allure.feature('Test button X with integer numbers')
    def test_is_button_X_is_valid_use_integer_numbers(self):
        dop.check_button_X_use_integer_numbers(self)

    @allure.feature('Test button X with float numbers')
    def test_is_button_X_is_valid_use_float_numbers(self):
        dop.check_button_X_use_float_numbers(self)

    @allure.feature('Test button X with different numbers')
    def test_is_button_X_is_valid_use_different_numbers(self):
        dop.check_test_is_button_X_is_valid_use_different_numbers(self)

    """ 
    @allure.feature('Test a button "-"')
    def test_is_button_Minus_is_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='operations']/li[4]", "/", self)
        dop.check_input_field("-", self, False)
    """

    @allure.feature('Test button "/" with integer numbers')
    def test_is_button_Divide_is_valid_use_integer_numbers(self):
        dop.check_button_Divide_use_integer_numbers(self)

    @allure.feature('Test button "/" with float numbers')
    def test_is_button_Divide_is_valid_use_float_numbers(self):
        dop.check_button_Divide_use_float_numbers(self)

    @allure.feature('Test button "/" with different numbers')
    def test_is_button_Divide_is_valid_use_different_number(self):
        dop.check_button_Divide_use_different_numbers(self)

    @allure.feature('Test button "+"')
    def test_is_button_Plus_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='operations']/li[5]", "+", self)

    @allure.feature('Test button "+" with integer numbers')
    def test_is_button_Plus_is_valid_use_integer_numbers(self):
        dop.check_button_Plus_use_integer_numbers(self)

    @allure.feature('Test button "+" with float numbers')
    def test_is_button_Plus_is_valid_use_float_numbers(self):
        dop.check_button_Plus_use_float_numbers(self)

    @allure.feature('Test button "+" with different numbers')
    def test_is_button_Plus_is_valid_use_different_number(self):
        dop.check_button_Plus_use_different_numbers(self)

    @allure.feature('Test button "-"')
    def test_is_button_Minus_valid(self):
        dop.check_button("/html/body/div[@class='buttons']/ul[@class='operations']/li[6]", "-", self)

    @allure.feature('Test button "-" with integer numbers')
    def test_is_button_Minus_is_valid_use_integer_numbers(self):
        dop.check_button_Minus_use_integer_numbers(self)

    @allure.feature('Test button "-" with float numbers')
    def test_is_button_Minus_is_valid_use_float_numbers(self):
        dop.check_button_Minus_use_float_numbers(self)

    @allure.feature('Test button "-" with different numbers')
    def test_is_button_Minus_is_valid_use_different_number(self):
        dop.check_button_Minus_use_float_different_numbers(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
