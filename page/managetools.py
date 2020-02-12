from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.material import Material


class ManageTools(BasePage):
    """
    管理工具页面
    """
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'

    def goto_material(self) -> Material:
        """
        进入素材库页面
        :return: 素材库page对象
        """
        self.find(By.PARTIAL_LINK_TEXT, '素材库').click()
        return Material(reuse=True)
