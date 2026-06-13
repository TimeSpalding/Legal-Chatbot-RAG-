# Trợ lý Pháp lý Việt Nam (Vietnamese Legal Chatbot RAG)

Hệ thống trợ lý ảo tư vấn pháp luật Việt Nam thông minh, áp dụng kỹ thuật RAG (Retrieval-Augmented Generation) tiên tiến để truy xuất và trả lời các câu hỏi pháp lý dựa trên cơ sở dữ liệu luật chính thống.

---

##  Tính năng nổi bật

- **Kiến trúc RAG lai (Hybrid Retrieval)**: Kết hợp tìm kiếm ngữ nghĩa bằng Vector DB (Qdrant) với tìm kiếm từ khóa truyền thống (BM25) để tối ưu hóa độ chính xác của tài liệu được truy xuất.
- **Phân loại câu hỏi chuyên biệt (Legal Domain Filtering)**: Tự động phân loại câu hỏi để chỉ trả lời các thắc mắc liên quan tới pháp luật Việt Nam, từ chối lịch sự đối với các câu hỏi ngoài phạm vi.
- **Tối ưu câu hỏi (Question Refinement)**: Làm sạch và chuẩn hóa câu hỏi của người dùng trước khi tiến hành truy xuất thông tin.
- **Tìm kiếm mở rộng tự động (Google Search Fallback)**: Khi dữ liệu nội bộ không đủ thông tin, hệ thống tự động tìm kiếm trên web thông qua Google Search để cung cấp câu trả lời tham khảo kèm nguồn uy tín.
- **Giao diện thân thiện (Gradio UI)**: Giao diện web trực quan, hiện đại, hỗ trợ các câu hỏi gợi ý theo danh mục và hiển thị tài liệu tham khảo trực quan ở bảng bên cạnh.

---

##  Kiến trúc hệ thống

Hệ thống được thiết kế theo mô hình mô-đun hóa với các thành phần cốt lõi:
1. **Dialogue Manager**: Quản lý lịch sử cuộc trò chuyện và trạng thái phiên làm việc của người dùng.
2. **Retrieval Module**:
   - Vector Store: Sử dụng **Qdrant** làm cơ sở dữ liệu vector.
   - Embedding Model: Sử dụng mô hình `bkai-foundation-models/vietnamese-bi-encoder` cho tiếng Việt chất lượng cao.
   - Lexical Search: **Rank-BM25**.
   - Reranker: Sử dụng Cross-Encoder (`cross-encoder/ms-marco-MiniLM-L-6-v2`) để tối ưu thứ tự tài liệu.
3. **Response Generator**: Tích hợp với mô hình LLM **Gemini 2.5 Flash** để tổng hợp câu trả lời chính xác, trích dẫn rõ ràng các điều khoản và văn bản pháp luật.

---

##  Cấu trúc thư mục dự án

```text
BTL-NLP/
├── data/                    # Thư mục chứa dữ liệu pháp luật
│   ├── corpus/              # Dataset chính (legal_corpus.json...) - [GitIgnored do dung lượng lớn]
│   └── utils/               # Stopwords và tệp bổ trợ
├── index/                   # Chỉ mục BM25 lưu cục bộ - [GitIgnored]
├── main/
│   └── chatbot.py           # Core logic của hệ thống RAG
├── utils/                   # Các module phụ trợ (retrieval, question_refiner, data_loader...)
├── css/
│   └── style.css            # Custom giao diện Gradio
├── app.py                   # Điểm chạy ứng dụng chính (Gradio Web UI)
├── setup_system.py          # Script cấu hình và cài đặt ban đầu
├── config.py                # File cấu hình tập trung cho toàn hệ thống
├── requirements.txt         # Khai báo thư viện phụ thuộc
├── .env.example             # File cấu hình biến môi trường mẫu
└── .gitignore               # Cấu hình bỏ qua các file dung lượng lớn
```

---

##  Hướng dẫn cài đặt và chạy ứng dụng

### 1. Yêu cầu hệ thống
- Python 3.9 - 3.11
- Git

### 2. Cài đặt môi trường ảo và thư viện
Tạo môi trường ảo và cài đặt các thư viện cần thiết:

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo (Windows)
venv\Scripts\activate

# Cài đặt thư viện phụ thuộc
pip install -r requirements.txt
```

### 3. Cấu hình biến môi trường
Tạo một file `.env` tại thư mục gốc của dự án với các thông tin sau:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
QDRANT_URL=your_qdrant_instance_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
```

### 4. Chuẩn bị dữ liệu và khởi động
Đảm bảo bạn đã tải file dataset `legal_corpus.json` vào thư mục `data/corpus/`.

Sau đó chạy ứng dụng:
```bash
python app.py
```

Ứng dụng sẽ tự động tải dữ liệu, xây dựng chỉ mục tìm kiếm và mở một giao diện Gradio trên trình duyệt của bạn (mặc định tại địa chỉ `http://127.0.0.1:7860`).

---
