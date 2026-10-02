from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Trợ lí AI điều khiển trình chiếu bằng cử chỉ",
    page_icon=":material/slideshow:",
    layout="wide",
)

st.title("Trợ lí AI điều khiển bài trình chiếu bằng cử chỉ")
st.caption("Dự án STEM Tin học 12 · THPT Marie Curie")

with st.expander("Chuẩn bị trước khi test", icon=":material/checklist:"):
    st.markdown(
        """
1. Dùng máy có **webcam** và trình duyệt **Chrome** hoặc **Edge**, có Internet.
2. Đóng Zoom, Teams hoặc phần mềm đang chiếm camera.
3. Chuẩn bị **đường dẫn mô hình** Teachable Machine
   (*Export Model → Tensorflow.js → Upload my model*, kết thúc bằng dấu `/`).
4. Chuẩn bị **nội dung slide** của nhóm, mỗi dòng một slide.
5. Bấm **Cho phép (Allow)** khi trình duyệt hỏi quyền camera.
6. Đứng cách camera 1,5–2 m, thấy rõ nửa thân trên và hai tay.
"""
    )

st.iframe(Path(__file__).with_name("index.html"), height=1000)
