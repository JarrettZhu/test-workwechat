from selenium.webdriver.common.by import By

from page.base_page import BasePage
from selenium.webdriver.support import expected_conditions


class Material(BasePage):
    """
    素材库页面
    """

    def add_image(self):
        """
        添加图片
        :return:
        """
        add_image_button = (By.CSS_SELECTOR, '.js_upload_file_selector')
        self.find((By.LINK_TEXT, '图片')).click()
        self.find(add_image_button).click()
        self.find(By.ID, 'js_upload_input').send_keys('/Users/zhujunhua/PycharmProjects/test-workwechat/eason.jpeg')
        # text_to_be_present_in_element : 判断某个元素中的text是否 包含了 预期的字符串
        # todo:显式等待图片完成上传再点击完成按钮，效果有待商榷”
        self.wait(10, expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, '.js_pic_name_show'),
                                                                        'eason.jpeg'))
        self.find(By.LINK_TEXT, '完成').click()
        return self

    def get_newest_image_message(self):
        """
        获取仅有的一张图片名，暂用
        如果有多张图片要使用findelements方法返回结果列表
        :return:
        """
        return self.find((By.CSS_SELECTOR, '.js_pic_name_show')).text
