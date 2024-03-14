from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        images = []
        fileNames = request.form.get('fileNames', "")
        parts = fileNames.split("&")

        for part in parts:
            if part.startswith("data:image/png;base64,"):
                part = part.split(",")[1]
            # Base64 문자열을 바이너리 데이터로 변환하고 이미지로 열기
            image_data = base64.b64decode(part)
            image = Image.open(io.BytesIO(image_data)).convert("RGBA")
            images.append(image)

        quality = int(request.form.get('quality', 80))  # 기본값으로 80 사용
        duration = int(request.form.get('duration', 100))  # 기본값으로 100ms 사용
        
        # 메모리 파일에 WebP 이미지를 저장
        img_byte_arr = io.BytesIO()
        images[0].save(img_byte_arr, format='WEBP', save_all=True, append_images=images[1:], duration=duration, loop=0, quality=quality)
        img_byte_arr.seek(0)

        # 사용자에게 WebP 이미지 전송
        return send_file(img_byte_arr, mimetype='image/webp', as_attachment=True, attachment_filename='animation.webp')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
