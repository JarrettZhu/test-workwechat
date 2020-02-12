from page.managetools import ManageTools


class TestManageTools:
    """
    管理工具测试用例
    """
    def setup(self):
        self.managetools = ManageTools(reuse=True)

    def test_material_add_image(self):
        """
        测试素材库上传图片
        """
        text = self.managetools.goto_material().add_image().get_newest_image_message()
        assert "eason.jpeg" == text
