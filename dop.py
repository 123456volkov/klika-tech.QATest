import random
import allure


@allure.story('Check tittle name')
def check_title_name(self):
    with allure.step("Get name of the page"):
        driver = self.driver
        title_name = driver.find_element_by_tag_name("title")
    with allure.step("The coincidence of the names"):
        assert title_name == "Calculator"


@allure.story('Coincidence value of the button')
def check_button(xpatch, value, self):
    with allure.step("Try to find the button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath(xpatch)
    with allure.step("Get a name from the button"):
        buttons_value = button.text
    with allure.step("The coincidence of the names"):
        assert buttons_value == value
    with allure.step("Try to click the button"):
        button.click()


@allure.story('Get text from the display')
def get_input_text(self):
    with allure.step("Get text from the display"):
        driver = self.driver
        input_field = driver.find_element_by_xpath("/html/body/div[@id='display']")
        return input_field.text


@allure.story('Coincidence the input values and from the display')
def check_input_field(value, self, inversion):
    with allure.step("Get text from the display"):
        input_field_value = get_input_text(self)
    # print(input_field_value)
    with allure.step("The coincidence of values"):
        if inversion == False:
            with allure.step("The values match"):
                assert input_field_value == value
        if inversion:
            with allure.step("The values don't match"):
                assert input_field_value != value

@allure.story('Click a button 1')
def click_button_1(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[7]")
    with allure.step("Try to click on the button"):
        button.click()

@allure.story('Click a button 2')
def click_button_2(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[8]")
    with allure.step("Try to click on the button"):
        button.click()

with allure.step("Click button 3"):
    def click_button_3(self):
        with allure.step("Try to find button by xpatch"):
            driver = self.driver
            button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[9]")
        with allure.step("Try to click on the button"):
            button.click()


def click_button_4(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[4]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_5(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[5]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_6(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[6]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_7(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[1]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_8(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[2]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_9(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[3]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_0(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath(
            "/html/body/div[@class='buttons']/ul[@class='digits']/li[@class='double']")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_C(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='operations']/li[1]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_AC(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='operations']/li[2]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_X(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='operations']/li[3]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_Devide(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='operations']/li[4]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_Plus(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='operations']/li[5]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_Minus(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='operations']/li[6]")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_Equally(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath(
            "/html/body/div[@class='buttons']/ul[@class='operations']/li[@class='double']")
    with allure.step("Try to click on the button"):
        button.click()


def click_button_DotButton(self):
    with allure.step("Try to find button by xpatch"):
        driver = self.driver
        button = driver.find_element_by_xpath("/html/body/div[@class='buttons']/ul[@class='digits']/li[11]")
    with allure.step("Try to click on the button"):
        button.click()


with allure.step("Click random button"):
    def click_button(a, self):
        if a == 0:
            click_button_0(self)
        if a == 1:
            click_button_1(self)
        if a == 2:
            click_button_2(self)
        if a == 3:
            click_button_3(self)
        if a == 4:
            click_button_4(self)
        if a == 5:
            click_button_5(self)
        if a == 6:
            click_button_6(self)
        if a == 7:
            click_button_7(self)
        if a == 8:
            click_button_8(self)
        if a == 9:
            click_button_9(self)

with allure.step("Generating an integer number"):
    def int_number_generation(self):
        with allure.step("Random length of the next number"):
            b = random.randint(1, 9)
            i = 0
        while i < b:
            # list_of_buttons[random.randint(5, 9)]
            a = random.randint(0, 9)
            # print(a)
            # print("random ", i)
            click_button(a, self)
            i = i + 1

with allure.step("Generating an float number"):
    def float_number_generation(self):
        with allure.step("Random length of the next number"):
            b = random.randint(1, 9)
        with allure.step("Set dot-position"):
            dot_position = b // 2
        i = 0
        while i < b:
            if i == dot_position:
                click_button_DotButton(self)
            # list_of_buttons[random.randint(5, 9)]
            a = random.randint(0, 10)
            # print(a)
            # print("random ", i)
            click_button(a, self)
            i = i + 1

with allure.step("Check dot-button"):
    def check_button_DotButton(self):
        i = 0
        while i < 8:
            click_button(i, self)
            click_button_DotButton(self)
            click_button(i + 1, self)
            real_float_number = get_input_text(self)
            result_float_number = str(i) + "." + str(i + 1)
            # print("real_float_number ", real_float_number)
            # print("result_float_number ", result_float_number)
            check_input_field(result_float_number, self, False)
            i = i + 1
            # time.sleep(2)
            click_button_AC(self)
        i = 0
        while i < 8:
            click_button(i + 1, self)
            click_button_DotButton(self)
            click_button(i, self)
            real_float_number = get_input_text(self)
            if str(i) != "0":
                result_float_number = str(i + 1) + "." + str(i)
                # print("real_float_number ", real_float_number)
                # print("result_float_number ", result_float_number)
                check_input_field(result_float_number, self, False)
            i = i + 1
            # time.sleep(2)
            click_button_AC(self)
        i = 0
        while i < 7:
            click_button(i, self)
            click_button_DotButton(self)
            click_button(i + 1, self)
            click_button_DotButton(self)
            click_button(i + 2, self)
            real_float_number = get_input_text(self)
            result_float_number = str(i) + "." + str(i + 1) + str(i + 2)
            # print("real_float_number ", real_float_number)
            # print("result_float_number ", result_float_number)
            check_input_field(result_float_number, self, False)
            i = i + 1
            # time.sleep(2)
            click_button_AC(self)
        i = 0
        while i < 7:
            click_button(i + 2, self)
            click_button_DotButton(self)
            click_button(i + 1, self)
            click_button_DotButton(self)
            click_button(i, self)
            real_float_number = get_input_text(self)
            if str(i) == "0":
                result_float_number = str(i + 2) + "." + str(i + 1)
            else:
                result_float_number = str(i + 2) + "." + str(i + 1) + str(i)
            # print("real_float_number ", real_float_number)
            # print("result_float_number ", result_float_number)
            check_input_field(result_float_number, self, False)
            i = i + 1
            # time.sleep(2)
            click_button_AC(self)

with allure.step("Check button C"):
    def check_button_C(self):
        int_number_generation(self)
        input_text = get_input_text(self)
        # print(input_text)

        click_button_C(self)
        lenn = len(input_text)
        mod_input_text = input_text[: lenn - 1]

        # print(mod_input_text)
        check_input_field(mod_input_text, self, False)

with allure.step("Check button AC"):
    def check_button_AC(self):
        int_number_generation(self)
        # print(input_text)
        click_button_AC(self)
        input_text = get_input_text(self)
        # print(mod_input_text)
        check_input_field(input_text, self, False)

# -------------------------------------------
with allure.step("Check button X use integer numbers"):
    def check_button_X_use_integer_numbers(self):
        int_number_generation(self)
        # time.sleep(2)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_X(self)

        int_number_generation(self)
        # time.sleep(2)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        # real_result = get_input_text(self)
        result = int(number_first) * int(number_second)
        # print(real_result)
        # print(result)
        check_input_field(str(result), self, False)

with allure.step("Check button X use float numbers"):
    def check_button_X_use_float_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_X(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) * float(number_second)
        print(real_result)
        print(result)
        check_input_field(str(result), self, False)

with allure.step("Check button X use different numbers"):
    def check_test_is_button_X_is_valid_use_different_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_X(self)

        int_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) * int(number_second)
        print(real_result)
        print(result)
        check_input_field(str(result), self, False)

        click_button_AC(self)

        int_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_X(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = int(number_first) * float(number_second)
        print(real_result)
        print(result)
        check_input_field(str(result), self, False)

# -------------------------------------------
with allure.step("Check button Divide use integer numbers"):
    def check_button_Divide_use_integer_numbers(self):
        int_number_generation(self)
        # time.sleep(2)
        number_first = get_input_text(self)
        print("number_first ", number_first)
        check_input_field(str(number_first), self, False)

        click_button_Devide(self)

        int_number_generation(self)
        # time.sleep(2)
        number_second = get_input_text(self)
        print("number_second ", number_second)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        if number_second != 0:
            result = int(number_first) / int(number_second)
        else:
            check_input_field("Infinity", self, False)
        print("real_result ", real_result)
        print("result ", result)
        check_input_field(str(result), self, False)

with allure.step("Check button Divide use float numbers"):
    def check_button_Divide_use_float_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        print("number_first ", number_first)
        check_input_field(str(number_first), self, False)

        click_button_Devide(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        print("number_second ", number_second)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) / float(number_second)
        print("real_result ", real_result)
        print("result ", result)
        check_input_field(str(result), self, False)

with allure.step("Check button Divide use different numbers"):
    def check_button_Divide_use_different_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        print("number_first ", number_first)
        check_input_field(str(number_first), self, False)

        click_button_Devide(self)

        int_number_generation(self)
        number_second = get_input_text(self)
        print("number_second ", number_second)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) / int(number_second)
        print("real_result ", real_result)
        print("result ", result)
        check_input_field(str(result), self, False)

        click_button_AC(self)

        int_number_generation(self)
        number_first = get_input_text(self)
        print("number_first ", number_first)
        check_input_field(str(number_first), self, False)

        click_button_Devide(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        print("number_second ", number_second)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = int(number_first) / float(number_second)
        print("real_result ", real_result)
        print("result ", result)
        check_input_field(str(result), self, False)

# -------------------------------------------
with allure.step("Check button Plus use integer numbers"):
    def check_button_Plus_use_integer_numbers(self):
        int_number_generation(self)
        # time.sleep(2)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_Plus(self)

        int_number_generation(self)
        # time.sleep(2)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        # real_result = get_input_text(self)
        result = int(number_first) + int(number_second)
        # print(real_result)
        # print(result)
        check_input_field(str(result), self, False)

with allure.step("Check button Plus use float numbers"):
    def check_button_Plus_use_float_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        print("number_first ", number_first)
        check_input_field(str(number_first), self, False)

        click_button_Plus(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        print("number_second ", number_second)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) + float(number_second)
        print(real_result)
        print(result)
        check_input_field(str(result), self, False)

with allure.step("Check button Plus use different numbers"):
    def check_button_Plus_use_different_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_Plus(self)

        int_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) + int(number_second)
        print(real_result)
        print(result)
        str_result = str(result)
        lenn = len(str_result)
        if str_result[lenn - 1:lenn] == "0":
            check_input_field(str(result[:lenn - 2]), self, False)
        else:
            check_input_field(str(result), self, False)

        click_button_AC(self)

        int_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_Plus(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = int(number_first) + float(number_second)
        print(real_result)
        print(result)
        str_result = str(result)
        lenn = len(str_result)
        if str_result[lenn - 1:lenn] == "0":
            check_input_field(str(result[:lenn - 2]), self, False)
        else:
            check_input_field(str(result), self, False)

# -------------------------------------------
with allure.step("Check button Minus use integer numbers"):
    def check_button_Minus_use_integer_numbers(self):
        int_number_generation(self)
        # time.sleep(2)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_Minus(self)

        int_number_generation(self)
        # time.sleep(2)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        # real_result = get_input_text(self)
        result = int(number_first) - int(number_second)
        # print(real_result)
        # print(result)
        check_input_field(str(result), self, False)

with allure.step("Check button Minus use float numbers"):
    def check_button_Minus_use_float_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_Minus(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) - float(number_second)
        print(real_result)
        print(result)
        check_input_field(str(result), self, False)

with allure.step("Check button Minus use different numbers"):
    def check_button_Minus_use_float_different_numbers(self):
        float_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_Minus(self)

        int_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = float(number_first) - int(number_second)
        print(real_result)
        print(result)
        check_input_field(str(result), self, False)

        click_button_AC(self)

        int_number_generation(self)
        number_first = get_input_text(self)
        check_input_field(str(number_first), self, False)

        click_button_Minus(self)

        float_number_generation(self)
        number_second = get_input_text(self)
        check_input_field(str(number_second), self, False)

        click_button_Equally(self)

        real_result = get_input_text(self)
        result = int(number_first) + float(number_second)
        print(real_result)
        print(result)
        check_input_field(str(result), self, False)
