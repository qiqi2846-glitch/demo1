import os
import json
import unittest

class TestCrawlComments(unittest.TestCase):

    def setUp(self):
        """Thiết lập đường dẫn file JSON để kiểm thử"""
        self.file_path = "data/cmts.json"

    # ------------------------
    # UT_1_FileExists
    # ------------------------
    def test_UT1_FileExists(self):
        """Kiểm tra file JSON có tồn tại sau khi crawl"""
    #         print("🔍 Kiểm tra file tồn tại:", os.path.abspath(self.file_path))
    #         self.assertTrue(os.path.exists(self.file_path), "❌ File cmts.json không tồn tại!")
    #
    #     # ------------------------
    #     # UT_2_ValidJSON
    #     # ------------------------
    def test_UT2_ValidJSON(self):
        """Kiểm tra định dạng JSON hợp lệ"""
        print("🔍 Kiểm tra định dạng JSON:", os.path.abspath(self.file_path))
        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                self.assertIsInstance(data, list, "❌ File JSON không chứa danh sách!")
            except json.JSONDecodeError:
                self.fail("❌ File cmts.json không phải định dạng JSON hợp lệ!")

    # ------------------------
    # UT_3_NonEmptyData
    # ------------------------
    def test_UT3_NonEmptyData(self):
        """Kiểm tra file có ít nhất một bình luận"""
        print("🔍 Kiểm tra dữ liệu không rỗng:", os.path.abspath(self.file_path))
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertGreater(len(data), 0, "❌ Không có bình luận nào được crawl!")

    # ------------------------
    # UT_4_ValidCommentStructure
    # ------------------------
    def test_UT4_ValidCommentStructure(self):
        """Kiểm tra cấu trúc mỗi bình luận có 'user' và 'comment' hợp lệ"""
        print("🔍 Kiểm tra cấu trúc dữ liệu:", os.path.abspath(self.file_path))
        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for i, item in enumerate(data, start=1):
            # Kiểm tra trường "user"
            self.assertIn("user", item, f"❌ Bình luận {i} thiếu trường 'user'!")
            self.assertTrue(item["user"].strip(), f"⚠️  Bình luận {i} có 'user' trống!")

            # Kiểm tra trường "comment"
            self.assertIn("comment", item, f"❌ Bình luận {i} thiếu trường 'comment'!")
            self.assertTrue(item["comment"].strip(), f"⚠️  Bình luận {i} có nội dung comment trống!")

if __name__ == "__main__":
    unittest.main()
