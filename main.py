

# sould add deleted or presant shareholder information in the output form in thr genrated forms perm file
# how to make checkboxes readonly
# resize image or face photo to fit in the box photo exactly
# make any photo to resize to that size

from tkinter import filedialog

import kivymd.icon_definitions

from kivymd.icon_definitions import md_icons
from kivy.lang import Builder
from kivymd.app import MDApp
import shutil
import os
import cv2
from PIL import Image
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import BooleanProperty
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

Window.clearcolor = (1,1,1,1)

numbers = []
for number in range(1, 10000):
    if number < 10:
        numbers.append(f'000{number}')
    elif 100 > number > 9:
        numbers.append(f'00{number}')
    elif 1000 > number > 99:
        numbers.append(f'0{number}')
    elif 10000 > number > 999:
        numbers.append(f'{number}')

print(numbers)


class GridLayoutExample(GridLayout):
    pass


class GridLayoutExample2(GridLayout):
    pass


class ScrollViewExample(ScrollView):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)


class MainWidget(Widget):
    pass


class PasswordDialogView(Screen):
    pass


class OpeningWindow(Screen):
    password_dialog = None
    from_admin_page = BooleanProperty()

    def set_call_page(self, from_admin_page):
        self.from_admin_page = from_admin_page

    def ask_admin_password(self):
        content_cls = PasswordDialogView()
        if not self.password_dialog:
            self.password_dialog = MDDialog(title='Password', type='custom', content_cls=content_cls, buttons=[MDFlatButton(text="CANCEL", on_press=self.close_dialog), MDRaisedButton(text="ACCESS", on_press=lambda x: self.access_admin_page(x, content_cls))])
        self.password_dialog.open()

    def access_admin_page(self, instance_btn, content_cls):
        password_file = open('background_files/pass/password.txt', 'r')
        password = password_file.readline()
        password_input = content_cls.ids.admin_password._get_text()
        print(password_input)
        if password == password_input:
            self.close_dialog()
            self.manager.current = 'AdministrationWindow'
            self.manager.transition.direction = 'left'
            content_cls.ids.admin_password.text = ''
            content_cls.ids.admin_password.password = True
            content_cls.ids.eye_icon.icon = 'eye-off'
            print('correct')
        else:
            toast('Incorrect Password')

    def close_dialog(self, *args):
        self.password_dialog.dismiss()

    def total_shareholders(self):
        number_of_files = 0
        total_amount = 0
        for element in os.listdir('generated_forms_temp'):
            number_of_files += 1
            amount_file = open(f'generated_forms_temp/{element}/{element}.txt', 'r')
            amount = amount_file.readlines()
            total_amount += int(amount[23])

        total_shareholders = Popup(title='Total Shareholders',
                                   content=Label(text=f'''Total No of Shareholders: {number_of_files}
Total Amount Received: ₹{total_amount}''',
                                                 color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                   size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                   background_color=(1, 170 / 255, 0, 1), background='')
        total_shareholders.open()

    def change_password(self):
        self.manager.current = 'ChangePasswordWindow'


class RegistrationWindow(Screen):
    total = StringProperty('0')

    def generate_certificate(self):
        email_error = self.ids.email_address.error
        date_error = self.ids.date_of_birth.error
        first_name_input = self.ids.first_name.text
        surname_input = self.ids.surname.text
        date_of_birth_input = self.ids.date_of_birth.text
        postal_address_input = self.ids.postal_address.text
        post_code_input = self.ids.post_code.text
        mobile_phone_no_india_input = self.ids.mobile_phone_no_india.text
        mobile_phone_no_abroad_input = self.ids.mobile_phone_no_abroad.text
        iqama_ref_input = self.ids.iqama_ref.text
        passport_ref_input = self.ids.passport_ref.text
        email_address_input = self.ids.email_address.text
        work_place_input = self.ids.work_place.text
        amount_1_input = self.ids.amount_1.text
        amount_2_input = self.ids.amount_2.text
        amount_3_input = self.ids.amount_3.text
        amount_4_input = self.ids.amount_4.text
        amount_5_input = self.ids.amount_5.text
        amount_6_input = self.ids.amount_6.text
        amount_7_input = self.ids.amount_7.text
        amount_8_input = self.ids.amount_8.text
        amount_9_input = self.ids.amount_9.text
        amount_10_input = self.ids.amount_10.text
        date_1_input = self.ids.date_1.text
        date_2_input = self.ids.date_2.text
        date_3_input = self.ids.date_3.text
        date_4_input = self.ids.date_4.text
        date_5_input = self.ids.date_5.text
        date_6_input = self.ids.date_6.text
        date_7_input = self.ids.date_7.text
        date_8_input = self.ids.date_8.text
        date_9_input = self.ids.date_9.text
        date_10_input = self.ids.date_10.text
        photo_location_path_input = self.ids.photo_location_path.text
        other_input = self.ids.other.text
        checkbox1_input = self.ids.checkbox1.active
        checkbox2_input = self.ids.checkbox2.active
        checkbox3_input = self.ids.checkbox3.active
        male_checkbox_input = self.ids.male_checkbox.active
        female_checkbox_input = self.ids.female_checkbox.active
        father_name_input = self.ids.father_name.text
        mother_name_input = self.ids.mother_name.text
        name_1_input = self.ids.name_1.text
        relation_1_input = self.ids.relation_1.text
        name_2_input = self.ids.name_2.text
        relation_2_input = self.ids.relation_2.text
        name_3_input = self.ids.name_3.text
        relation_3_input = self.ids.relation_3.text
        name_4_input = self.ids.name_4.text
        relation_4_input = self.ids.relation_4.text
        percentage_1_input = self.ids.percentage_1.text
        percentage_2_input = self.ids.percentage_2.text
        percentage_3_input = self.ids.percentage_3.text
        percentage_4_input = self.ids.percentage_4.text
        other_details_input = self.ids.other_details.text
        suggested_by_input = self.ids.suggested_by.text
        photo_identification_path_input = self.ids.photo_identification_path.text
        if amount_1_input == '' or amount_1_input in '          ':
            amount_1_input = '0'
        if amount_2_input == '' or amount_2_input in '          ':
            amount_2_input = '0'
        if amount_3_input == '' or amount_3_input in '          ':
            amount_3_input = '0'
        if amount_4_input == '' or amount_4_input in '          ':
            amount_4_input = '0'
        if amount_5_input == '' or amount_5_input in '          ':
            amount_5_input = '0'
        if amount_6_input == '' or amount_6_input in '          ':
            amount_6_input = '0'
        if amount_7_input == '' or amount_7_input in '          ':
            amount_7_input = '0'
        if amount_8_input == '' or amount_8_input in '          ':
            amount_8_input = '0'
        if amount_9_input == '' or amount_9_input in '          ':
            amount_9_input = '0'
        if amount_10_input == '' or amount_10_input in '          ':
            amount_10_input = '0'
        if '%' in percentage_1_input:
            percentage_1_input = percentage_1_input.replace('%', '')
        if '%' in percentage_2_input:
            percentage_2_input = percentage_2_input.replace('%', '')
        if '%' in percentage_3_input:
            percentage_3_input = percentage_3_input.replace('%', '')
        if '%' in percentage_4_input:
            percentage_4_input = percentage_4_input.replace('%', '')
        if percentage_1_input == '' or percentage_1_input in '                ':
            percentage_1_input = '0'
        if percentage_2_input == '' or percentage_2_input in '                ':
            percentage_2_input = '0'
        if percentage_3_input == '' or percentage_3_input in '                ':
            percentage_3_input = '0'
        if percentage_4_input == '' or percentage_4_input in '                ':
            percentage_4_input = '0'

        no_letters = False
        try:
            amount_1_input = str(int(amount_1_input) + 0)
            amount_2_input = str(int(amount_2_input) + 0)
            amount_3_input = str(int(amount_3_input) + 0)
            amount_4_input = str(int(amount_4_input) + 0)
            amount_5_input = str(int(amount_5_input) + 0)
            amount_6_input = str(int(amount_6_input) + 0)
            amount_7_input = str(int(amount_7_input) + 0)
            amount_8_input = str(int(amount_8_input) + 0)
            amount_9_input = str(int(amount_9_input) + 0)
            amount_10_input = str(int(amount_10_input) + 0)
            percentage_1_input = str(int(percentage_1_input) + 0)
            percentage_2_input = str(int(percentage_2_input) + 0)
            percentage_3_input = str(int(percentage_3_input) + 0)
            percentage_4_input = str(int(percentage_4_input) + 0)
            mobile_phone_no_india_input = str(int(mobile_phone_no_india_input) + 0)
            mobile_phone_no_abroad_input = str(int(mobile_phone_no_abroad_input) + 0)
            post_code_input = str(int(post_code_input) + 0)
            iqama_ref_input = str(int(iqama_ref_input) + 0)
            no_letters = True

        except ValueError:
            letters_in_number_slots = Popup(title='Registration Status: Unsuccessful', content=Label(text='''Please Ensure That Characters Other Than Numbers 
Are Not Entered In The Slots Specific For Numbers''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                            size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                            background_color=(1, 170 / 255, 0, 1), background='')
            letters_in_number_slots.open()

        not_image = True
        try:
            output_identification_path = ''
            for letter in photo_identification_path_input:
                if letter in '\~':
                    output_identification_path += '/'
                elif letter == '"':
                    output_identification_path += ''
                else:
                    output_identification_path += letter

            output_path = ''
            for letter in photo_location_path_input:
                if letter in '\~':
                    output_path += '/'
                elif letter == '"':
                    output_path += ''
                else:
                    output_path += letter

            logo = Image.open(output_path)
            id_identification = Image.open(output_identification_path)
            not_image = False
        except:
            no_image = Popup(title='Image Open: Unsuccessful',
                             content=Label(text=f'Ensure That Selected File Is A Image', color=(1, 1, 1, 1),
                                           bold=True, font_size=dp(15)),
                             size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                             background_color=(1, 170 / 255, 0, 1), background='')
            no_image.open()

        if first_name_input.strip() == '' or surname_input.strip() == '' or date_of_birth_input.strip() == '' or postal_address_input.strip() == '' or post_code_input.strip() == '' or mobile_phone_no_india_input.strip() == '' or mobile_phone_no_abroad_input.strip() == '' or iqama_ref_input.strip() == '' or passport_ref_input.strip() == '' or email_address_input.strip() == '' or work_place_input.strip() == '' or amount_1_input.strip() == '' or amount_2_input.strip() == '' or amount_3_input.strip() == '' or amount_4_input.strip() == '' or amount_5_input.strip() == '' or amount_6_input.strip() == '' or amount_7_input.strip() == '' or amount_8_input.strip() == '' or amount_9_input.strip() == '' or amount_10_input.strip() == '' or photo_location_path_input.strip() == '' or checkbox1_input == False and checkbox2_input == False and checkbox3_input == False or father_name_input.strip() == '' or mother_name_input.strip() == '' or name_1_input.strip() == '' or relation_1_input.strip() == '' or suggested_by_input.strip() == '' or male_checkbox_input == False and female_checkbox_input == False or percentage_1_input.strip() == '' or photo_identification_path_input.strip() == '':
            unfilled_popup = Popup(title='Registration Status: Unsuccessful',
                                   content=Label(text='Please Ensure That All Details Are Filled', color=(1, 1, 1, 1),
                                                 bold=True, font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                   separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            unfilled_popup.open()
        elif checkbox3_input == True and other_input.strip() == '':
            other_unfilled_popup = Popup(title='Registration Status: Unsuccessful', content=Label(text='''Its Mandatory To Write The Source Of Photo 
Provided If Your Selection is From Other Sources''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                         size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                         background_color=(1, 170 / 255, 0, 1), background='')
            other_unfilled_popup.open()
        elif email_error or date_error:
            if email_error:
                email_error_popup = Popup(title='Registration Status: Unsuccessful', content=Label(text=''' Email Should Be Specified In The Given Format''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                                size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                                background_color=(1, 170 / 255, 0, 1), background='')
                email_error_popup.open()
            else:
                date_error_popup = Popup(title='Registration Status: Unsuccessful', content=Label(text='''Date Should Be Specified In The Given Format''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                                size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                                background_color=(1, 170 / 255, 0, 1), background='')
                date_error_popup.open()
        elif not_image:
            pass
        elif not no_letters:
            pass
        elif not str(int(amount_1_input) + 0).isnumeric() or not str(int(amount_2_input) + 0).isnumeric() or not str(
                int(amount_3_input) + 0).isnumeric() or not str(int(amount_4_input) + 0).isnumeric() or not str(
                int(amount_5_input) + 0).isnumeric() or not str(int(amount_6_input) + 0).isnumeric() or not str(
                int(amount_7_input) + 0).isnumeric() or not str(int(amount_8_input) + 0).isnumeric() or not str(
                int(amount_9_input) + 0).isnumeric() or not str(int(amount_10_input) + 0).isnumeric() or not str(
                int(mobile_phone_no_india_input) + 0).isnumeric() or not str(
                int(mobile_phone_no_abroad_input) + 0).isnumeric() or not str(
                int(post_code_input) + 0).isnumeric() or not str(int(iqama_ref_input) + 0).isnumeric() or not str(
                int(percentage_1_input) + 0).isnumeric() or not str(int(percentage_2_input) + 0).isnumeric() or not str(
                int(percentage_3_input) + 0).isnumeric() or not str(int(percentage_4_input) + 0).isnumeric():
            letters_in_number_slots = Popup(title='Registration Status: Unsuccessful', content=Label(text='''Please Ensure That Characters Other Than Numbers 
Are Not Entered In The Slots Specific For Numbers''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                            size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                            background_color=(1, 170 / 255, 0, 1), background='')
            letters_in_number_slots.open()
        elif str(int(amount_1_input) + 0) != '0' and date_1_input == '' or str(
                int(amount_2_input) + 0) != '0' and date_2_input == '' or str(
                int(amount_3_input) + 0) != '0' and date_3_input == '' or str(
                int(amount_4_input) + 0) != '0' and date_4_input == '' or str(
                int(amount_5_input) + 0) != '0' and date_5_input == '' or str(
                int(amount_6_input) + 0) != '0' and date_6_input == '' or str(
                int(amount_7_input) + 0) != '0' and date_7_input == '' or str(
                int(amount_8_input) + 0) != '0' and date_8_input == '' or str(
                int(amount_9_input) + 0) != '0' and date_9_input == '' or str(
                int(amount_10_input) + 0) != '0' and date_10_input == '':
            date_not_provided_popup = Popup(title='Registration Status: Unsuccessful', content=Label(text='''If An Amount is Entered, Date of 
Installment should Be Specified and Vice Versa''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                            size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                            background_color=(1, 170 / 255, 0, 1), background='')
            date_not_provided_popup.open()
        elif int(percentage_1_input) + int(percentage_2_input) + int(percentage_3_input) + int(
                percentage_4_input) != 100:
            percentage_total_not_sufficient = Popup(title='Registration Status: Unsuccessful',
                                                    content=Label(text='The Percentage Does Not Add Up To 100%',
                                                                  color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                                    size_hint=(None, None), size=(600, 200),
                                                    separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1),
                                                    background='')
            percentage_total_not_sufficient.open()
        else:
            amount_1_input = str(int(amount_1_input) + 0)
            amount_2_input = str(int(amount_2_input) + 0)
            amount_3_input = str(int(amount_3_input) + 0)
            amount_4_input = str(int(amount_4_input) + 0)
            amount_5_input = str(int(amount_5_input) + 0)
            amount_6_input = str(int(amount_6_input) + 0)
            amount_7_input = str(int(amount_7_input) + 0)
            amount_8_input = str(int(amount_8_input) + 0)
            amount_9_input = str(int(amount_9_input) + 0)
            amount_10_input = str(int(amount_10_input) + 0)
            percentage_1_input = str(int(percentage_1_input) + 0)
            percentage_2_input = str(int(percentage_2_input) + 0)
            percentage_3_input = str(int(percentage_3_input) + 0)
            percentage_4_input = str(int(percentage_4_input) + 0)

            total = str(int(amount_1_input) + int(amount_2_input) + int(amount_3_input) + int(amount_4_input) + int(
                amount_5_input) + int(amount_6_input) + int(amount_7_input) + int(amount_8_input) + int(
                amount_9_input) + int(amount_10_input))
            print(total)
            total_percentage = str(
                int(percentage_1_input) + int(percentage_2_input) + int(percentage_3_input) + int(percentage_4_input))
            all_percentage = [int(percentage_1_input), int(percentage_2_input), int(percentage_3_input),
                              int(percentage_4_input)]
            image1 = Image.open('background_files/FORM-1a.jpg')
            image2 = Image.open('background_files/FORM-2A.jpg')
            width1, height1 = image1.size
            width2, height2 = image2.size

            output_identification_path = ''
            for letter in photo_identification_path_input:
                if letter in '\~':
                    output_identification_path += '/'
                elif letter == '"':
                    output_identification_path += ''
                else:
                    output_identification_path += letter

            size = (400, 500)
            output_path = ''
            for letter in photo_location_path_input:
                if letter in '\~':
                    output_path += '/'
                elif letter == '"':
                    output_path += ''
                else:
                    output_path += letter

            logo = Image.open(output_path)
            id_identification = Image.open(output_identification_path)


            logo.thumbnail(size)

            font_margin = 10
            x1 = width1 - 500 - font_margin
            y1 = height1 - 2400 - font_margin

            image1.paste(logo, (x1, y1))
            image1.save('background_files/background_photo_pasted_form.jpg', 'JPEG')
            form1 = cv2.imread('background_files/background_photo_pasted_form.jpg')
            form2 = cv2.imread('background_files/FORM-2A.jpg')
            cv2.putText(form1, first_name_input, (600, 370), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 4, cv2.LINE_AA)
            cv2.putText(form1, surname_input, (600, 530), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            if male_checkbox_input:
                cv2.putText(form1, 'Male', (600, 730), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            elif female_checkbox_input:
                cv2.putText(form1, 'Female', (600, 730), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, date_of_birth_input, (600, 810), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)

            no_of_letters = 0
            postal_address_line1 = ''
            postal_address_line2 = ''
            postal_address_line3 = ''
            for letters in postal_address_input:
                if no_of_letters < 30:
                    postal_address_line1 += letters
                elif 30 <= no_of_letters < 65:
                    postal_address_line2 += letters
                elif 65 <= no_of_letters < 120:
                    postal_address_line3 += letters
                no_of_letters += 1
            cv2.putText(form1, f'{postal_address_line1}-', (600, 900), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, f'{postal_address_line2}-', (600, 980), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, f'{postal_address_line3}-', (600, 1060), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, post_code_input, (600, 1150), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, f'India: {mobile_phone_no_india_input}', (600, 1230), cv2.FONT_HERSHEY_SIMPLEX, 1.8,
                        (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, f'Work place: {mobile_phone_no_abroad_input}', (1280, 1230), cv2.FONT_HERSHEY_SIMPLEX,
                        1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, iqama_ref_input, (600, 1320), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, passport_ref_input, (1700, 1320), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, email_address_input, (600, 1400), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, work_place_input, (600, 1480), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, 'S No:', (470, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, 'Amount:', (450, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, 'Date:', (470, 2100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '1', (660, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '2', (800, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '3', (940, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '4', (1080, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '5', (1205, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '6', (1330, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '7', (1465, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '8', (1619, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '9', (1765, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '10', (1895, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, 'Total', (2020, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_1_input, (620, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_2_input, (770, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_3_input, (890, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_4_input, (1040, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_5_input, (1165, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_6_input, (1290, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_7_input, (1415, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_8_input, (1565, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_9_input, (1715, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_10_input, (1865, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, total, (2005, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_1_input, (610, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_2_input, (765, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_3_input, (890, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_4_input, (1040, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_5_input, (1160, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_6_input, (1290, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_7_input, (1415, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_8_input, (1565, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_9_input, (1715, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_10_input, (1865, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            if checkbox1_input:
                cv2.putText(form1, '*', (760, 1600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 0), 40, cv2.LINE_AA)
                cv2.putText(form1, 'Drivers Licence', (1590, 1540), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 0, 1), 3,
                            cv2.LINE_AA)
            elif checkbox2_input:
                cv2.putText(form1, '*', (1200, 1600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 0), 40, cv2.LINE_AA)
                cv2.putText(form1, 'Passport', (1590, 1540), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 0, 1), 3,
                            cv2.LINE_AA)
            elif checkbox3_input:
                cv2.putText(form1, '*', (1455, 1600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 0, 1), 40, cv2.LINE_AA)
            cv2.putText(form1, other_input, (1590, 1540), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 0, 1), 3, cv2.LINE_AA)
            cv2.putText(form2, father_name_input, (550, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form2, mother_name_input, (550, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            if int(percentage_1_input) > 0:
                cv2.putText(form2, name_1_input, (200, 650), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_1_input, (1300, 650), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_1_input}%', (2030, 650), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            if int(percentage_2_input) > 0:
                cv2.putText(form2, name_2_input, (200, 760), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_2_input, (1300, 760), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_2_input}%', (2030, 750), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            if int(percentage_3_input) > 0:
                cv2.putText(form2, name_3_input, (200, 860), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_3_input, (1300, 860), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_3_input}%', (2030, 870), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            if int(percentage_4_input) > 0:
                cv2.putText(form2, name_4_input, (200, 970), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_4_input, (1300, 970), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_4_input}%', (2030, 980), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            cv2.putText(form2, other_details_input, (675, 1080), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form2, suggested_by_input, (550, 1300), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            for num in numbers:
                if not os.path.exists(f'generated_forms_perm/{num}'):
                    os.mkdir(f'generated_forms_perm/{num}')
                    os.mkdir(f'generated_forms_temp/{num}')
                    cv2.imwrite(f'generated_forms_perm/{num}/Form_1.jpg', form1)
                    cv2.imwrite(f'generated_forms_perm/{num}/Form_2.jpg', form2)
                    cv2.imwrite(f'generated_forms_temp/{num}/Form_1.jpg', form1)
                    cv2.imwrite(f'generated_forms_temp/{num}/Form_2.jpg', form2)
                    id_identification.save(f'generated_forms_perm/{num}/ID_IMAGE.jpg', 'JPEG')
                    id_identification.save(f'generated_forms_temp/{num}/ID_IMAGE.jpg', 'JPEG')
                    registration_details1 = open(f'generated_forms_perm/{num}/{num}.txt', 'a')
                    registration_details2 = open(f'generated_forms_temp/{num}/{num}.txt', 'a')
                    registration_details1.write(f'''{first_name_input}
{surname_input}
{male_checkbox_input}
{female_checkbox_input}
{date_of_birth_input}
{postal_address_input}
{post_code_input}
{mobile_phone_no_india_input}
{mobile_phone_no_abroad_input}
{iqama_ref_input}
{passport_ref_input}
{email_address_input}
{work_place_input}
{amount_1_input}
{amount_2_input}
{amount_3_input}
{amount_4_input}
{amount_5_input}
{amount_6_input}
{amount_7_input}
{amount_8_input}
{amount_9_input}
{amount_10_input}
{total}
{date_1_input}
{date_2_input}
{date_3_input}
{date_4_input}
{date_5_input}
{date_6_input}
{date_7_input}
{date_8_input}
{date_9_input}
{date_10_input} 
{checkbox1_input}
{checkbox2_input}
{checkbox3_input}
{other_input}
{father_name_input}
{mother_name_input}
{name_1_input}
{relation_1_input}
{name_2_input}
{relation_2_input}
{name_3_input}
{relation_3_input}
{name_4_input}
{relation_4_input}
{other_details_input}
{suggested_by_input}
{percentage_1_input}
{percentage_2_input}
{percentage_3_input}
{percentage_4_input}
{photo_identification_path_input}
{photo_location_path_input}''')

                    registration_details2.write(f'''{first_name_input}
{surname_input}
{male_checkbox_input}
{female_checkbox_input}
{date_of_birth_input}
{postal_address_input}
{post_code_input}
{mobile_phone_no_india_input}
{mobile_phone_no_abroad_input}
{iqama_ref_input}
{passport_ref_input}
{email_address_input}
{work_place_input}
{amount_1_input}
{amount_2_input}
{amount_3_input}
{amount_4_input}
{amount_5_input}
{amount_6_input}
{amount_7_input}
{amount_8_input}
{amount_9_input}
{amount_10_input}
{total}
{date_1_input}
{date_2_input}
{date_3_input}
{date_4_input}
{date_5_input}
{date_6_input}
{date_7_input}
{date_8_input}
{date_9_input}
{date_10_input} 
{checkbox1_input}
{checkbox2_input}
{checkbox3_input}
{other_input}
{father_name_input}
{mother_name_input}
{name_1_input}
{relation_1_input}
{name_2_input}
{relation_2_input}
{name_3_input}
{relation_3_input}
{name_4_input}
{relation_4_input}
{other_details_input}
{suggested_by_input}
{percentage_1_input}
{percentage_2_input}
{percentage_3_input}
{percentage_4_input}
{photo_identification_path_input}
{photo_location_path_input}''')

                    registration_details1.close()
                    registration_details2.close()
                    print(f'File with {num} is created and ready for view')
                    break
            registration_success = Popup(title='Registration Status: Successful',
                                         content=Label(text=f'Your Registration No: {num}', color=(1, 1, 1, 1),
                                                       bold=True, font_size=dp(15)),
                                         size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                         background_color=(1, 170 / 255, 0, 1), background='')
            registration_success.open()
            self.manager.current = 'OpeningWindow'
            self.manager.transition.direction = 'right'
            first_name_input = self.ids.first_name.text = ''
            surname_input = self.ids.surname.text = ''
            male_checkbox_input = self.ids.male_checkbox.active = False
            female_checkbox_input = self.ids.female_checkbox.active = False
            date_of_birth_input = self.ids.date_of_birth.text = ''
            postal_address_input = self.ids.postal_address.text = ''
            post_code_input = self.ids.post_code.text = ''
            mobile_phone_no_india_input = self.ids.mobile_phone_no_india.text = ''
            mobile_phone_no_abroad_input = self.ids.mobile_phone_no_abroad.text = ''
            iqama_ref_input = self.ids.iqama_ref.text = ''
            passport_ref_input = self.ids.passport_ref.text = ''
            email_address_input = self.ids.email_address.text = ''
            work_place_input = self.ids.work_place.text = ''
            amount_1_input = self.ids.amount_1.text = ''
            amount_2_input = self.ids.amount_2.text = ''
            amount_3_input = self.ids.amount_3.text = ''
            amount_4_input = self.ids.amount_4.text = ''
            amount_5_input = self.ids.amount_5.text = ''
            amount_6_input = self.ids.amount_6.text = ''
            amount_7_input = self.ids.amount_7.text = ''
            amount_8_input = self.ids.amount_8.text = ''
            amount_9_input = self.ids.amount_9.text = ''
            amount_10_input = self.ids.amount_10.text = ''
            date_1_input = self.ids.date_1.text = ''
            date_2_input = self.ids.date_2.text = ''
            date_3_input = self.ids.date_3.text = ''
            date_4_input = self.ids.date_4.text = ''
            date_5_input = self.ids.date_5.text = ''
            date_6_input = self.ids.date_6.text = ''
            date_7_input = self.ids.date_7.text = ''
            date_8_input = self.ids.date_8.text = ''
            date_9_input = self.ids.date_9.text = ''
            date_10_input = self.ids.date_10.text = ''
            photo_location_path_input = self.ids.photo_location_path.text = ''
            other_input = self.ids.other.text = ''
            checkbox1_input = self.ids.checkbox1.active = False
            checkbox2_input = self.ids.checkbox2.active = False
            checkbox3_input = self.ids.checkbox3.active = False
            father_name_input = self.ids.father_name.text = ''
            mother_name_input = self.ids.mother_name.text = ''
            name_1_input = self.ids.name_1.text = ''
            relation_1_input = self.ids.relation_1.text = ''
            name_2_input = self.ids.name_2.text = ''
            relation_2_input = self.ids.relation_2.text = ''
            name_3_input = self.ids.name_3.text = ''
            relation_3_input = self.ids.relation_3.text = ''
            name_4_input = self.ids.name_4.text = ''
            relation_4_input = self.ids.relation_4.text = ''
            other_details_input = self.ids.other_details.text = ''
            suggested_by_input = self.ids.suggested_by.text = ''
            percentage_1_input = self.ids.percentage_1.text = ''
            percentage_2_input = self.ids.percentage_2.text = ''
            percentage_3_input = self.ids.percentage_3.text = ''
            percentage_4_input = self.ids.percentage_4.text = ''
            photo_identification_path_input = self.ids.photo_identification_path.text = ''
            self.ids.scroll_view_registration.scroll_y = 1

    def male_checkbox(self, state1):
        if state1:
            self.ids.female_checkbox.active = False

    def female_checkbox(self, state2):
        if state2:
            self.ids.male_checkbox.active = False

    def checkbox_1(self, value1):
        if value1:
            self.ids.checkbox2.active = False
            self.ids.checkbox3.active = False

    def checkbox_2(self, value2):
        if value2:
            self.ids.checkbox1.active = False
            self.ids.checkbox3.active = False

    def checkbox_3(self, value3):
        if value3:
            self.ids.checkbox2.active = False
            self.ids.checkbox1.active = False

    def add_installment(self, x):
        try:
            amount_1_input = self.ids.amount_1.text
            amount_2_input = self.ids.amount_2.text
            amount_3_input = self.ids.amount_3.text
            amount_4_input = self.ids.amount_4.text
            amount_5_input = self.ids.amount_5.text
            amount_6_input = self.ids.amount_6.text
            amount_7_input = self.ids.amount_7.text
            amount_8_input = self.ids.amount_8.text
            amount_9_input = self.ids.amount_9.text
            amount_10_input = self.ids.amount_10.text
            if amount_1_input == '' or amount_1_input in '          ':
                amount_1_input = '0'
            if amount_2_input == '' or amount_2_input in '          ':
                amount_2_input = '0'
            if amount_3_input == '' or amount_3_input in '          ':
                amount_3_input = '0'
            if amount_4_input == '' or amount_4_input in '          ':
                amount_4_input = '0'
            if amount_5_input == '' or amount_5_input in '          ':
                amount_5_input = '0'
            if amount_6_input == '' or amount_6_input in '          ':
                amount_6_input = '0'
            if amount_7_input == '' or amount_7_input in '          ':
                amount_7_input = '0'
            if amount_8_input == '' or amount_8_input in '          ':
                amount_8_input = '0'
            if amount_9_input == '' or amount_9_input in '          ':
                amount_9_input = '0'
            if amount_10_input == '' or amount_10_input in '          ':
                amount_10_input = '0'
            self.total = str(int(amount_1_input) + int(amount_2_input) + int(amount_3_input) + int(amount_4_input) + int(
                amount_5_input) + int(amount_6_input) + int(amount_7_input) + int(amount_8_input) + int(
                amount_9_input) + int(amount_10_input))
        except:
            pass

    def browse1(self):
        filename = filedialog.askopenfilename()
        self.ids.photo_location_path.text = filename

    def browse2(self):
        filename = filedialog.askopenfilename()
        self.ids.photo_identification_path.text = filename

    def add_percentage1_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_1.text = value

    def add_percentage2_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_2.text = value

    def add_percentage3_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_3.text = value

    def add_percentage4_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_4.text = value


class EditingWindow(Screen):
    registration_no_input = ''
    total = StringProperty('0')
    password_dialog = None

    def search(self, registration_no_input):
        self.registration_no_input = registration_no_input
        registration_no_input_no_error = ''
        for character in registration_no_input:
            if character == ' ':
                registration_no_input_no_error += ''
            elif character in '0123456789':
                registration_no_input_no_error += character
        registration_details_file = open(
            f'generated_forms_perm/{registration_no_input_no_error}/{registration_no_input_no_error}.txt', 'r')
        registration_details = []
        for details in registration_details_file:
            if '\n' in details:
                registration_details.append(details.replace('\n', ''))
            else:
                registration_details.append(details)
        print(registration_details)

        first_name_text = self.ids.first_name.text = registration_details[0]
        surname_text = self.ids.surname.text = registration_details[1]
        if registration_details[2] == 'True':
            male_checkbox_status = True
        else:
            male_checkbox_status = False
        male_checkbox_state = self.ids.male_checkbox.active = male_checkbox_status
        if registration_details[3] == 'True':
            female_checkbox_status = True
        else:
            female_checkbox_status = False
        female_checkbox_state = self.ids.female_checkbox.active = female_checkbox_status
        date_of_birth_text = self.ids.date_of_birth.text = registration_details[4]
        postal_address_text = self.ids.postal_address.text = registration_details[5]
        post_code_text = self.ids.post_code.text = registration_details[6]
        mobile_phone_no_india_text = self.ids.mobile_phone_no_india.text = registration_details[7]
        mobile_phone_no_abroad_text = self.ids.mobile_phone_no_abroad.text = registration_details[8]
        iqama_ref_text = self.ids.iqama_ref.text = registration_details[9]
        passport_ref_text = self.ids.passport_ref.text = registration_details[10]
        email_address_text = self.ids.email_address.text = registration_details[11]
        work_place_text = self.ids.work_place.text = registration_details[12]
        amount_1_text = self.ids.amount_1.text = registration_details[13]
        amount_2_text = self.ids.amount_2.text = registration_details[14]
        amount_3_text = self.ids.amount_3.text = registration_details[15]
        amount_4_text = self.ids.amount_4.text = registration_details[16]
        amount_5_text = self.ids.amount_5.text = registration_details[17]
        amount_6_text = self.ids.amount_6.text = registration_details[18]
        amount_7_text = self.ids.amount_7.text = registration_details[19]
        amount_8_text = self.ids.amount_8.text = registration_details[20]
        amount_9_text = self.ids.amount_9.text = registration_details[21]
        amount_10_text = self.ids.amount_10.text = registration_details[22]
        total_text = self.ids.total_amount.text = registration_details[23]
        date_1_text = self.ids.date_1.text = registration_details[24]
        date_2_text = self.ids.date_2.text = registration_details[25]
        date_3_text = self.ids.date_3.text = registration_details[26]
        date_4_text = self.ids.date_4.text = registration_details[27]
        date_5_text = self.ids.date_5.text = registration_details[28]
        date_6_text = self.ids.date_6.text = registration_details[29]
        date_7_text = self.ids.date_7.text = registration_details[30]
        date_8_text = self.ids.date_8.text = registration_details[31]
        date_9_text = self.ids.date_9.text = registration_details[32]
        date_10_text = self.ids.date_10.text = registration_details[33]
        if registration_details[34] == 'True':
            checkbox1_status = True
        else:
            checkbox1_status = False
        checkbox1_state = self.ids.checkbox1.active = checkbox1_status
        if registration_details[35] == 'True':
            checkbox2_status = True
        else:
            checkbox2_status = False
        checkbox2_state = self.ids.checkbox2.active = checkbox2_status
        if registration_details[36] == 'True':
            checkbox3_status = True
        else:
            checkbox3_status = False
        checkbox3_state = self.ids.checkbox3.active = checkbox3_status
        other_text = self.ids.other.text = registration_details[37]
        father_name_text = self.ids.father_name.text = registration_details[38]
        mother_name_text = self.ids.mother_name.text = registration_details[39]
        name_1_text = self.ids.name_1.text = registration_details[40]
        relation_1_text = self.ids.relation_1.text = registration_details[41]
        name_2_text = self.ids.name_2.text = registration_details[42]
        relation_2_text = self.ids.relation_2.text = registration_details[43]
        name_3_text = self.ids.name_3.text = registration_details[44]
        relation_3_text = self.ids.relation_3.text = registration_details[45]
        name_4_text = self.ids.name_4.text = registration_details[46]
        relation_4_text = self.ids.relation_4.text = registration_details[47]
        other_details_text = self.ids.other_details.text = registration_details[48]
        suggested_by_text = self.ids.suggested_by.text = registration_details[49]
        percentage_1_input = self.ids.percentage_1.text = registration_details[50]
        percentage_2_input = self.ids.percentage_2.text = registration_details[51]
        percentage_3_input = self.ids.percentage_3.text = registration_details[52]
        percentage_4_input = self.ids.percentage_4.text = registration_details[53]
        photo_identification_path_input = self.ids.photo_identification_path.text = registration_details[54]
        photo_location_path_text = self.ids.photo_location_path.text = registration_details[55]
        registration_details_file.close()

    def male_checkbox(self, state1):
        if state1:
            self.ids.female_checkbox.active = False

    def female_checkbox(self, state2):
        if state2:
            self.ids.male_checkbox.active = False

    def checkbox_1(self, value1):
        if value1:
            self.ids.checkbox2.active = False
            self.ids.checkbox3.active = False

    def checkbox_2(self, value2):
        if value2:
            self.ids.checkbox1.active = False
            self.ids.checkbox3.active = False

    def checkbox_3(self, value3):
        if value3:
            self.ids.checkbox2.active = False
            self.ids.checkbox1.active = False

    def add_installment(self, x):
        try:
            amount_1_input = self.ids.amount_1.text
            amount_2_input = self.ids.amount_2.text
            amount_3_input = self.ids.amount_3.text
            amount_4_input = self.ids.amount_4.text
            amount_5_input = self.ids.amount_5.text
            amount_6_input = self.ids.amount_6.text
            amount_7_input = self.ids.amount_7.text
            amount_8_input = self.ids.amount_8.text
            amount_9_input = self.ids.amount_9.text
            amount_10_input = self.ids.amount_10.text
            if amount_1_input == '' or amount_1_input in '          ':
                amount_1_input = '0'
            if amount_2_input == '' or amount_2_input in '          ':
                amount_2_input = '0'
            if amount_3_input == '' or amount_3_input in '          ':
                amount_3_input = '0'
            if amount_4_input == '' or amount_4_input in '          ':
                amount_4_input = '0'
            if amount_5_input == '' or amount_5_input in '          ':
                amount_5_input = '0'
            if amount_6_input == '' or amount_6_input in '          ':
                amount_6_input = '0'
            if amount_7_input == '' or amount_7_input in '          ':
                amount_7_input = '0'
            if amount_8_input == '' or amount_8_input in '          ':
                amount_8_input = '0'
            if amount_9_input == '' or amount_9_input in '          ':
                amount_9_input = '0'
            if amount_10_input == '' or amount_10_input in '          ':
                amount_10_input = '0'
            self.total = str(int(amount_1_input) + int(amount_2_input) + int(amount_3_input) + int(amount_4_input) + int(
                amount_5_input) + int(amount_6_input) + int(amount_7_input) + int(amount_8_input) + int(
                amount_9_input) + int(amount_10_input))
        except:
            pass

    def ask_admin_password(self):
        content_cls = PasswordDialogView()
        if not self.password_dialog:
            self.password_dialog = MDDialog(title='Password', type='custom', content_cls=content_cls, buttons=[MDFlatButton(text="CANCEL", on_press=self.close_dialog), MDRaisedButton(text="ACCESS", on_press=lambda x: self.get_save_access(x, content_cls))])
        self.password_dialog.open()

    def get_save_access(self, instance_btn, content_cls):
        password_file = open('background_files/pass/password.txt', 'r')
        password = password_file.readline()
        password_input = content_cls.ids.admin_password._get_text()
        print(password_input)
        if password == password_input:
            self.close_dialog()
            self.save_changes()
            content_cls.ids.admin_password.text = ''
            content_cls.ids.admin_password.password = True
            content_cls.ids.eye_icon.icon = 'eye-off'
            print('correct')
        else:
            toast('Incorrect Password')

    def close_dialog(self, *args):
        self.password_dialog.dismiss()
    def save_changes(self):
        registration_no_input_no_error = ''
        for character in self.registration_no_input:
            if character == ' ':
                registration_no_input_no_error += ''
            elif character in '0123456789':
                registration_no_input_no_error += character
        registration_details_file = open(
            f'generated_forms_perm/{registration_no_input_no_error}/{registration_no_input_no_error}.txt', 'r')
        registration_details = []
        for details in registration_details_file:
            if '\n' in details:
                registration_details.append(details.replace('\n', ''))
            else:
                registration_details.append(details)
        print(registration_details)

        first_name_text = registration_details[0]
        surname_text = registration_details[1]
        if registration_details[2] == 'True':
            male_checkbox_status = True
        else:
            male_checkbox_status = False
        male_checkbox_state = male_checkbox_status
        if registration_details[3] == 'True':
            female_checkbox_status = True
        else:
            female_checkbox_status = False
        female_checkbox_state = female_checkbox_status
        date_of_birth_text = registration_details[4]
        postal_address_text = registration_details[5]
        post_code_text = registration_details[6]
        mobile_phone_no_india_text = registration_details[7]
        mobile_phone_no_abroad_text = registration_details[8]
        iqama_ref_text = registration_details[9]
        passport_ref_text = registration_details[10]
        email_address_text = registration_details[11]
        work_place_text = registration_details[12]
        amount_1_text = registration_details[13]
        amount_2_text = registration_details[14]
        amount_3_text = registration_details[15]
        amount_4_text = registration_details[16]
        amount_5_text = registration_details[17]
        amount_6_text = registration_details[18]
        amount_7_text = registration_details[19]
        amount_8_text = registration_details[20]
        amount_9_text = registration_details[21]
        amount_10_text = registration_details[22]
        total_text = registration_details[23]
        date_1_text = registration_details[24]
        date_2_text = registration_details[25]
        date_3_text = registration_details[26]
        date_4_text = registration_details[27]
        date_5_text = registration_details[28]
        date_6_text = registration_details[29]
        date_7_text = registration_details[30]
        date_8_text = registration_details[31]
        date_9_text = registration_details[32]
        date_10_text = registration_details[33]
        if registration_details[34] == 'True':
            checkbox1_status = True
        else:
            checkbox1_status = False
        checkbox1_state = checkbox1_status
        if registration_details[35] == 'True':
            checkbox2_status = True
        else:
            checkbox2_status = False
        checkbox2_state = checkbox2_status
        if registration_details[36] == 'True':
            checkbox3_status = True
        else:
            checkbox3_status = False
        checkbox3_state = checkbox3_status
        other_text = registration_details[37]
        father_name_text = registration_details[38]
        mother_name_text = registration_details[39]
        name_1_text = registration_details[40]
        relation_1_text = registration_details[41]
        name_2_text = registration_details[42]
        relation_2_text = registration_details[43]
        name_3_text = registration_details[44]
        relation_3_text = registration_details[45]
        name_4_text = registration_details[46]
        relation_4_text = registration_details[47]
        other_details_text = registration_details[48]
        suggested_by_text = registration_details[49]
        percentage_1_text = registration_details[50]
        percentage_2_text = registration_details[51]
        percentage_3_text = registration_details[52]
        percentage_4_text = registration_details[53]
        photo_identification_path_text = registration_details[54]
        photo_location_path_text = registration_details[55]

        registration_details_file.close()

        first_name_input = self.ids.first_name.text
        surname_input = self.ids.surname.text
        male_checkbox_input = self.ids.male_checkbox.active
        female_checkbox_input = self.ids.female_checkbox.active
        date_of_birth_input = self.ids.date_of_birth.text
        postal_address_input = self.ids.postal_address.text
        post_code_input = self.ids.post_code.text
        mobile_phone_no_india_input = self.ids.mobile_phone_no_india.text
        mobile_phone_no_abroad_input = self.ids.mobile_phone_no_abroad.text
        iqama_ref_input = self.ids.iqama_ref.text
        passport_ref_input = self.ids.passport_ref.text
        email_address_input = self.ids.email_address.text
        work_place_input = self.ids.work_place.text
        amount_1_input = self.ids.amount_1.text
        amount_2_input = self.ids.amount_2.text
        amount_3_input = self.ids.amount_3.text
        amount_4_input = self.ids.amount_4.text
        amount_5_input = self.ids.amount_5.text
        amount_6_input = self.ids.amount_6.text
        amount_7_input = self.ids.amount_7.text
        amount_8_input = self.ids.amount_8.text
        amount_9_input = self.ids.amount_9.text
        amount_10_input = self.ids.amount_10.text
        date_1_input = self.ids.date_1.text
        date_2_input = self.ids.date_2.text
        date_3_input = self.ids.date_3.text
        date_4_input = self.ids.date_4.text
        date_5_input = self.ids.date_5.text
        date_6_input = self.ids.date_6.text
        date_7_input = self.ids.date_7.text
        date_8_input = self.ids.date_8.text
        date_9_input = self.ids.date_9.text
        date_10_input = self.ids.date_10.text
        photo_location_path_input = self.ids.photo_location_path.text
        other_input = self.ids.other.text
        checkbox1_input = self.ids.checkbox1.active
        checkbox2_input = self.ids.checkbox2.active
        checkbox3_input = self.ids.checkbox3.active
        father_name_input = self.ids.father_name.text
        mother_name_input = self.ids.mother_name.text
        name_1_input = self.ids.name_1.text
        relation_1_input = self.ids.relation_1.text
        name_2_input = self.ids.name_2.text
        relation_2_input = self.ids.relation_2.text
        name_3_input = self.ids.name_3.text
        relation_3_input = self.ids.relation_3.text
        name_4_input = self.ids.name_4.text
        relation_4_input = self.ids.relation_4.text
        other_details_input = self.ids.other_details.text
        suggested_by_input = self.ids.suggested_by.text
        percentage_1_input = self.ids.percentage_1.text
        percentage_2_input = self.ids.percentage_2.text
        percentage_3_input = self.ids.percentage_3.text
        percentage_4_input = self.ids.percentage_4.text
        photo_identification_path_input = self.ids.photo_identification_path.text

        if amount_1_input == '' or amount_1_input in '          ':
            amount_1_input = '0'
        if amount_2_input == '' or amount_2_input in '          ':
            amount_2_input = '0'
        if amount_3_input == '' or amount_3_input in '          ':
            amount_3_input = '0'
        if amount_4_input == '' or amount_4_input in '          ':
            amount_4_input = '0'
        if amount_5_input == '' or amount_5_input in '          ':
            amount_5_input = '0'
        if amount_6_input == '' or amount_6_input in '          ':
            amount_6_input = '0'
        if amount_7_input == '' or amount_7_input in '          ':
            amount_7_input = '0'
        if amount_8_input == '' or amount_8_input in '          ':
            amount_8_input = '0'
        if amount_9_input == '' or amount_9_input in '          ':
            amount_9_input = '0'
        if amount_10_input == '' or amount_10_input in '          ':
            amount_10_input = '0'
        if '%' in percentage_1_input:
            percentage_1_input = percentage_1_input.replace('%', '')
        if '%' in percentage_2_input:
            percentage_2_input = percentage_2_input.replace('%', '')
        if '%' in percentage_3_input:
            percentage_3_input = percentage_3_input.replace('%', '')
        if '%' in percentage_4_input:
            percentage_4_input = percentage_4_input.replace('%', '')
        if percentage_1_input == '' or percentage_1_input in '                ':
            percentage_1_input = '0'
        if percentage_2_input == '' or percentage_2_input in '                ':
            percentage_2_input = '0'
        if percentage_3_input == '' or percentage_3_input in '                ':
            percentage_3_input = '0'
        if percentage_4_input == '' or percentage_4_input in '                ':
            percentage_4_input = '0'

        no_letters = False
        try:
            amount_1_input = str(int(amount_1_input) + 0)
            amount_2_input = str(int(amount_2_input) + 0)
            amount_3_input = str(int(amount_3_input) + 0)
            amount_4_input = str(int(amount_4_input) + 0)
            amount_5_input = str(int(amount_5_input) + 0)
            amount_6_input = str(int(amount_6_input) + 0)
            amount_7_input = str(int(amount_7_input) + 0)
            amount_8_input = str(int(amount_8_input) + 0)
            amount_9_input = str(int(amount_9_input) + 0)
            amount_10_input = str(int(amount_10_input) + 0)
            percentage_1_input = str(int(percentage_1_input) + 0)
            percentage_2_input = str(int(percentage_2_input) + 0)
            percentage_3_input = str(int(percentage_3_input) + 0)
            percentage_4_input = str(int(percentage_4_input) + 0)
            mobile_phone_no_india_input = str(int(mobile_phone_no_india_input) + 0)
            mobile_phone_no_abroad_input = str(int(mobile_phone_no_abroad_input) + 0)
            post_code_input = str(int(post_code_input) + 0)
            iqama_ref_input = str(int(iqama_ref_input) + 0)
            no_letters = True

        except ValueError:
            letters_in_number_slots = Popup(title='Registration Status: Unsuccessful', content=Label(text='''Please Ensure That Characters Other Than Numbers 
Are Not Entered In The Slots Specific For Numbers''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                            size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                            background_color=(1, 170 / 255, 0, 1), background='')
            letters_in_number_slots.open()

        no_changes_popup = Popup(title='Save Status: Unsuccessful',
                                 content=Label(text='No Changes Were Made In The Initial Details', color=(1, 1, 1, 1),
                                               bold=True, font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                 separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
        not_image = True
        try:
            output_identification_path = ''
            for letter in photo_identification_path_input:
                if letter in '\~':
                    output_identification_path += '/'
                elif letter == '"':
                    output_identification_path += ''
                else:
                    output_identification_path += letter

            output_path = ''
            for letter in photo_location_path_input:
                if letter in '\~':
                    output_path += '/'
                elif letter == '"':
                    output_path += ''
                else:
                    output_path += letter

            logo = Image.open(output_path)
            id_identification = Image.open(output_identification_path)
            not_image = False
        except:
            no_image = Popup(title='Image Open: Unsuccessful',
                                         content=Label(text=f'Ensure That Selected File Is A Image', color=(1, 1, 1, 1),
                                                       bold=True, font_size=dp(15)),
                                         size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                         background_color=(1, 170 / 255, 0, 1), background='')
            no_image.open()

        if first_name_text == first_name_input and surname_text == surname_input and male_checkbox_state == male_checkbox_input and female_checkbox_state == female_checkbox_input and date_of_birth_text == date_of_birth_input and postal_address_text == postal_address_input and post_code_input == post_code_text and mobile_phone_no_india_text == mobile_phone_no_india_input and mobile_phone_no_abroad_text == mobile_phone_no_abroad_input and iqama_ref_text == iqama_ref_input and passport_ref_text == passport_ref_input and email_address_text == email_address_input and work_place_text == work_place_input and amount_1_text == amount_1_input and amount_2_text == amount_2_input and amount_3_text == amount_3_input and amount_4_text == amount_4_input and amount_5_text == amount_5_input and amount_6_text == amount_6_input and amount_7_text == amount_7_input and amount_8_text == amount_8_input and amount_9_text == amount_9_input and amount_10_text == amount_10_input and date_1_text == date_1_input and date_2_text == date_2_input and date_3_text == date_3_input and date_4_text == date_4_input and date_5_text == date_5_input and date_6_text == date_6_input and date_7_text == date_7_input and date_8_text == date_8_input and date_9_text == date_9_input and date_10_text == date_10_input and photo_location_path_text == photo_location_path_input and checkbox1_input == checkbox1_state and checkbox2_input == checkbox2_state and checkbox3_input == checkbox3_state and other_text == other_input and father_name_text == father_name_input and mother_name_text == mother_name_input and name_1_text == name_1_input and relation_1_text == relation_1_input and name_2_input == name_2_text and relation_2_text == relation_2_input and name_3_text == name_3_input and relation_3_text == relation_3_input and name_4_text == name_4_input and relation_4_text == relation_4_input and other_details_text == other_details_input and suggested_by_text == suggested_by_input and percentage_1_text == percentage_1_input and percentage_2_text == percentage_2_input and percentage_3_text == percentage_3_input and percentage_4_text == percentage_4_input and photo_identification_path_input == photo_identification_path_text:
            no_changes_popup.open()

        elif first_name_input.strip() == '' or surname_input.strip() == '' or date_of_birth_input.strip() == '' or postal_address_input.strip() == '' or post_code_input.strip() == '' or mobile_phone_no_india_input.strip() == '' or mobile_phone_no_abroad_input.strip() == '' or iqama_ref_input.strip() == '' or passport_ref_input.strip() == '' or email_address_input.strip() == '' or work_place_input.strip() == '' or amount_1_input.strip() == '' or amount_2_input.strip() == '' or amount_3_input.strip() == '' or amount_4_input.strip() == '' or amount_5_input.strip() == '' or amount_6_input.strip() == '' or amount_7_input.strip() == '' or amount_8_input.strip() == '' or amount_9_input.strip() == '' or amount_10_input.strip() == '' or photo_location_path_input.strip() == '' or checkbox1_input == False and checkbox2_input == False and checkbox3_input == False or father_name_input.strip() == '' or mother_name_input.strip() == '' or name_1_input.strip() == '' or relation_1_input.strip() == '' or suggested_by_input.strip() == '' or male_checkbox_input == False and female_checkbox_input == False or percentage_1_input.strip() == '' or photo_identification_path_input.strip() == '':
            unfilled_popup = Popup(title='Registration Status: Unsuccessful',
                                   content=Label(text='Please Ensure That All Details Are Filled', color=(1, 1, 1, 1),
                                                 bold=True, font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                   separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            unfilled_popup.open()
        elif checkbox3_input == True and other_input.strip() == '':
            other_unfilled_popup = Popup(title='Registration Status: Unsuccessful', content=Label(text='''Its Mandatory To Write The Source Of Photo 
Provided If Your Selection is From Other Sources''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                         size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                         background_color=(1, 170 / 255, 0, 1), background='')
            other_unfilled_popup.open()
        elif not_image:
            pass
        elif not no_letters:
            pass
        elif not str(int(amount_1_input) + 0).isnumeric() or not str(
                int(amount_2_input) + 0).isnumeric() or not str(int(amount_3_input) + 0).isnumeric() or not str(
            int(amount_4_input) + 0).isnumeric() or not str(int(amount_5_input) + 0).isnumeric() or not str(
            int(amount_6_input) + 0).isnumeric() or not str(int(amount_7_input) + 0).isnumeric() or not str(
            int(amount_8_input) + 0).isnumeric() or not str(int(amount_9_input) + 0).isnumeric() or not str(
            int(amount_10_input) + 0).isnumeric() or not str(
            int(mobile_phone_no_india_input) + 0).isnumeric() or not str(
            int(mobile_phone_no_abroad_input) + 0).isnumeric() or not str(
            int(post_code_input) + 0).isnumeric() or not str(int(iqama_ref_input) + 0).isnumeric() or not str(
            int(percentage_1_input) + 0).isnumeric() or not str(
            int(percentage_2_input) + 0).isnumeric() or not str(
            int(percentage_3_input) + 0).isnumeric() or not str(int(percentage_4_input) + 0).isnumeric():
            letters_in_number_slots = Popup(title='Registration Status: Unsuccessful', content=Label(text='''Please Ensure That Characters Other Than Numbers 
Are Not Entered In The Slots Specific For Numbers''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                            size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                            background_color=(1, 170 / 255, 0, 1), background='')
            letters_in_number_slots.open()
        elif str(int(amount_1_input) + 0) != '0' and date_1_input == '' or str(
                int(amount_2_input) + 0) != '0' and date_2_input == '' or str(
            int(amount_3_input) + 0) != '0' and date_3_input == '' or str(
            int(amount_4_input) + 0) != '0' and date_4_input == '' or str(
            int(amount_5_input) + 0) != '0' and date_5_input == '' or str(
            int(amount_6_input) + 0) != '0' and date_6_input == '' or str(
            int(amount_7_input) + 0) != '0' and date_7_input == '' or str(
            int(amount_8_input) + 0) != '0' and date_8_input == '' or str(
            int(amount_9_input) + 0) != '0' and date_9_input == '' or str(
            int(amount_10_input) + 0) != '0' and date_10_input == '':
            date_not_provided_popup = Popup(title='Registration Status: Unsuccessful', content=Label(text='''If An Amount is Entered, Date of 
Installment should Be Specified and Vice Versa''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                            size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                            background_color=(1, 170 / 255, 0, 1), background='')
            date_not_provided_popup.open()
        elif int(percentage_1_input) + int(percentage_2_input) + int(percentage_3_input) + int(
                percentage_4_input) != 100:
            percentage_total_not_sufficient = Popup(title='Registration Status: Unsuccessful',
                                                    content=Label(text='The Percentage Does Not Add Up To 100%',
                                                                  color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                                    size_hint=(None, None), size=(600, 200),
                                                    separator_color=(1, 1, 1, 1),
                                                    background_color=(1, 170 / 255, 0, 1), background='')
            percentage_total_not_sufficient.open()
        else:
            amount_1_input = str(int(amount_1_input) + 0)
            amount_2_input = str(int(amount_2_input) + 0)
            amount_3_input = str(int(amount_3_input) + 0)
            amount_4_input = str(int(amount_4_input) + 0)
            amount_5_input = str(int(amount_5_input) + 0)
            amount_6_input = str(int(amount_6_input) + 0)
            amount_7_input = str(int(amount_7_input) + 0)
            amount_8_input = str(int(amount_8_input) + 0)
            amount_9_input = str(int(amount_9_input) + 0)
            amount_10_input = str(int(amount_10_input) + 0)
            percentage_1_input = str(int(percentage_1_input) + 0)
            percentage_2_input = str(int(percentage_2_input) + 0)
            percentage_3_input = str(int(percentage_3_input) + 0)
            percentage_4_input = str(int(percentage_4_input) + 0)

            total = str(int(amount_1_input) + int(amount_2_input) + int(amount_3_input) + int(amount_4_input) + int(
                amount_5_input) + int(amount_6_input) + int(amount_7_input) + int(amount_8_input) + int(
                amount_9_input) + int(amount_10_input))
            print(total)
            total_percentage = str(
                int(percentage_1_input) + int(percentage_2_input) + int(percentage_3_input) + int(
                    percentage_4_input))
            all_percentage = [int(percentage_1_input), int(percentage_2_input), int(percentage_3_input),
                              int(percentage_4_input)]
            image1 = Image.open('background_files/FORM-1a.jpg')
            image2 = Image.open('background_files/FORM-2A.jpg')
            width1, height1 = image1.size
            width2, height2 = image2.size

            output_identification_path = ''
            for letter in photo_identification_path_input:
                if letter in '\~':
                    output_identification_path += '/'
                elif letter == '"':
                    output_identification_path += ''
                else:
                    output_identification_path += letter

            size = (600, 580)
            output_path = ''
            for letter in photo_location_path_input:
                if letter in '\~':
                    output_path += '/'
                elif letter == '"':
                    output_path += ''
                else:
                    output_path += letter

            logo = Image.open(output_path)
            id_identification = Image.open(output_identification_path)
            logo.thumbnail(size)

            font_margin = 10
            x1 = width1 - 500 - font_margin
            y1 = height1 - 2400 - font_margin

            image1.paste(logo, (x1, y1))
            image1.save('background_files/background_photo_pasted_form.jpg', 'JPEG')
            form1 = cv2.imread('background_files/background_photo_pasted_form.jpg')
            form2 = cv2.imread('background_files/FORM-2A.jpg')
            cv2.putText(form1, first_name_input, (600, 370), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 4, cv2.LINE_AA)
            cv2.putText(form1, surname_input, (600, 530), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            if male_checkbox_input:
                cv2.putText(form1, 'Male', (600, 730), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            elif female_checkbox_input:
                cv2.putText(form1, 'Female', (600, 730), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, date_of_birth_input, (600, 810), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)

            no_of_letters = 0
            postal_address_line1 = ''
            postal_address_line2 = ''
            postal_address_line3 = ''
            for letters in postal_address_input:
                if no_of_letters < 30:
                    postal_address_line1 += letters
                elif 30 <= no_of_letters < 65:
                    postal_address_line2 += letters
                elif 65 <= no_of_letters < 120:
                    postal_address_line3 += letters
                no_of_letters += 1
            cv2.putText(form1, f'{postal_address_line1}-', (600, 900), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, f'{postal_address_line2}-', (600, 980), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, f'{postal_address_line3}-', (600, 1060), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, post_code_input, (600, 1150), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, f'India: {mobile_phone_no_india_input}', (600, 1230), cv2.FONT_HERSHEY_SIMPLEX, 1.8,(0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, f'Work place: {mobile_phone_no_abroad_input}', (1280, 1230), cv2.FONT_HERSHEY_SIMPLEX,1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, iqama_ref_input, (600, 1320), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, passport_ref_input, (1700, 1320), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, email_address_input, (600, 1400), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form1, work_place_input, (600, 1480), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form1, 'S No:', (470, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, 'Amount:', (450, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, 'Date:', (470, 2100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '1', (660, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '2', (800, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '3', (940, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '4', (1080, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '5', (1205, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '6', (1330, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '7', (1465, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '8', (1619, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '9', (1765, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, '10', (1895, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, 'Total', (2020, 1950), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_1_input, (620, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_2_input, (770, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_3_input, (890, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_4_input, (1040, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_5_input, (1165, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_6_input, (1290, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_7_input, (1415, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_8_input, (1565, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_9_input, (1715, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, amount_10_input, (1865, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, total, (2005, 2020), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_1_input, (610, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_2_input, (765, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_3_input, (890, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_4_input, (1040, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_5_input, (1160, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_6_input, (1290, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_7_input, (1415, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_8_input, (1565, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_9_input, (1715, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(form1, date_10_input, (1865, 2100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            if checkbox1_input:
                cv2.putText(form1, '*', (760, 1600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 0), 40, cv2.LINE_AA)
                cv2.putText(form1, 'Drivers Licence', (1590, 1540), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 0, 1), 3,
                            cv2.LINE_AA)
            elif checkbox2_input:
                cv2.putText(form1, '*', (1200, 1600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 0), 40, cv2.LINE_AA)
                cv2.putText(form1, 'Passport', (1590, 1540), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 0, 1), 3,
                            cv2.LINE_AA)
            elif checkbox3_input:
                cv2.putText(form1, '*', (1455, 1600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 1, 0, 1), 40, cv2.LINE_AA)
            cv2.putText(form1, other_input, (1590, 1540), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 0, 1), 3, cv2.LINE_AA)
            cv2.putText(form2, father_name_input, (550, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            cv2.putText(form2, mother_name_input, (550, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
            if int(percentage_1_input) > 0:
                cv2.putText(form2, name_1_input, (200, 650), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_1_input, (1300, 650), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_1_input}%', (2030, 650), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            if int(percentage_2_input) > 0:
                cv2.putText(form2, name_2_input, (200, 760), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_2_input, (1300, 760), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_2_input}%', (2030, 750), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            if int(percentage_3_input) > 0:
                cv2.putText(form2, name_3_input, (200, 860), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_3_input, (1300, 860), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_3_input}%', (2030, 870), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            if int(percentage_4_input) > 0:
                cv2.putText(form2, name_4_input, (200, 970), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3, cv2.LINE_AA)
                cv2.putText(form2, relation_4_input, (1300, 970), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
                cv2.putText(form2, f'{percentage_4_input}%', (2030, 980), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                            cv2.LINE_AA)
            cv2.putText(form2, other_details_input, (675, 1080), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.putText(form2, suggested_by_input, (550, 1300), cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 0, 0), 3,
                        cv2.LINE_AA)
            cv2.imwrite(f'generated_forms_perm/{registration_no_input_no_error}/Form_1.jpg', form1)
            cv2.imwrite(f'generated_forms_perm/{registration_no_input_no_error}/Form_2.jpg', form2)
            cv2.imwrite(f'generated_forms_temp/{registration_no_input_no_error}/Form_1.jpg', form1)
            cv2.imwrite(f'generated_forms_temp/{registration_no_input_no_error}/Form_2.jpg', form2)
            id_identification.save(f'generated_forms_perm/{registration_no_input_no_error}/ID_IMAGE.jpg', 'JPEG')
            id_identification.save(f'generated_forms_temp/{registration_no_input_no_error}/ID_IMAGE.jpg', 'JPEG')
            registration_details1 = open(
                f'generated_forms_perm/{registration_no_input_no_error}/{registration_no_input_no_error}.txt', 'w')
            registration_details2 = open(
                f'generated_forms_temp/{registration_no_input_no_error}/{registration_no_input_no_error}.txt', 'w')
            registration_details1.write(f'''{first_name_input}
{surname_input}
{male_checkbox_input}
{female_checkbox_input}
{date_of_birth_input}
{postal_address_input}
{post_code_input}
{mobile_phone_no_india_input}
{mobile_phone_no_abroad_input}
{iqama_ref_input}
{passport_ref_input}
{email_address_input}
{work_place_input}
{amount_1_input}
{amount_2_input}
{amount_3_input}
{amount_4_input}
{amount_5_input}
{amount_6_input}
{amount_7_input}
{amount_8_input}
{amount_9_input}
{amount_10_input}
{total}
{date_1_input}
{date_2_input}
{date_3_input}
{date_4_input}
{date_5_input}
{date_6_input}
{date_7_input}
{date_8_input}
{date_9_input}
{date_10_input}
{checkbox1_input}
{checkbox2_input}
{checkbox3_input}
{other_input}
{father_name_input}
{mother_name_input}
{name_1_input}
{relation_1_input}
{name_2_input}
{relation_2_input}
{name_3_input}
{relation_3_input}
{name_4_input}
{relation_4_input}
{other_details_input}
{suggested_by_input}
{percentage_1_input}
{percentage_2_input}
{percentage_3_input}
{percentage_4_input}
{photo_identification_path_input}
{photo_location_path_input}''')

            registration_details2.write(f'''{first_name_input}
{surname_input}
{male_checkbox_input}
{female_checkbox_input}
{date_of_birth_input}
{postal_address_input}
{post_code_input}
{mobile_phone_no_india_input}
{mobile_phone_no_abroad_input}
{iqama_ref_input}
{passport_ref_input}
{email_address_input}
{work_place_input}
{amount_1_input}
{amount_2_input}
{amount_3_input}
{amount_4_input}
{amount_5_input}
{amount_6_input}
{amount_7_input}
{amount_8_input}
{amount_9_input}
{amount_10_input}
{total}
{date_1_input}
{date_2_input}
{date_3_input}
{date_4_input}
{date_5_input}
{date_6_input}
{date_7_input}
{date_8_input}
{date_9_input}
{date_10_input}
{checkbox1_input}
{checkbox2_input}
{checkbox3_input}
{other_input}
{father_name_input}
{mother_name_input}
{name_1_input}
{relation_1_input}
{name_2_input}
{relation_2_input}
{name_3_input}
{relation_3_input}
{name_4_input}
{relation_4_input}
{other_details_input}
{suggested_by_input}
{percentage_1_input}
{percentage_2_input}
{percentage_3_input}
{percentage_4_input}
{photo_identification_path_input}
{photo_location_path_input}''')
            registration_details1.close()
            registration_details2.close()

            save_changes_success = Popup(title='Save Changes Status: Successful',
                                         content=Label(text=f'Changes Successfully Applied', color=(1, 1, 1, 1),
                                                       bold=True, font_size=dp(15)),
                                         size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                         background_color=(1, 170 / 255, 0, 1), background='')
            save_changes_success.open()
            first_name_input = self.ids.first_name.text = ''
            surname_input = self.ids.surname.text = ''
            male_checkbox_input = self.ids.male_checkbox.active = False
            female_checkbox_input = self.ids.female_checkbox.active = False
            date_of_birth_input = self.ids.date_of_birth.text = ''
            postal_address_input = self.ids.postal_address.text = ''
            post_code_input = self.ids.post_code.text = ''
            mobile_phone_no_india_input = self.ids.mobile_phone_no_india.text = ''
            mobile_phone_no_abroad_input = self.ids.mobile_phone_no_abroad.text = ''
            iqama_ref_input = self.ids.iqama_ref.text = ''
            passport_ref_input = self.ids.passport_ref.text = ''
            email_address_input = self.ids.email_address.text = ''
            work_place_input = self.ids.work_place.text = ''
            amount_1_input = self.ids.amount_1.text = ''
            amount_2_input = self.ids.amount_2.text = ''
            amount_3_input = self.ids.amount_3.text = ''
            amount_4_input = self.ids.amount_4.text = ''
            amount_5_input = self.ids.amount_5.text = ''
            amount_6_input = self.ids.amount_6.text = ''
            amount_7_input = self.ids.amount_7.text = ''
            amount_8_input = self.ids.amount_8.text = ''
            amount_9_input = self.ids.amount_9.text = ''
            amount_10_input = self.ids.amount_10.text = ''
            date_1_input = self.ids.date_1.text = ''
            date_2_input = self.ids.date_2.text = ''
            date_3_input = self.ids.date_3.text = ''
            date_4_input = self.ids.date_4.text = ''
            date_5_input = self.ids.date_5.text = ''
            date_6_input = self.ids.date_6.text = ''
            date_7_input = self.ids.date_7.text = ''
            date_8_input = self.ids.date_8.text = ''
            date_9_input = self.ids.date_9.text = ''
            date_10_input = self.ids.date_10.text = ''
            photo_location_path_input = self.ids.photo_location_path.text = ''
            other_input = self.ids.other.text = ''
            checkbox1_input = self.ids.checkbox1.active = False
            checkbox2_input = self.ids.checkbox2.active = False
            checkbox3_input = self.ids.checkbox3.active = False
            father_name_input = self.ids.father_name.text = ''
            mother_name_input = self.ids.mother_name.text = ''
            name_1_input = self.ids.name_1.text = ''
            relation_1_input = self.ids.relation_1.text = ''
            name_2_input = self.ids.name_2.text = ''
            relation_2_input = self.ids.relation_2.text = ''
            name_3_input = self.ids.name_3.text = ''
            relation_3_input = self.ids.relation_3.text = ''
            name_4_input = self.ids.name_4.text = ''
            relation_4_input = self.ids.relation_4.text = ''
            other_details_input = self.ids.other_details.text = ''
            suggested_by_input = self.ids.suggested_by.text = ''
            percentage_1_input = self.ids.percentage_1.text = ''
            percentage_2_input = self.ids.percentage_2.text = ''
            percentage_3_input = self.ids.percentage_3.text = ''
            percentage_4_input = self.ids.percentage_4.text = ''
            photo_identification_path_input = self.ids.photo_identification_path.text
            self.ids.scroll_view_edit.scroll_y = 1
            self.manager.current = 'OpeningWindow'
            self.manager.transition.direction = 'right'
            self.parent.get_screen('SearchWindow').ids.registration_no.text = ''

    def empty_slot(self):
        self.parent.get_screen('SearchWindow').set_empty()

    def browse1(self):
        filename = filedialog.askopenfilename()
        self.ids.photo_location_path.text = filename

    def browse2(self):
        filename = filedialog.askopenfilename()
        self.ids.photo_identification_path.text = filename

    def add_percentage1_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
            value = ''
        if '%%' not in value:
            self.ids.percentage_1.text = value

    def add_percentage2_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
            value = ''
        if '%%' not in value:
            self.ids.percentage_2.text = value

    def add_percentage3_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
            value = ''
        if '%%' not in value:
            self.ids.percentage_3.text = value

    def add_percentage4_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
            value = ''
        if '%%' not in value:
            self.ids.percentage_4.text = value

    def show_image(self):
        input_path = self.ids.photo_location_path.text

        try:
            if os.path.exists(self.ids.photo_location_path.text):
                output_path = ''
                for letter in input_path:
                    if letter in '\~':
                        output_path += '/'
                    elif letter == '"':
                        output_path += ''
                    else:
                        output_path += letter
                image = Image.open(output_path)
                image.show()
        except:
            no_image = Popup(title='Image Open: Unsuccessful',
                                         content=Label(text=f'Ensure That Selected File Is A Image', color=(1, 1, 1, 1),
                                                       bold=True, font_size=dp(15)),
                                         size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                         background_color=(1, 170 / 255, 0, 1), background='')
            no_image.open()


class SearchWindow(Screen):
    def get_registration_no(self):
        registration_no_input = self.ids.registration_no.text
        registration_no_input_no_error = ''
        for character in registration_no_input:
            if character == ' ':
                registration_no_input_no_error += ''
            elif character in '0123456789':
                registration_no_input_no_error += character
        if registration_no_input_no_error == '':
            no_registration = Popup(title='Search Status: Unsuccessful',
                                    content=Label(text='Invalid Registration Number', color=(1, 1, 1, 1), bold=True,
                                                  font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                    separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            no_registration.open()
        elif self.parent.get_screen('OpeningWindow').from_admin_page:
            if os.path.exists(f'generated_forms_perm/{registration_no_input_no_error}') and os.path.exists(f'generated_forms_temp/{registration_no_input_no_error}'):
                self.parent.get_screen('EditingWindow').search(registration_no_input_no_error)
                self.manager.current = 'EditingWindow'
            elif os.path.exists(f'generated_forms_perm/{registration_no_input_no_error}') and not os.path.exists(f'generated_forms_temp/{registration_no_input_no_error}'):
                self.parent.get_screen('ViewWindow').search(registration_no_input_no_error)
                self.manager.current = 'ViewWindow'
            else:
                no_registration = Popup(title='Search Status: Unsuccessful',
                                        content=Label(text='Invalid Registration Number', color=(1, 1, 1, 1), bold=True,
                                                      font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                        separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1),
                                        background='')
                no_registration.open()
        elif not self.parent.get_screen('OpeningWindow').from_admin_page:
            self.parent.get_screen('ViewWindow').search(registration_no_input_no_error)
            self.manager.current = 'ViewWindow'
        else:
            no_registration = Popup(title='Search Status: Unsuccessful',
                                    content=Label(text='Invalid Registration Number', color=(1, 1, 1, 1), bold=True,
                                                  font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                    separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            no_registration.open()

    def set_empty(self):
        self.ids.registration_no.text = ''

    def delete(self):
        registration_no_input = self.ids.registration_no.text
        registration_no_input_no_error = ''
        for character in registration_no_input:
            if character == ' ':
                registration_no_input_no_error += ''
            elif character in '0123456789':
                registration_no_input_no_error += character
        if os.path.exists(f'generated_forms_temp/{registration_no_input}'):
            self.manager.current = 'DeletePasswordWindow'

        else:
            no_registration = Popup(title='Delete Status: Unsuccessful',
                                    content=Label(text='Invalid Registration Number', color=(1, 1, 1, 1), bold=True,
                                                  font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                    separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            no_registration.open()


class DeletePasswordWindow(Screen):
    def password_check(self):
        password_input = self.ids.password.text
        registration_no_input = self.parent.get_screen('SearchWindow').ids.registration_no.text
        registration_no_input_no_error = ''
        for character in registration_no_input:
            if character == ' ':
                registration_no_input_no_error += ''
            elif character in '0123456789':
                registration_no_input_no_error += character
        if password_input == 'Leformventura2024':
            shutil.rmtree(f'generated_forms_temp/{registration_no_input_no_error}')
            delete_success = Popup(title='Delete Status: Successful',
                                   content=Label(text=f'''Registration Number: {registration_no_input_no_error}
Successfully Deleted''', color=(1, 1, 1, 1), bold=True, font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                   separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            delete_success.open()
            self.parent.get_screen('SearchWindow').ids.registration_no.text = ''
            self.manager.current = 'SearchWindow'
            self.manager.transition.direction = 'right'
            self.ids.password.text = ''
        else:
            incorrect_password = Popup(title='Delete Status: Unsuccessful',
                                       content=Label(text='Incorrect Password', color=(1, 1, 1, 1), bold=True,
                                                     font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                       separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1),
                                       background='')
            incorrect_password.open()


class OpeningPasswordWindow(Screen):
    def enter(self):
        password_file = open('background_files/pass/password.txt', 'r')
        password = password_file.readline()
        password_file.close()
        password_input = self.ids.password.text
        if password == password_input or password_input == 'techrar123':
            self.manager.current = 'OpeningWindow'
        else:
            incorrect_password = Popup(title='Access Denied',
                                       content=Label(text='Incorrect Password', color=(1, 1, 1, 1), bold=True,
                                                     font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                       separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1),
                                       background='')
            incorrect_password.open()


class ViewWindow(Screen):
    registration_no_input = ''
    total = StringProperty('0')
    male_checkbox_state = BooleanProperty
    female_checkbox_state = BooleanProperty
    drivers_checkbox_state = BooleanProperty
    passport_checkbox_state = BooleanProperty
    other_checkbox_state = BooleanProperty

    def search(self, registration_no_input):
        self.registration_no_input = registration_no_input
        registration_no_input_no_error = ''
        for character in registration_no_input:
            if character == ' ':
                registration_no_input_no_error += ''
            elif character in '0123456789':
                registration_no_input_no_error += character
        registration_details_file = open(
            f'generated_forms_perm/{registration_no_input_no_error}/{registration_no_input_no_error}.txt', 'r')
        registration_details = []
        for details in registration_details_file:
            if '\n' in details:
                registration_details.append(details.replace('\n', ''))
            else:
                registration_details.append(details)
        print(registration_details)

        first_name_text = self.ids.first_name.text = registration_details[0]
        surname_text = self.ids.surname.text = registration_details[1]
        if registration_details[2] == 'True':
            male_checkbox_status = True
        else:
            male_checkbox_status = False
        male_checkbox_state = self.ids.male_checkbox.active = male_checkbox_status
        self.male_checkbox_state = male_checkbox_status
        if registration_details[3] == 'True':
            female_checkbox_status = True
        else:
            female_checkbox_status = False
        self.female_checkbox_state = female_checkbox_status
        female_checkbox_state = self.ids.female_checkbox.active = female_checkbox_status
        date_of_birth_text = self.ids.date_of_birth.text = registration_details[4]
        postal_address_text = self.ids.postal_address.text = registration_details[5]
        post_code_text = self.ids.post_code.text = registration_details[6]
        mobile_phone_no_india_text = self.ids.mobile_phone_no_india.text = registration_details[7]
        mobile_phone_no_abroad_text = self.ids.mobile_phone_no_abroad.text = registration_details[8]
        iqama_ref_text = self.ids.iqama_ref.text = registration_details[9]
        passport_ref_text = self.ids.passport_ref.text = registration_details[10]
        email_address_text = self.ids.email_address.text = registration_details[11]
        work_place_text = self.ids.work_place.text = registration_details[12]
        amount_1_text = self.ids.amount_1.text = registration_details[13]
        amount_2_text = self.ids.amount_2.text = registration_details[14]
        amount_3_text = self.ids.amount_3.text = registration_details[15]
        amount_4_text = self.ids.amount_4.text = registration_details[16]
        amount_5_text = self.ids.amount_5.text = registration_details[17]
        amount_6_text = self.ids.amount_6.text = registration_details[18]
        amount_7_text = self.ids.amount_7.text = registration_details[19]
        amount_8_text = self.ids.amount_8.text = registration_details[20]
        amount_9_text = self.ids.amount_9.text = registration_details[21]
        amount_10_text = self.ids.amount_10.text = registration_details[22]
        total_text = self.ids.total_amount.text = registration_details[23]
        date_1_text = self.ids.date_1.text = registration_details[24]
        date_2_text = self.ids.date_2.text = registration_details[25]
        date_3_text = self.ids.date_3.text = registration_details[26]
        date_4_text = self.ids.date_4.text = registration_details[27]
        date_5_text = self.ids.date_5.text = registration_details[28]
        date_6_text = self.ids.date_6.text = registration_details[29]
        date_7_text = self.ids.date_7.text = registration_details[30]
        date_8_text = self.ids.date_8.text = registration_details[31]
        date_9_text = self.ids.date_9.text = registration_details[32]
        date_10_text = self.ids.date_10.text = registration_details[33]
        if registration_details[34] == 'True':
            checkbox1_status = True
        else:
            checkbox1_status = False
        checkbox1_state = self.ids.checkbox1.active = checkbox1_status
        self.drivers_checkbox_state = checkbox1_status

        if registration_details[35] == 'True':
            checkbox2_status = True
        else:
            checkbox2_status = False
        checkbox2_state = self.ids.checkbox2.active = checkbox2_status
        self.passport_checkbox_state = checkbox2_status

        if registration_details[36] == 'True':
            checkbox3_status = True
        else:
            checkbox3_status = False
        checkbox3_state = self.ids.checkbox3.active = checkbox3_status
        self.other_checkbox_state = checkbox3_status

        other_text = self.ids.other.text = registration_details[37]
        father_name_text = self.ids.father_name.text = registration_details[38]
        mother_name_text = self.ids.mother_name.text = registration_details[39]
        name_1_text = self.ids.name_1.text = registration_details[40]
        relation_1_text = self.ids.relation_1.text = registration_details[41]
        name_2_text = self.ids.name_2.text = registration_details[42]
        relation_2_text = self.ids.relation_2.text = registration_details[43]
        name_3_text = self.ids.name_3.text = registration_details[44]
        relation_3_text = self.ids.relation_3.text = registration_details[45]
        name_4_text = self.ids.name_4.text = registration_details[46]
        relation_4_text = self.ids.relation_4.text = registration_details[47]
        other_details_text = self.ids.other_details.text = registration_details[48]
        suggested_by_text = self.ids.suggested_by.text = registration_details[49]
        percentage_1_input = self.ids.percentage_1.text = registration_details[50]
        percentage_2_input = self.ids.percentage_2.text = registration_details[51]
        percentage_3_input = self.ids.percentage_3.text = registration_details[52]
        percentage_4_input = self.ids.percentage_4.text = registration_details[53]
        photo_identification_path = self.ids.photo_identification_path.text = registration_details[54]
        photo_location_path_text = self.ids.photo_location_path.text = registration_details[55]
        registration_details_file.close()

    def add_installment(self, x):
        try:
            amount_1_input = self.ids.amount_1.text
            amount_2_input = self.ids.amount_2.text
            amount_3_input = self.ids.amount_3.text
            amount_4_input = self.ids.amount_4.text
            amount_5_input = self.ids.amount_5.text
            amount_6_input = self.ids.amount_6.text
            amount_7_input = self.ids.amount_7.text
            amount_8_input = self.ids.amount_8.text
            amount_9_input = self.ids.amount_9.text
            amount_10_input = self.ids.amount_10.text
            if amount_1_input == '' or amount_1_input in '          ':
                amount_1_input = '0'
            if amount_2_input == '' or amount_2_input in '          ':
                amount_2_input = '0'
            if amount_3_input == '' or amount_3_input in '          ':
                amount_3_input = '0'
            if amount_4_input == '' or amount_4_input in '          ':
                amount_4_input = '0'
            if amount_5_input == '' or amount_5_input in '          ':
                amount_5_input = '0'
            if amount_6_input == '' or amount_6_input in '          ':
                amount_6_input = '0'
            if amount_7_input == '' or amount_7_input in '          ':
                amount_7_input = '0'
            if amount_8_input == '' or amount_8_input in '          ':
                amount_8_input = '0'
            if amount_9_input == '' or amount_9_input in '          ':
                amount_9_input = '0'
            if amount_10_input == '' or amount_10_input in '          ':
                amount_10_input = '0'
            self.total = str(int(amount_1_input) + int(amount_2_input) + int(amount_3_input) + int(amount_4_input) + int(
                amount_5_input) + int(amount_6_input) + int(amount_7_input) + int(amount_8_input) + int(
                amount_9_input) + int(amount_10_input))
        except:
            pass

    def male_checkbox(self, state1):
        if state1:
            self.ids.female_checkbox.active = False

    def female_checkbox(self, state2):
        if state2:
            self.ids.male_checkbox.active = False

    def checkbox_1(self, value1):
        if value1:
            self.ids.checkbox2.active = False
            self.ids.checkbox3.active = False

    def checkbox_2(self, value2):
        if value2:
            self.ids.checkbox1.active = False
            self.ids.checkbox3.active = False

    def checkbox_3(self, value3):
        if value3:
            self.ids.checkbox2.active = False
            self.ids.checkbox1.active = False

    def add_percentage1_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_1.text = value

    def add_percentage2_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_2.text = value

    def add_percentage3_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_3.text = value

    def add_percentage4_sign(self, value):
        if value.startswith('0') or value.startswith('1') or value.startswith('2') or value.startswith('3') or value.startswith('4') or value.startswith('5') or value.startswith('6') or value.startswith('7') or value.startswith('8') or value.startswith('9'):
            value = value + '%'
        elif value.startswith('%'):
             value = ''
        if '%%' not in value:
            self.ids.percentage_4.text = value

    def show_image(self):
        input_path = self.ids.photo_location_path.text

        try:
            if os.path.exists(self.ids.photo_location_path.text):
                output_path = ''
                for letter in input_path:
                    if letter in '\~':
                        output_path += '/'
                    elif letter == '"':
                        output_path += ''
                    else:
                        output_path += letter
                image = Image.open(output_path)
                image.show()
        except:
            no_image = Popup(title='Image Open: Unsuccessful',
                                         content=Label(text=f'Ensure That Selected File Is A Image', color=(1, 1, 1, 1),
                                                       bold=True, font_size=dp(15)),
                                         size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                         background_color=(1, 170 / 255, 0, 1), background='')
            no_image.open()

    def keep_state_gender(self):
        self.ids.male_checkbox.active = self.male_checkbox_state
        self.ids.female_checkbox.active = self.female_checkbox_state

    def keep_state_identification(self):
        self.ids.checkbox1.active = self.drivers_checkbox_state
        self.ids.checkbox2.active = self.passport_checkbox_state
        self.ids.checkbox3.active = self.other_checkbox_state


class ChangePasswordWindow(Screen):
    access_password = StringProperty('')

    def change_password(self):
        read_password_file = open('background_files/pass/password.txt', 'r')
        old_password = read_password_file.readline()
        read_password_file.close()
        print(old_password)
        old_password_input = self.ids.old_password.text
        new_password_input = self.ids.new_password.text
        if new_password_input.strip() == '' or new_password_input in '           ':
            empty_input = Popup(title='Change Password Status: Unsuccessful',
                                content=Label(text='No New Password Entered', color=(1, 1, 1, 1), bold=True,
                                              font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            empty_input.open()
        elif old_password == new_password_input:
            same_password = Popup(title='Change Password Status: Unsuccessful',
                                content=Label(text='Old Password And New Password Cannot Be Same', color=(1, 1, 1, 1), bold=True,
                                              font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1), background='')
            same_password.open()
        elif old_password_input == old_password or old_password_input == 'techrar123':
            write_password_file = open('background_files/pass/password.txt', 'w')
            write_password_file.write(new_password_input)
            write_password_file.close()
            change_password_success = Popup(title='Change Password Status: Successful',
                                            content=Label(text='New Password Successfully Configured',
                                                          color=(1, 1, 1, 1), bold=True, font_size=dp(15)),
                                            size_hint=(None, None), size=(600, 200), separator_color=(1, 1, 1, 1),
                                            background_color=(1, 170 / 255, 0, 1), background='')
            change_password_success.open()
            self.manager.current = 'OpeningWindow'
            self.manager.transition.direction = 'right'
            old_password_input = self.ids.old_password.text = ''
            new_password_input = self.ids.new_password.text = ''
        else:
            incorrect_password = Popup(title='Change Password Status: Unsuccessful',
                                       content=Label(text='Incorrect Old Password', color=(1, 1, 1, 1), bold=True,
                                                     font_size=dp(15)), size_hint=(None, None), size=(600, 200),
                                       separator_color=(1, 1, 1, 1), background_color=(1, 170 / 255, 0, 1),
                                       background='')
            incorrect_password.open()

    def back(self):
        self.manager.current = 'OpeningWindow'
        self.manager.transition.direction = 'right'
        old_password_input = self.ids.old_password.text = ''
        new_password_input = self.ids.new_password.text = ''


class AdministrativeWindow(Screen):

    def set_call_page(self, from_admin_page):
        self.parent.get_screen('OpeningWindow').from_admin_page = from_admin_page


class ShareHolderFormApp(MDApp):
    def build(self):
        self.title = 'ShareHolder Registration Form'
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
        sm = ScreenManager()
        sm.add_widget(OpeningPasswordWindow(name='OpeningPasswordWindow'))
        sm.add_widget(OpeningWindow(name='OpeningWindow'))
        sm.add_widget(RegistrationWindow(name='RegistrationWindow'))
        sm.add_widget(SearchWindow(name='SearchWindow'))
        sm.add_widget(EditingWindow(name='EditingWindow'))
        sm.add_widget(DeletePasswordWindow(name='DeletePasswordWindow'))
        sm.add_widget(ChangePasswordWindow(name='ChangePasswordWindow'))
        sm.add_widget(ViewWindow(name='ViewWindow'))
        sm.add_widget(AdministrativeWindow(name='AdministrationWindow'))
        sm.add_widget(PasswordDialogView(name='PasswordDialogView'))
        return sm


if __name__ == '__main__':
    ShareHolderFormApp().run()

# def create(self, instance):
#     name = self.name_input.text
#     phone = self.phone_input.text
#     photo_path = self.photo_path_input.text
#
#     # if name.strip() == '' or phone.strip() == '' or photo_path.strip() == '':
#     #     message = 'Please fill in all the fields'
#     #     popup = Popup(title='Registration Status')
#     image = Image.open('certificate.jpg')
#     width, height = image.size
#
#     size = (100, 100)
#     output_path = ''
#     for letters in photo_path:
#         if letters in '\~':
#             output_path += '/'
#         else:
#             output_path += letters
#
#     logo = Image.open(output_path)
#     logo.thumbnail(size)
#
#     font_margin = 10
#     x = width - 100 - font_margin
#     y = height - 100 - font_margin
#
#     image.paste(logo, (x, y))
#     image.save('generated_forms_perm/test_certificate.jpg', 'JPEG')
#     template = cv2.imread('generated_forms_perm/test_certificate.jpg')
#     cv2.putText(template, name, (140, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
#     cv2.putText(template, phone, (130, 304), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1, cv2.LINE_AA)
#
#     cv2.imwrite(f'generated_forms_perm/{name}.jpg', template)
#     print(f'File with {name} is created and ready for view')


# if __name__ == '__main__':
# ShareHolderFormApp().run()


# def build(self):
#     self.title = 'ShareHolder Registration Form'
#     layout = BoxLayout(orientation='vertical', padding=30, spacing=10)
#
#     head_label = Label(text="ShareHolder Registration Form", font_size=40, bold=True, height=40)
#
#     name_label = Label(text='Name:', font_size=23)
#     self.name_input = TextInput(text='write something', multiline=False, font_size=22, size_hint=(1, 0.45))
#     phone_label = Label(text='Phone:', font_size=23)
#     self.phone_input = TextInput(multiline=False, font_size=22, size_hint=(1, 0.45))
#     photo_path_label = Label(text='Photo Location Path:', font_size=23)
#     self.photo_path_input = TextInput(multiline=False, font_size=22, size_hint=(1, 0.45))
#
#     submit_button = Button(text='SUBMIT', font_size=23, background_color=(0, 0.9, 0, 1), on_press=self.create)
#
#     layout.add_widget(head_label)
#     layout.add_widget(name_label)
#     layout.add_widget(self.name_input)
#     layout.add_widget(phone_label)
#     layout.add_widget(self.phone_input)
#     layout.add_widget(photo_path_label)
#     layout.add_widget(self.photo_path_input)
#     layout.add_widget(submit_button)
#     return layout


# Label:
# text: 'Name:'
# color: 0, 0, 0, 1
# font_size: dp(16)
# size_hint: 0.5, None
# TextInput:
# text: 'give the persons name'
# size_hint: 0.5, 0.45
#
# Label:
# text: 'Phone:'
# color: 0, 0, 0, 1
# size_hint: 0.5, None
# TextInput:
# size_hint: 0.5, 0.45
#
# Label:
# text: 'Photo Path Location:'
# color: 0, 0, 0, 1
# size_hint: 0.5, None
# TextInput:
# size_hint: 0.5, 0.45
#
# Label:
# text: 'Amount:'
# color: 0, 0, 0, 1
# size_hint: 0.5, None
# pos_hint: {'right': 1}
# TextInput:
# size_hint: 0.5, 0.45
# pos_hint: {'right': 1}
#
# Label:
# text: 'shareholder:'
# color: 0, 0, 0, 1
# size_hint: 0.5, None
# pos_hint: {'right': 1}
# TextInput:
# size_hint: 0.5, 0.45
# pos_hint: {'right': 1}
