# 🔍 Desktop File Searcher (AI Indexing) - Portable Version

Đây là công cụ tìm kiếm tài liệu nội bộ siêu tốc dành cho Windows. Phần mềm sử dụng cơ sở dữ liệu SQLite kết hợp với Trí tuệ Nhân tạo (HuggingFace Zero-shot Classification) được thiết kế theo **Kiến trúc Hybrid**, mang đến trải nghiệm tìm kiếm tức thì và hoàn toàn chạy Offline trên máy tính cá nhân.

Phiên bản **Portable (Độc lập)** này đã tích hợp sẵn toàn bộ môi trường và thư viện AI. Người dùng **không cần cài đặt Python** hay bất kỳ phần mềm phụ trợ nào khác.

## 🚀 Tính năng nổi bật
- **⚡ Lập Chỉ Mục Lười Biếng (Two-Phase Indexing):** Quét siêu tốc Tên file/Đường dẫn chỉ trong vài giây để bạn có thể tìm kiếm ngay lập tức. Nội dung chi tiết sẽ được AI âm thầm phân tích ở chế độ chạy ngầm.
- **🧠 AI Phân Loại Tự Động (Zero-shot NLP):** Tự động nhận diện file thuộc chủ đề (Toán học, Lập trình, Đại cương...) bằng mô hình AI đa ngôn ngữ mà không cần dán nhãn thủ công.
- **👁️ Trích Xuất Ngữ Cảnh Trực Quan:** Hiển thị đoạn văn chứa từ khóa và bôi vàng từ khóa ngay trong ứng dụng (trải nghiệm tương tự Google Search).
- **🔄 Đồng Bộ Thời Gian Thực (Watchdog):** Hệ thống tự động nhận biết file mới/sửa đổi ngay khi bạn vừa tải về và cập nhật vào Database mà không cần bấm quét lại.
- **🛡️ Hoạt Động Ngầm Tối Ưu (System Tray):** Thu nhỏ ứng dụng xuống khay hệ thống, canh gác và tự động cập nhật file 24/7 với mức tiêu thụ CPU gần như bằng 0%.

## 💻 Yêu cầu hệ thống
- **Hệ điều hành:** Windows 10 / 11 (64-bit).
- **Phần cứng:** Hoạt động mượt mà trên cả CPU phổ thông. Khuyến nghị máy tính có Card đồ họa (VGA) NVIDIA để AI xử lý nội dung với tốc độ cao nhất.
- **Môi trường:** **KHÔNG YÊU CẦU cài đặt Python**. Trải nghiệm "Cắm và Chạy" (Plug & Play) 100%.

## ⚙️ Hướng dẫn Sử dụng (Chỉ 2 bước)
1. Tải file `.zip` ở mục **Releases** bên tay phải trang này và giải nén ra một thư mục cố định (Ví dụ: `D:\PhanMemTimKiem`).
2. Nhấp đúp chuột vào file **`Run_SearchApp.bat`** để sử dụng ngay lập tức! (Bạn có thể tạo Shortcut cho file này ra ngoài màn hình Desktop).

## 💡 Hướng dẫn Thao tác
- **Tab 1 (Lập chỉ mục):** Chọn thư mục chứa tài liệu của bạn và bấm "Bắt đầu Quét". Hệ thống sẽ nạp siêu tốc metadata và mở khóa tìm kiếm ngay lập tức.
- **Chế độ Chạy Ngầm:** Khi bấm nút "X" ở góc trên bên phải, phần mềm **không tắt** mà sẽ thu nhỏ xuống khay hệ thống (System Tray - góc dưới bên phải màn hình). Để thoát hoàn toàn, click chuột phải vào icon ứng dụng và chọn "Thoát".
- **Tab 2 (Tìm kiếm):** Gõ từ khóa, chọn chủ đề và bấm Tìm kiếm. Nhấp đúp chuột vào kết quả để mở hẳn file gốc bằng phần mềm mặc định của máy.