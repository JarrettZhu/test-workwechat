from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class ContactPage(BasePage):
    """
    通讯录页面
    """
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'

    def add_member(self, name, smallname, useraccount, mobile_area_code_value, mobile_number, position):
        """
        填写信息添加成员
        :param name: 姓名
        :param smallname: 别名
        :param useraccount: 账号
        :param mobile_area_code_value: 手机区号
        :param mobile_number: 手机号码
        :param position:职务
        :return:
        """
        # 姓名输入框
        name_input_text = (By.CSS_SELECTOR, '.ww_compatibleTxt #username')
        # 别名输入框
        smallname_input_text = (By.CSS_SELECTOR, '.ww_compatibleTxt #memberAdd_english_name')
        # 账号输入框
        useraccount_input_text = (By.CSS_SELECTOR, '#memberAdd_acctid')
        # 性别-男-选择框
        sex_male_select = (By.CSS_SELECTOR, '.member_edit_sec:nth-child(1) .ww_label:nth-child(1) > .ww_radio')
        # 性别-女-选择框
        sex_female_select = (By.CSS_SELECTOR, '.member_edit_sec:nth-child(1) .ww_label:nth-child(2) > .ww_radio')
        # 手机区号框
        mobile_area_code = (By.CSS_SELECTOR, '.ww_telInput_zipCode_input > .qui_inputText')
        # 具体手机区号：中国 86
        mobile_area_code_select = (By.CSS_SELECTOR, '[data-value="%s"]' % mobile_area_code_value)
        # 手机号码输入框
        mobile_number_input_text = (By.CSS_SELECTOR, '.qui_inputText.ww_inputText.ww_telInput_mainNumber')
        # 部门修改按钮
        department_change_button = (By.CSS_SELECTOR, '.ww_groupSelBtn_add.js_show_party_selector')
        # 部门修改页面确认按钮
        department_change_page_confirm_button = (By.LINK_TEXT, '确认')
        # department_change_page_confirm_button = (By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue.js_submit')
        # 职务输入框
        position_input_text = (By.CSS_SELECTOR, '.member_edit_item_right #memberAdd_title')
        # 底部确认按钮
        final_confirm_button = (By.LINK_TEXT, '保存')

        add_member_button = (By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member')
        WebDriverWait(self._driver, 10).until(self._wait_element)
        # self.wait(10, expected_conditions.visibility_of_element_located(add_member_button))
        # self.find(add_member_button).click()
        self.find(name_input_text).send_keys(name)
        self.find(smallname_input_text).send_keys(smallname)
        self.find(useraccount_input_text).send_keys(useraccount)
        self.find(sex_female_select).click()
        self.find(mobile_area_code).click()
        self.find(mobile_area_code_select).click()
        self.find(mobile_number_input_text).send_keys(mobile_number)
        self.find(department_change_button).click()
        self.wait(10, expected_conditions.visibility_of_element_located(department_change_page_confirm_button))
        # 加5秒死等查看效果
        sleep(2)
        self.find(department_change_page_confirm_button).click()
        self.find(position_input_text).send_keys(position)
        self.find(final_confirm_button).click()

    def _wait_element(self, d):
        size = len(self._driver.find_elements(By.ID, 'username'))
        if size < 1:
            self.find((By.CSS_SELECTOR, '.ww_operationBar:nth-child(1) .js_add_member')).click()
        return size >= 1

    def get_contact_userlist(self):
        # todo 暂未实现获取通讯录列表信息
        pass
        # return self._driver.find_elements(By.CSS_SELECTOR,
        #                                   '#member_list [data-type="member"] .member_colRight_memberTable_td span')
