from page.contact import ContactPage


class TestContact:
    """
    通讯录测试用例
    todo 后期完善参数化构造测试用例
    """

    def setup(self):
        self.contact = ContactPage(reuse=True)

    def test_add_member(self):
        """
        测试通讯录添加成员功能
        :return:
        """
        self.contact.add_member('test1', 'eason', 'jarrettzhu', '86', '18924237052', '测试开发')
        # todo 暂未实现断言，后续使用get_contact_userlist方法实现，打算通过成员列表姓名进行断言，是否存在

    def test_edit_member(self):
        """
        测试通讯录添加成员功能
        """
        edit_name = "修改用户名2020"
        after_edit_name = self.contact.edit_member(edit_name)
        assert after_edit_name == edit_name
