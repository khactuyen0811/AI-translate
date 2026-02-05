#  AI Word Translator (Gemma 2B)

Dự án sử dụng mô hình ngôn ngữ lớn (LLM) **Gemma-2b-it** của Google để tự động dịch thuật các tệp văn bản Microsoft Word (.docx) từ tiếng Anh sang tiếng Việt, giữ nguyên cấu trúc đoạn văn và bảng biểu.

## Tính năng chính
- **Dịch đa dạng cấu trúc**: Hỗ trợ dịch nội dung trong cả Paragraph bình thường và các ô trong Bảng (Table).
- **Lọc nhiễu thông minh**: Tích hợp hàm `clean_ai_output` để loại bỏ các câu nói leo của AI (ví dụ: "Sure, here is the translation...") và xử lý các trường hợp AI từ chối dịch.
- **Tối ưu hóa phần cứng**: Sử dụng cấu hình `4-bit quantization` giúp chạy mượt mà trên GPU miễn phí (như Google Colab T4).
- **Giữ nguyên định dạng**: Đảm bảo căn lề (Alignment) của văn bản gốc không bị thay đổi sau khi dịch.

##  Công nghệ sử dụng
- **Model**: `google/gemma-2b-it` (thông qua Hugging Face).
- **Thư viện chính**:
  - `transformers`, `bitsandbytes`: Quản lý và nén mô hình AI.
  - `python-docx`: Đọc và ghi file Word.
  - `torch`: Nền tảng tính toán tensor cho mô hình.

##  Cách sử dụng
1. Cấu hình `HF_TOKEN` từ tài khoản Hugging Face của bạn.
2. Tải file Word cần dịch lên môi trường chạy (ví dụ: Colab).
3. Chỉnh sửa tên file đầu vào (`INPUT_WORD`) và đầu ra (`OUTPUT_WORD`) trong code.
4. Chạy script và đợi file hoàn thiện tự động tải về.

---
*Lưu ý: Dự án đang trong quá trình thử nghiệm để tối ưu hóa khả năng dịch thuật các thuật ngữ chuyên ngành.*
