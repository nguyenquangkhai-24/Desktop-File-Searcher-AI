MỤC TIÊU NÂNG CẤP: Thêm tính năng Trích xuất ngữ cảnh (Context Snippet) và Khung xem trước bôi đen từ khóa (Highlighted Preview In-App).

1. LOGIC TRÍCH XUẤT NGỮ CẢNH:
   - Cập nhật hàm `search_db(keyword, topic)` để `SELECT filepath, content FROM documents`.
   - Viết logic tìm vị trí `keyword` trong `content` (không phân biệt hoa thường). Cắt lấy chuỗi con gồm khoảng 40 ký tự trước và 100 ký tự sau từ khóa. Loại bỏ ký tự ngắt dòng (\n) trong trích đoạn và thêm "..." ở 2 đầu.

2. CẬP NHẬT GIAO DIỆN TÌM KIẾM (MASTER-DETAIL UI):
   - Tab Tìm Kiếm chia làm 2 phần (sử dụng PanedWindow hoặc cấu trúc Frame trên/dưới):
   - PHẦN TRÊN (Danh sách): `Treeview` có 2 cột: "Đường dẫn File" (width=300) và "Trích đoạn chứa từ khóa" (width=500).
   - PHẦN DƯỚI (Xem trước): Thêm một `tk.Text` widget (Read-only) có thanh cuộn.
   
3. LOGIC TƯƠNG TÁC & BÔI ĐEN:
   - Khi Single-click vào một kết quả trong Treeview: Load nội dung `content` tương ứng lên `tk.Text` bên dưới.
   - Sử dụng `Text.tag_add` và `Text.tag_config` để tìm và BÔI ĐEN MÀU VÀNG (`background="yellow"`) tất cả các vị trí xuất hiện của từ khóa trong `tk.Text`. Đồng thời tự động cuộn (scroll) `tk.Text` đến vị trí từ khóa đầu tiên (`Text.see()`).
   - Giữ nguyên Double-click để `os.startfile()`.