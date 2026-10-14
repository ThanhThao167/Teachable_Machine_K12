<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<title>Trợ lí AI điều khiển bài trình chiếu bằng cử chỉ</title>
<style>
  :root{--bg:#111;--fg:#fff;--panel:#1d1d1d;--accent:#4da3ff}
  body{font-family:Arial,Helvetica,sans-serif;margin:0;background:var(--bg);color:var(--fg)}
  #slide{height:420px;display:flex;align-items:center;justify-content:center;font-size:40px;text-align:center;padding:24px;box-sizing:border-box;border-radius:10px 10px 0 0;background:#2a2a2a;transition:background-color .25s ease}
  #bar{display:flex;gap:18px;align-items:center;padding:10px 20px;background:var(--panel);flex-wrap:wrap;border-radius:0 0 10px 10px}
  #label{font-size:18px;min-width:230px}
  #thanhCho{height:6px;background:#333;border-radius:3px;width:140px;overflow:hidden}
  #thanhCho div{height:100%;width:0;background:var(--accent)}
  canvas{border-radius:8px;display:block}
  .nho{font-size:13px;color:#aaa}
  .loi{color:#ff8a80}
</style>
</head>
<body>

<div id="slide">Đang nạp mô hình và bật camera…</div>

<div id="bar">
  <div id="cam"></div>
  <div id="label">Cử chỉ: —</div>
  <div>
    <div class="nho">Thời gian chờ</div>
    <div id="thanhCho"><div id="thanhChoFill"></div></div>
  </div>
  <label class="nho"><input type="checkbox" id="lienTiep" checked> Cho phép lật liên tiếp khi giữ nguyên cử chỉ</label>
  <div id="pos" class="nho"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"></script>
<script>
// Đường dẫn mô hình và nội dung slide do app.py điền vào (học sinh nhập trên Streamlit)
const CAU_HINH = /*CAU_HINH*/null;

// ============================================================
//  THAM SỐ DO CON NGƯỜI ĐẶT RA — đây là chỗ con người giữ quyền
//  kiểm soát hệ thống AI. Nhóm phải giải thích được ý nghĩa (SP5).
// ============================================================
const NGUONG_TIN_CAY = 0.90;   // dưới mức này thì KHÔNG hành động
const THOI_GIAN_CHO  = 45;     // số khung hình nghỉ giữa 2 lần lật (~1,5 giây)

// Mỗi slide một màu nền riêng để nhận biết ngay bằng mắt là đã chuyển slide
// (lặp lại vòng nếu nhóm có nhiều hơn 8 slide).
const MAU_SLIDE = ["#2d5d7c","#6b3fa0","#1f7a5c","#a3401f","#7a1f4d","#4d5d1f","#1f4d7a","#7a1f1f"];

let SLIDES = [];
let model, webcam, ctx, i = 0, cooldown = 0, nhanTruoc = "nghi";

function render(){
  const o = document.getElementById("slide");
  o.innerText = SLIDES[i];
  o.style.background = MAU_SLIDE[i % MAU_SLIDE.length];
  document.getElementById("pos").innerText = "Slide " + (i + 1) + "/" + SLIDES.length;
}

function baoLoi(thongBao){
  const o = document.getElementById("slide");
  o.innerHTML = "";
  const p = document.createElement("div");
  p.className = "loi";
  p.style.fontSize = "20px";
  p.innerText = thongBao;
  o.appendChild(p);
}

async function batDau(){
  if (!CAU_HINH){ baoLoi("Chưa có cấu hình. Hãy nhập đường dẫn mô hình ở phía trên."); return; }
  const URL_MODEL = CAU_HINH.url;
  SLIDES = CAU_HINH.slides;
  try{
    model = await tmPose.load(URL_MODEL + "model.json", URL_MODEL + "metadata.json");
  }catch(e){
    baoLoi("Không nạp được mô hình. Kiểm tra lại đường dẫn (Export Model → Tensorflow.js → Upload my model) và kết nối mạng.");
    return;
  }
  try{
    // Tự xin camera trước: tmPose chỉ báo lỗi chung chung, còn ở đây biết rõ nguyên nhân
    const thu = await navigator.mediaDevices.getUserMedia({ video: true });
    thu.getTracks().forEach(t => t.stop());
    webcam = new tmPose.Webcam(200, 200, true);          // true = lật gương
    await webcam.setup();                                // trình duyệt xin quyền camera
    await webcam.play();
  }catch(e){
    const ten = (e && e.name) || "";
    if (ten === "NotAllowedError") baoLoi("Trình duyệt đang chặn camera. Bấm biểu tượng camera trên thanh địa chỉ → Cho phép, rồi tải lại trang.");
    else if (ten === "NotFoundError") baoLoi("Không tìm thấy webcam. Hãy cắm webcam rồi tải lại trang.");
    else if (ten === "NotReadableError") baoLoi("Webcam đang bị phần mềm khác dùng (Zoom, Teams…). Đóng phần mềm đó rồi tải lại trang.");
    else baoLoi("Không bật được camera. Kiểm tra webcam và quyền camera của trình duyệt.");
    return;
  }
  const c = document.createElement("canvas");
  c.width = 200; c.height = 200;
  ctx = c.getContext("2d");
  document.getElementById("cam").appendChild(c);
  render();
  window.requestAnimationFrame(loop);
}

async function loop(){
  webcam.update();
  await predict();
  window.requestAnimationFrame(loop);
}

async function predict(){
  const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
  const pred = await model.predict(posenetOutput);

  let best = pred[0];
  for (const p of pred) if (p.probability > best.probability) best = p;
  document.getElementById("label").innerText =
      "Cử chỉ: " + best.className + " (" + (best.probability * 100).toFixed(0) + "%)";

  // Hai điều kiện luôn phải thoả: đủ tin cậy VÀ đã hết thời gian chờ.
  let duocPhep = best.probability > NGUONG_TIN_CAY && cooldown <= 0;

  // Lựa chọn thiết kế của nhóm: có cho lật liên tiếp khi giữ nguyên cử chỉ không?
  // Bỏ chọn ô này = mỗi lần muốn lật phải hạ tay về "nghi" rồi giơ lại.
  if (!document.getElementById("lienTiep").checked) duocPhep = duocPhep && best.className !== nhanTruoc;

  if (duocPhep){
    if (best.className === "tien" && i < SLIDES.length - 1){ i++; render(); cooldown = THOI_GIAN_CHO; }
    else if (best.className === "lui" && i > 0){ i--; render(); cooldown = THOI_GIAN_CHO; }
  }
  nhanTruoc = best.className;

  if (cooldown > 0) cooldown--;
  document.getElementById("thanhChoFill").style.width = (cooldown / THOI_GIAN_CHO * 100) + "%";

  if (webcam.canvas) ctx.drawImage(webcam.canvas, 0, 0);
}

batDau();
</script>
</body>
</html>
