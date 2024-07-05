# from common.browser import Browser
# import time
# import os
# from config.config import *
#
#
# class AssertWrapper(Browser):
#
#     # 保存失败页面
#     def save_page_fail(self, page_action):
#         for_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
#         save_time = "{}-{}.png".format(page_action, for_time)
#         file_name = os.path.join(image_dir, save_time)
#         try:
#             self.driver.save_screenshot(file_name)
#         except:
#             print(f"在{page_action} 保存图片失败，请检查路径是否存在！！！")
#
#
#     def Assert_Testcases(self, actual, expected,page_action):
#         try:
#             self.assertEqual(actual, expected)
#         except Exception as e:
#             self.save_page_fail(page_action)
#             print(e)






