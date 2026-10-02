# Trợ lí AI điều khiển bài trình chiếu bằng cử chỉ

Dự án STEM Tin học 12 — THPT Marie Curie. Học sinh huấn luyện mô hình nhận diện
cử chỉ trên [Teachable Machine](https://teachablemachine.withgoogle.com/) (3 nhãn:
`tien`, `lui`, `nghi`), rồi nạp vào trang web để chuyển slide bằng cử chỉ qua webcam.

Mọi xử lý (webcam, mô hình) chạy trong trình duyệt của học sinh. Streamlit chỉ làm nhiệm
vụ phục vụ trang qua HTTPS nên trình duyệt cho phép dùng camera.

## Cấu trúc

| Tệp | Vai trò |
| --- | --- |
| `app.py` | Ứng dụng Streamlit, nhúng `index.html` |
| `index.html` | Trang điều khiển (JavaScript + TensorFlow.js + Teachable Machine) |
| `requirements.txt` | Thư viện cần cài |
| `.streamlit/config.toml` | Giao diện tối |

## Chạy thử trên máy

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Đưa lên Streamlit Community Cloud

1. Tạo repo GitHub mới và đẩy toàn bộ thư mục này lên (nhánh `main`).
2. Vào [share.streamlit.io](https://share.streamlit.io), đăng nhập bằng GitHub, chọn **Create app**.
3. Chọn repo, nhánh `main`, tệp chính `app.py`, rồi bấm **Deploy**.
4. Gửi đường link `*.streamlit.app` cho học sinh.

Lưu ý: app miễn phí sẽ "ngủ" khi lâu không ai dùng. Giáo viên nên mở link trước giờ học
để app khởi động xong (mất khoảng 30 giây).

## Học sinh dùng như thế nào

1. Mở link, dán đường dẫn mô hình Teachable Machine
   (*Export Model → Tensorflow.js → Upload my model*, kết thúc bằng dấu `/`).
2. Gõ nội dung slide của nhóm, mỗi dòng một slide.
3. Bấm **Nạp mô hình và bật camera**, rồi bấm **Cho phép** khi trình duyệt hỏi quyền camera.
