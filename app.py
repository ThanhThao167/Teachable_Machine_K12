import json
from pathlib import Path

import streamlit as st

THU_MUC = Path(__file__).parent
MO_HINH_MAU = "https://teachablemachine.withgoogle.com/models/_c-_TFkuu/"
SLIDE_MAC_DINH = """Slide 1 — Tên dự án của nhóm
Slide 2 — Vấn đề thực tiễn
Slide 3 — Cách nhóm thu thập dữ liệu
Slide 4 — Kết quả kiểm thử
Slide 5 — Bài học về đạo đức AI"""
CU_CHI = [
    ("tien", "Tiến", "Chuyển sang slide sau"),
    ("lui", "Lùi", "Quay lại slide trước"),
    ("nghi", "Nghỉ", "Đứng yên, không lật slide"),
]

st.set_page_config(
    page_title="Trợ lí AI điều khiển trình chiếu bằng cử chỉ",
    page_icon=":material/slideshow:",
    layout="wide",
)

st.session_state.setdefault("url_mo_hinh", "")
st.session_state.setdefault("noi_dung_slide", SLIDE_MAC_DINH)


def dung_mo_hinh_mau():
    st.session_state.url_mo_hinh = MO_HINH_MAU


st.title("Trợ lí AI điều khiển bài trình chiếu bằng cử chỉ")
st.caption("Dự án STEM Tin học 12 · THPT Marie Curie")

with st.expander("Chuẩn bị trước khi test", icon=":material/checklist:"):
    st.markdown(
        """
1. Dùng máy có **webcam** và trình duyệt **Chrome** hoặc **Edge**, có Internet.
2. Đóng Zoom, Teams hoặc phần mềm đang chiếm camera.
3. Bấm **Cho phép (Allow)** khi trình duyệt hỏi quyền camera.
4. Đứng cách camera 1,5–2 m, thấy rõ nửa thân trên và hai tay.
"""
    )

# ---------- Bước 1: mô hình mẫu của giáo viên ----------
st.subheader("1. Mô hình mẫu của giáo viên", divider="gray")
st.markdown(
    "Mô hình mẫu nhận 3 cử chỉ dưới đây. Nhóm nào **chưa làm xong mô hình** "
    "thì dùng tạm mô hình mẫu để thử trước."
)

with st.container(horizontal=True, gap="medium"):
    for ten_tep, nhan, y_nghia in CU_CHI:
        with st.container(border=True):
            anh = THU_MUC / f"{ten_tep}.png"
            if anh.exists():
                st.image(anh, alt=f"Cử chỉ {nhan}: {y_nghia.lower()}", width="stretch")
            else:
                st.warning(f"Thiếu ảnh `{ten_tep}.png`", icon=":material/image_not_supported:")
            st.markdown(f"**{nhan}** · nhãn `{ten_tep}`")
            st.caption(y_nghia)

st.markdown("Đường dẫn mô hình mẫu (bấm biểu tượng sao chép ở góc phải):")
st.code(MO_HINH_MAU, language=None)

# ---------- Bước 2: nạp mô hình ----------
st.subheader("2. Nạp mô hình và nội dung slide", divider="gray")

with st.form("form_nap_mo_hinh"):
    url = st.text_input(
        "Đường dẫn mô hình Teachable Machine",
        key="url_mo_hinh",
        placeholder="https://teachablemachine.withgoogle.com/models/xxxxxxxx/",
        help="Teachable Machine → Export Model → Tensorflow.js → Upload my model.",
    )
    noi_dung = st.text_area(
        "Nội dung các slide của nhóm (mỗi dòng là một slide)",
        key="noi_dung_slide",
        height=150,
    )
    with st.container(horizontal=True):
        bat_dau = st.form_submit_button(
            "Nạp mô hình và bật camera", type="primary", icon=":material/videocam:"
        )
        dung_mau = st.form_submit_button(
            "Dùng mô hình mẫu của GV",
            icon=":material/school:",
            on_click=dung_mo_hinh_mau,
        )

if bat_dau or dung_mau:
    url = st.session_state.url_mo_hinh.strip()
    slides = [dong for dong in noi_dung.splitlines() if dong.strip()]
    if not url.startswith(("https://", "http://")):
        st.error("Đường dẫn mô hình chưa đúng. Đường dẫn phải bắt đầu bằng `https://`.")
    elif not slides:
        st.error("Hãy nhập ít nhất một dòng nội dung slide.")
    else:
        if not url.endswith("/"):
            url += "/"
        st.session_state.cau_hinh = {"url": url, "slides": slides}

# ---------- Bước 3: trình chiếu ----------
cau_hinh = st.session_state.get("cau_hinh")
if cau_hinh:
    st.subheader("3. Trình chiếu bằng cử chỉ", divider="gray")
    if cau_hinh["url"] == MO_HINH_MAU:
        st.caption(":material/school: Đang dùng mô hình mẫu của giáo viên.")
    else:
        st.caption(f":material/model_training: Đang dùng mô hình: `{cau_hinh['url']}`")
    # Thay "<" để nội dung slide không thể đóng thẻ <script> trong trang
    du_lieu = json.dumps(cau_hinh, ensure_ascii=False).replace("<", "\\u003c")
    trang = (THU_MUC / "index.html").read_text(encoding="utf-8")
    st.iframe(
        trang.replace("/*CAU_HINH*/null", du_lieu),
        height=640,
        alt="Trang trình chiếu điều khiển bằng cử chỉ qua webcam",
    )
