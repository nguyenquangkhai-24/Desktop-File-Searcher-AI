# 🔍 Desktop File Searcher (AI Indexing)

Đây là công cụ tìm kiếm tài liệu nội bộ siêu tốc dành cho Windows. Phần mềm sử dụng cơ sở dữ liệu SQLite kết hợp với Trí tuệ Nhân tạo (HuggingFace Zero-shot Classification) để tự động phân loại chủ đề tài liệu và trích xuất ngữ cảnh thông minh.

## 🚀 Tính năng nổi bật
- **Tìm kiếm Siêu Tốc:** Phản hồi kết quả trong tích tắc nhờ kiến trúc lập chỉ mục ngầm.
- **AI Phân Loại Tự Động:** Tự động nhận diện file thuộc chủ đề (Toán học, Lập trình, Đại cương...) mà không cần dán nhãn thủ công.
- **Trích Xuất Ngữ Cảnh:** Hiển thị đoạn văn chứa từ khóa và bôi vàng từ khóa ngay trong ứng dụng (giống Google Search).
- **Tối Ưu Phần Cứng:** Hỗ trợ tính toán song song, ép xung GPU (FP16) và cơ chế Lazy Loading để khởi động app ngay lập tức.
- **Quét Gia Tăng (Incremental Sync):** Nhận biết file mới/sửa đổi để chỉ quét những file cần thiết, tiết kiệm tối đa thời gian.

## 💻 Yêu cầu hệ thống
- Hệ điều hành: Windows 10 / 11.
- Phần cứng: Khuyến nghị máy tính có Card đồ họa (VGA) NVIDIA để AI xử lý tốc độ cao nhất. Các máy tính không có VGA rời vẫn có thể chạy nhưng thời gian lập chỉ mục file sẽ lâu hơn.
- Cài đặt sẵn Python 3.10 trở lên trên máy.

## ⚙️ Hướng dẫn Cài đặt (Từ A - Z)
1. Tải phiên bản mới nhất ở mục **Releases** bên tay phải trang này.
2. Giải nén file `.zip` vừa tải về ra một thư mục cố định trên máy (ví dụ: `D:\PhanMemTimKiem`).
3. Nhấp đúp chuột vào file **`CaiDat.bat`**. 
4. Hãy pha một tách cà phê và đợi từ 5-10 phút để hệ thống tự động tải môi trường và các lõi AI nặng về máy. (Lưu ý: Quá trình này chỉ diễn ra **DUY NHẤT MỘT LẦN**).
5. Khi màn hình báo "Cài đặt hoàn tất", bạn có thể tắt cửa sổ đó đi.

## 💡 Cách sử dụng
- Từ bây giờ, để mở phần mềm, bạn chỉ cần nhấp đúp vào file **`Run_SearchApp.bat`**. (Bạn có thể tạo Shortcut cho file này ra Desktop để tiện sử dụng).
- **Tab 1 (Lập chỉ mục):** Chọn thư mục chứa tài liệu của bạn và bấm "Bắt đầu Quét". (Lần quét đầu tiên AI sẽ cần tải mô hình ngôn ngữ khoảng 1.6GB, vui lòng không tắt app).
- **Tab 2 (Tìm kiếm):** Gõ từ khóa, chọn chủ đề và bấm Tìm kiếm. Bấm vào tên file để xem trước nội dung bôi vàng, hoặc nhấp đúp chuột để mở hẳn file gốc.