# Mục tiêu Dự án
Xây dựng phần mềm Desktop tìm kiếm nội dung file cục bộ.
Giao diện cửa sổ ứng dụng độc lập, không dùng Web/Trình duyệt.
Tính năng cốt lõi: 
1. Quét tìm từ khóa bên trong các file thuộc một ổ đĩa cụ thể (Ví dụ D: D:\).
2. Hiển thị kết quả dưới dạng danh sách (Listbox/Treeview).
3. Người dùng nhấp đúp vào kết quả, file đó sẽ tự động mở lên bằng ứng dụng mặc định của hệ điều hành.

# Công nghệ sử dụng
- Ngôn ngữ: Python
- Giao diện: Tkinter (hoặc CustomTkinter)
- Thư viện đọc: os, subprocess, threading (để giao diện không bị đơ khi đang quét).
- Hỗ trợ thêm định dạng: .pptx (dùng python-pptx) và .xlsx (dùng openpyxl).
- Hỗ trợ OCR: Nhận diện văn bản trong hình ảnh nằm trong PDF/DOCX (dùng pytesseract và pdf2image).
- Yêu cầu cấu trúc: Tách hàm search_files thành các hàm nhỏ hơn (ví dụ: extract_text_pdf, extract_text_docx, extract_text_excel, extract_text_pptx) để code không bị rối.

# QUY TẮC AN TOÀN & BẮT BUỘC
1. BỎ QUA LỖI HỆ THỐNG: Khi quét toàn bộ ổ đĩa, bắt buộc phải dùng block `try-except` để bắt và bỏ qua lỗi `PermissionError` (lỗi không có quyền đọc file hệ thống đang bị khóa). Nếu không phần mềm sẽ bị văng (crash).
2. KHÔNG THAY ĐỔI DỮ LIỆU: Chỉ sử dụng các hàm đọc file. Cấm dùng os.remove, os.rename.
3. TẠO FILE KHỞI CHẠY TỰ ĐỘNG: Cần có một file .bat (Windows) để người dùng chạy phần mềm trực tiếp từ Desktop mà không cần mở IDE.