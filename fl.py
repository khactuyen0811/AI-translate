import graphviz

# Khởi tạo sơ đồ theo chiều dọc (Top to Bottom)
dot = graphviz.Digraph('Universal_Doc_Translator', comment='Quy trình dịch thuật Word tổng quát')
dot.attr(rankdir='TB', size='10,12')

# 1. Các khối xử lý dữ liệu đầu vào
dot.node('START', 'BẮT ĐẦU\n(Nạp Model AI & File Word bất kỳ)', shape='ellipse', color='blue')
dot.node('EXTRACT', 'TRÍCH XUẤT DỮ LIỆU\n(Duyệt Paragraphs & Table Cells)', shape='box')

# 2. Khối điều kiện lọc (should_skip)
dot.node('SKIP_CHECK', 'BỘ LỌC ĐỊNH DẠNG\n(Né Mục lục, số trang,\ndấu chấm dài, dòng trống)', shape='diamond', color='orange')

# 3. Khối tương tác AI
dot.node('AI_PROMPT', 'GỬI AI XỬ LÝ\n(Prompt ép buộc: "Dịch hoặc\ngiữ nguyên gốc")', shape='box', color='purple')

# 4. Khối hậu kỳ - Chống lỗi (clean_ai_output)
dot.node('REFUSAL_FILTER', 'KIỂM TRA NỘI DUNG\n(Phát hiện "I cannot", "unable"...)', shape='diamond', color='red')
dot.node('REVERT', 'KHÔI PHỤC BẢN GỐC\n(Nếu AI từ chối dịch)', shape='box', style='filled', color='lightgrey')
dot.node('CLEAN', 'LỌC NÓI LEO\n(Xóa "Sure", "Here is...")', shape='box')

# 5. Khối ghi dữ liệu bảo tồn định dạng
dot.node('WRITE', 'GHI VÀO FILE\n(Tác động vào "Runs" để\ngiữ nguyên căn lề & font)', shape='box', color='green')
dot.node('END', 'XUẤT FILE HOÀN THIỆN', shape='ellipse', color='blue')

# Kết nối các logic
dot.edge('START', 'EXTRACT')
dot.edge('EXTRACT', 'SKIP_CHECK')
dot.edge('SKIP_CHECK', 'AI_PROMPT', label='Văn bản hợp lệ')
dot.edge('SKIP_CHECK', 'EXTRACT', label='Là rác/định dạng (Bỏ qua)')
dot.edge('AI_PROMPT', 'REFUSAL_FILTER')
dot.edge('REFUSAL_FILTER', 'REVERT', label='Nếu AI từ chối')
dot.edge('REFUSAL_FILTER', 'CLEAN', label='Nếu AI dịch tốt')
dot.edge('REVERT', 'WRITE')
dot.edge('CLEAN', 'WRITE')
dot.edge('WRITE', 'EXTRACT', label='Tiếp tục cho đến hết file')
dot.edge('EXTRACT', 'END', label='Đã duyệt hết 100%')

# Xuất kết quả ra file ảnh
dot.render('flowchart_tong_quat', format='png', view=True)
print("✅ Đã vẽ xong! Bro kiểm tra file 'flowchart_tong_quat.png' ở thư mục bên trái nhé.")