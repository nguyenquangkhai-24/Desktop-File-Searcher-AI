# 🔍 Desktop File Searcher (AI Indexing)

Đây là công cụ tìm kiếm tài liệu nội bộ siêu tốc dành cho Windows. Phần mềm sử dụng cơ sở dữ liệu SQLite kết hợp với Trí tuệ Nhân tạo (HuggingFace Zero-shot Classification) được thiết kế theo **Kiến trúc Hybrid**, mang đến trải nghiệm tìm kiếm nội dung thông minh, tức thì và hoàn toàn chạy Offline trên máy tính cá nhân.

## 🚀 Tính năng nổi bật
- **⚡ Lập Chỉ Mục Lười Biếng (Two-Phase Indexing):** Quét siêu tốc Tên file/Đường dẫn chỉ trong vài giây để bạn có thể tìm kiếm ngay lập tức. Nội dung chi tiết sẽ được AI âm thầm phân tích ở chế độ chạy ngầm.
- **🧠 AI Phân Loại Tự Động (Zero-shot NLP):** Tự động nhận diện file thuộc chủ đề (Toán học, Lập trình, Đại cương...) bằng mô hình siêu nhẹ đa ngôn ngữ `mDeBERTa-v3` mà không cần dán nhãn thủ công.
- **👁️ Trích Xuất Ngữ Cảnh Trực Quan:** Hiển thị đoạn văn chứa từ khóa và bôi vàng từ khóa ngay trong ứng dụng (trải nghiệm tương tự Google Search).
- **🔄 Đồng Bộ Thời Gian Thực (Watchdog):** Hệ thống tự động nhận biết file mới/sửa đổi ngay khi bạn vừa tải về và cập nhật vào Database mà không cần bấm quét lại.
- **🛡️ Hoạt Động Ngầm Tối Ưu (System Tray):** Thu nhỏ ứng dụng xuống khay hệ thống. Kết hợp với kiến trúc Hybrid OCR (ưu tiên đọc text trực tiếp) và Throttling, phần mềm có thể canh gác file 24/7 với mức tiêu thụ CPU gần như bằng 0%.

## 💻 Yêu cầu hệ thống
- **Hệ điều hành:** Windows 10 / 11.
- **Phần cứng:** Hoạt động mượt mà trên cả CPU phổ thông nhờ mô hình AI Lightweight. Khuyến nghị máy tính có Card đồ họa (VGA) NVIDIA để AI xử lý nội dung với tốc độ cao nhất.
- **Môi trường:** Yêu cầu máy cài đặt sẵn Python 3.10 trở lên (Hoặc sử dụng bản Portable độc lập).

## ⚙️ Hướng dẫn Cài đặt (Từ A - Z)
1. Tải phiên bản mới nhất ở mục **Releases** bên tay phải trang này.
2. Giải nén file `.zip` vừa tải về ra một thư mục cố định trên máy (ví dụ: `D:\PhanMemTimKiem`).
3. Nhấp đúp chuột vào file **`CaiDat.bat`**. 
4. Hãy pha một tách cà phê và đợi từ 5-10 phút để hệ thống tự động thiết lập môi trường và tải các lõi AI về máy. (Lưu ý: Quá trình này chỉ diễn ra **DUY NHẤT MỘT LẦN**).
5. Khi màn hình báo "Cài đặt hoàn tất", bạn có thể tắt cửa sổ đó đi.

## 💡 Cách sử dụng
- **Khởi động:** Nhấp đúp vào file **`Run_SearchApp.bat`** để mở phần mềm. (Bạn có thể tạo Shortcut ra Desktop để tiện sử dụng).
- **Tab 1 (Lập chỉ mục):** Chọn thư mục chứa tài liệu của bạn và bấm "Bắt đầu Quét". Hệ thống sẽ nạp siêu tốc metadata và mở khóa tìm kiếm ngay lập tức. Lần quét đầu tiên AI sẽ tải mô hình ngôn ngữ (khoảng 500MB), vui lòng giữ kết nối mạng.
- **Chế độ Chạy Ngầm:** Khi bấm nút "X" trên cửa sổ, phần mềm **không tắt** mà sẽ thu nhỏ xuống góc dưới cùng bên phải màn hình (System Tray). Để thoát hoàn toàn, click chuột phải vào icon ứng dụng và chọn "Thoát".
- **Tab 2 (Tìm kiếm):** Gõ từ khóa, chọn chủ đề và bấm Tìm kiếm. Nhấp đúp chuột vào kết quả để mở hẳn file gốc bằng phần mềm mặc định của máy tính.