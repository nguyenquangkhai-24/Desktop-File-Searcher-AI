# Lịch sử lỗi và Giải pháp
(Bắt đầu chu kỳ mới - Hiện chưa có lỗi)
[Lưu ý Kiến trúc]: Hệ thống giao diện (Tkinter) và Threading hiện tại đang hoạt động rất tốt, TUYỆT ĐỐI không thay đổi cấu trúc luồng của chúng. Chỉ thay đổi logic đọc nội dung bên trong hàm search_files.
[Quy tắc an toàn OCR]: Việc quét OCR rất dễ sinh lỗi nếu thiếu thư viện hệ thống (Poppler hoặc Tesseract.exe). Bắt buộc phải dùng try-except cho các đoạn code OCR. Nếu lỗi, in ra console "Bỏ qua OCR do thiếu thư viện" và tiếp tục quét các file khác bình thường.
[Cấu hình OCR bắt buộc]: Trong hàm xử lý pytesseract, tham số ngôn ngữ phải được thiết lập là lang='vie+eng' để phần mềm đọc được cả tiếng Việt và tiếng Anh trong cùng một file hình ảnh.
[Cấu hình Poppler bắt buộc]: Tuyệt đối KHÔNG yêu cầu người dùng cài đặt biến môi trường PATH. Trong hàm extract_text_pdf, khi gọi lệnh convert_from_path, BẮT BUỘC phải truyền tham số poppler_path vào.
Cú pháp yêu cầu: convert_from_path(filepath, poppler_path=r'C:\poppler\Library\bin')
[Ràng buộc phiên bản]: Dự án hiện đã chuyển sang Python 3.11 để tương thích với PyTorch và EasyOCR. Tuyệt đối không sử dụng các cú pháp chỉ có trên Python 3.12+ trở lên.