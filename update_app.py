import sys

with open("app.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_imports = """import os
import sys
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import customtkinter as ctk
import zipfile
from io import BytesIO
import sqlite3
import gc
import time

# Config CTK
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
"""

new_app_class = """# ==========================================
# GIAO DIỆN CHÍNH (CUSTOMTKINTER)
# ==========================================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Desktop File Searcher (AI Indexing)")
        self.root.geometry("900x700")
        
        self.is_indexing = False
        init_db() # Khởi tạo DB nếu chưa có
        
        # Style cho Treeview (Dark Mode)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="#2b2b2b",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#2b2b2b",
                        bordercolor="#343638",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#1f538d')])
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat")
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])
        
        # Tạo Tabview
        self.tabview = ctk.CTkTabview(root)
        self.tabview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.tab_index = self.tabview.add("Quản lý Dữ liệu & Lập chỉ mục")
        self.tab_search = self.tabview.add("Tìm Kiếm Nhanh")
        
        self.setup_tab_index()
        self.setup_tab_search()
        
        # System Tray setup
        self.root.protocol("WM_DELETE_WINDOW", self.hide_window)
        self.setup_tray()
        
        # Watchdog setup
        self.observer = None
        self.start_watchdog(self.entry_dir.get().strip())
        
    def setup_tab_index(self):
        frame_top = ctk.CTkFrame(self.tab_index)
        frame_top.pack(fill=tk.X, padx=10, pady=20)
        
        ctk.CTkLabel(frame_top, text="Thư mục/Ổ đĩa:").grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        self.entry_dir = ctk.CTkEntry(frame_top, width=450)
        self.entry_dir.grid(row=0, column=1, padx=5, pady=5)
        self.entry_dir.insert(0, os.path.expanduser('~') if sys.platform == 'darwin' else "D:\\\\")
        
        btn_browse = ctk.CTkButton(frame_top, text="Chọn Thư Mục", command=self.browse_dir, width=120)
        btn_browse.grid(row=0, column=2, padx=5, pady=5)
        
        self.btn_index = ctk.CTkButton(frame_top, text="Bắt đầu Quét & Phân loại", command=self.start_indexing, fg_color="#28a745", hover_color="#218838")
        self.btn_index.grid(row=1, column=0, columnspan=3, pady=15)
        
        self.progress_bar = ctk.CTkProgressBar(frame_top)
        self.progress_bar.grid(row=2, column=0, columnspan=3, sticky=tk.EW, pady=10, padx=10)
        self.progress_bar.set(0)
        
        self.lbl_index_status = ctk.CTkLabel(frame_top, text="Trạng thái: Sẵn sàng.", text_color="#3498db")
        self.lbl_index_status.grid(row=3, column=0, columnspan=3, sticky=tk.W, pady=5, padx=5)
        
    def setup_tab_search(self):
        frame_top = ctk.CTkFrame(self.tab_search)
        frame_top.pack(fill=tk.X, padx=10, pady=10)
        
        ctk.CTkLabel(frame_top, text="Từ khóa:").grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        self.entry_keyword = ctk.CTkEntry(frame_top, width=300)
        self.entry_keyword.grid(row=0, column=1, padx=5, pady=5)
        self.entry_keyword.bind("<Return>", lambda event: self.do_search())
        
        ctk.CTkLabel(frame_top, text="Chủ đề:").grid(row=0, column=2, sticky=tk.W, pady=5, padx=5)
        self.combo_topic = ctk.CTkOptionMenu(frame_top, values=["Tất cả", "Toán học", "Lập trình", "Kiến thức Đại cương", "Khác"], width=150)
        self.combo_topic.set("Tất cả")
        self.combo_topic.grid(row=0, column=3, padx=5, pady=5)
        
        self.btn_search = ctk.CTkButton(frame_top, text="Tìm kiếm Siêu Tốc", command=self.do_search, width=150)
        self.btn_search.grid(row=0, column=4, padx=10, pady=5)
        
        self.lbl_search_status = ctk.CTkLabel(frame_top, text="Nhập từ khóa và bấm Tìm kiếm.", text_color="#3498db")
        self.lbl_search_status.grid(row=1, column=0, columnspan=5, sticky=tk.W, pady=5, padx=5)
        
        self.paned_window = tk.PanedWindow(self.tab_search, orient=tk.VERTICAL, bg="#2b2b2b", bd=0, sashwidth=4)
        self.paned_window.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        frame_list = ctk.CTkFrame(self.paned_window)
        self.paned_window.add(frame_list, minsize=150)
        
        self.tree = ttk.Treeview(frame_list, columns=("Path", "Snippet", "Topic"), show="headings")
        self.tree.heading("Path", text="Đường dẫn File (Nhấp đúp để mở)")
        self.tree.heading("Snippet", text="Trích đoạn chứa từ khóa")
        self.tree.heading("Topic", text="Chủ đề")
        self.tree.column("Path", width=300)
        self.tree.column("Snippet", width=400)
        self.tree.column("Topic", width=100)
        self.tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        
        scrollbar_list = ttk.Scrollbar(frame_list, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar_list.set)
        scrollbar_list.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tree.bind("<Double-1>", self.open_file)
        self.tree.bind("<<TreeviewSelect>>", self.show_preview)
        
        frame_preview = ctk.CTkFrame(self.paned_window)
        self.paned_window.add(frame_preview, minsize=150)
        
        ctk.CTkLabel(frame_preview, text="Xem trước nội dung (Từ khóa được bôi đậm):").pack(anchor=tk.W, padx=5, pady=2)
        self.text_preview = ctk.CTkTextbox(frame_preview, wrap=tk.WORD)
        self.text_preview.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.text_preview.tag_config("highlight", background="#005fcc", foreground="white")
        self.text_preview.configure(state=tk.DISABLED)
        
        self.current_search_results = {}
        self.current_search_keyword = ""

    def hide_window(self):
        self.root.withdraw()
        
    def show_window(self, icon=None, item=None):
        self.root.after(0, self.root.deiconify)
        
    def quit_app(self, icon, item):
        if getattr(self, 'observer', None):
            self.observer.stop()
            self.observer.join()
        icon.stop()
        self.root.after(0, self.root.destroy)

    def setup_tray(self):
        image = Image.new('RGB', (64, 64), color=(255, 0, 0))
        d = ImageDraw.Draw(image)
        d.rectangle((16, 16, 48, 48), fill=(0, 0, 255))
        
        menu = pystray.Menu(
            pystray.MenuItem("Mở giao diện", self.show_window, default=True),
            pystray.MenuItem("Thoát", self.quit_app)
        )
        self.tray_icon = pystray.Icon("DFS_AI", image, "Desktop Searcher AI", menu)
        threading.Thread(target=self.tray_icon.run, daemon=True).start()

    def start_watchdog(self, directory):
        if getattr(self, 'observer', None):
            self.observer.stop()
            self.observer.join()
            self.observer = None
            
        if directory and os.path.exists(directory):
            try:
                self.observer = Observer()
                handler = DocumentEventHandler(self)
                self.observer.schedule(handler, directory, recursive=True)
                self.observer.start()
            except Exception as e:
                print(f"Lỗi khởi tạo Watchdog: {e}")
        
    def browse_dir(self):
        d = filedialog.askdirectory()
        if d:
            self.entry_dir.delete(0, tk.END)
            self.entry_dir.insert(0, d)
            self.start_watchdog(d)
            
    def open_file(self, event):
        selected = self.tree.selection()
        if selected:
            filepath = self.tree.item(selected[0], "values")[0]
            try:
                if sys.platform == 'darwin':
                    subprocess.call(['open', filepath])
                else:
                    os.startfile(filepath)
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể mở file: {e}")

    def show_preview(self, event):
        selected = self.tree.selection()
        if not selected:
            return
            
        filepath = self.tree.item(selected[0], "values")[0]
        content = self.current_search_results.get(filepath, "")
        keyword = self.current_search_keyword
        
        self.text_preview.configure(state=tk.NORMAL)
        self.text_preview.delete("1.0", tk.END)
        self.text_preview.insert(tk.END, content)
        
        if keyword:
            idx = "1.0"
            first_match = None
            while True:
                idx = self.text_preview.search(keyword, idx, nocase=True, stopindex=tk.END)
                if not idx:
                    break
                if not first_match:
                    first_match = idx
                end_idx = f"{idx}+{len(keyword)}c"
                self.text_preview.tag_add("highlight", idx, end_idx)
                idx = end_idx
                
            if first_match:
                self.text_preview.see(first_match)
                
        self.text_preview.configure(state=tk.DISABLED)

    def start_indexing(self):
        if self.is_indexing:
            return
            
        directory = self.entry_dir.get().strip()
        if not directory or not os.path.exists(directory):
            messagebox.showwarning("Cảnh báo", "Đường dẫn không hợp lệ!")
            return
            
        self.start_watchdog(directory)
            
        self.is_indexing = True
        self.btn_index.configure(state=tk.DISABLED)
        self.lbl_index_status.configure(text="Trạng thái: Đang quét siêu tốc metadata...")
        self.progress_bar.set(0)
        
        threading.Thread(target=self.indexing_worker, args=(directory,), daemon=True).start()
        
    def indexing_worker(self, directory):
        allowed_extensions = {".pdf", ".docx", ".pptx", ".xlsx"}
        files_to_process = []
        
        for root_dir, _, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in allowed_extensions:
                    files_to_process.append(os.path.join(root_dir, file))
                    
        total_files = len(files_to_process)
        if total_files == 0:
            self.root.after(0, self.phase1_complete, 0, 0)
            return
            
        processed_count = 0
        skipped_count = 0
            
        for i, filepath in enumerate(files_to_process):
            try:
                os_mtime = os.path.getmtime(filepath)
                db_mtime = get_db_mtime(filepath)
                
                percent = (i + 1) / total_files
                
                if os_mtime > db_mtime:
                    self.root.after(0, self.update_progress, percent, filepath, "Ghi nhận Metadata")
                    insert_or_update_document(filepath, "", "Đang chờ", os_mtime)
                    processed_count += 1
                else:
                    self.root.after(0, self.update_progress, percent, filepath, "Bỏ qua Metadata")
                    skipped_count += 1
                
            except Exception as e:
                print(f"Lỗi index metadata file {filepath}: {e}")
                
        self.root.after(0, self.phase1_complete, processed_count, skipped_count)
        
    def phase1_complete(self, processed_count, skipped_count):
        self.btn_index.configure(state=tk.NORMAL)
        self.lbl_index_status.configure(text=f"Hoàn tất quét siêu tốc! Đang khởi động đọc ngầm...")
        messagebox.showinfo("Thành công", f"Quá trình nạp Metadata hoàn tất.\\n\\n- File mới/cập nhật: {processed_count}\\n- File đã bỏ qua: {skipped_count}\\n\\nĐã mở khóa tìm kiếm theo tên. Hệ thống đang tiến hành đọc nội dung ngầm.")
        threading.Thread(target=self.background_processing_worker, daemon=True).start()

    def background_processing_worker(self):
        try:
            conn = sqlite3.connect(DB_PATH, timeout=10)
            cursor = conn.cursor()
            cursor.execute("SELECT filepath FROM documents WHERE topic = 'Đang chờ'")
            pending_files = [row[0] for row in cursor.fetchall()]
            conn.close()
        except Exception as e:
            print(f"Lỗi lấy danh sách phase 2: {e}")
            self.is_indexing = False
            return
            
        if not pending_files:
            self.root.after(0, lambda: self.lbl_index_status.configure(text="Trạng thái: Hoàn tất 100% (Không có file cần đọc nội dung)."))
            self.is_indexing = False
            return
            
        def status_callback(msg):
            self.root.after(0, lambda: self.lbl_index_status.configure(text=msg))
        init_ai_models(status_callback)
        
        total = len(pending_files)
        for i, filepath in enumerate(pending_files):
            percent = (i + 1) / total
            self.root.after(0, self.update_progress, percent, filepath, "Phân tích ngầm nội dung")
            
            ext = os.path.splitext(filepath)[1].lower()
            try:
                os_mtime = os.path.getmtime(filepath)
                content = ""
                if ext == ".pdf":
                    content = extract_text_pdf(filepath)
                elif ext == ".docx":
                    content = extract_text_docx(filepath)
                elif ext == ".pptx":
                    content = extract_text_pptx(filepath)
                elif ext == ".xlsx":
                    content = extract_text_excel(filepath)
                    
                topic = classify_text(content)
                insert_or_update_document(filepath, content, topic, os_mtime)
                
            except Exception as e:
                print(f"Lỗi đọc nội dung file {filepath}: {e}")
                insert_or_update_document(filepath, "", "Lỗi đọc", get_db_mtime(filepath))
                
            time.sleep(0.1) # Throttling nhường CPU/GPU
            
        self.root.after(0, lambda: self.lbl_index_status.configure(text="Trạng thái: Đã hoàn tất 100% lập chỉ mục toàn bộ nội dung."))
        self.is_indexing = False

    def update_progress(self, percent, current_file, action_text):
        self.progress_bar.set(percent)
        self.lbl_index_status.configure(text=f"Trạng thái: {action_text} ({percent*100:.1f}%) - {os.path.basename(current_file)}")

    def do_search(self):
        keyword = self.entry_keyword.get().strip().lower()
        topic = self.combo_topic.get()
        
        if not keyword:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập từ khóa tìm kiếm!")
            return
            
        # Xóa kết quả cũ
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        self.text_preview.configure(state=tk.NORMAL)
        self.text_preview.delete("1.0", tk.END)
        self.text_preview.configure(state=tk.DISABLED)
        
        self.current_search_results.clear()
        self.current_search_keyword = keyword
            
        self.lbl_search_status.configure(text="Đang tìm kiếm trong Database...")
        self.root.update()
        
        results = search_db(keyword, topic)
        
        for filepath, content, item_topic, snippet_text in results:
            self.current_search_results[filepath] = content
            
            if snippet_text:
                # Làm sạch HTML tags
                clean_snippet = snippet_text.replace("\\n", " ")
                clean_snippet = clean_snippet.replace("<b>", "").replace("</b>", "")
                snippet = clean_snippet
            else:
                content_lower = content.lower()
                idx = content_lower.find(keyword)
                if idx != -1:
                    start_idx = max(0, idx - 40)
                    end_idx = min(len(content), idx + len(keyword) + 100)
                    snippet = content[start_idx:end_idx].replace("\\n", " ")
                    if start_idx > 0:
                        snippet = "..." + snippet
                    if end_idx < len(content):
                        snippet = snippet + "..."
                else:
                    snippet = "Không tìm thấy đoạn chứa từ khóa trực tiếp."
                
            self.tree.insert("", tk.END, values=(filepath, snippet, item_topic))
            
        self.lbl_search_status.configure(text=f"Tìm thấy {len(results)} kết quả.")

if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
"""

# Tìm dòng chứa # ========================================== GIAO DIỆN CHÍNH
split_idx = -1
for i, line in enumerate(lines):
    if "# GIAO DIỆN CHÍNH" in line:
        split_idx = i - 1
        break

if split_idx != -1:
    middle_code = "".join(lines[12:split_idx])
    final_content = new_imports + middle_code + new_app_class
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(final_content)
    print("Successfully updated app.py")
else:
    print("Could not find split index!")
