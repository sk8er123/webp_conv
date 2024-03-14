from PIL import Image, ImageSequence
import glob

# 이미지 파일 목록을 가져옵니다.
image_files = glob.glob('/media/lee/data1/python_project/webp_conv/jpg/*.png')
print(image_files);
# 첫 번째 이미지를 열어 기준 이미지로 사용합니다.
base_image = Image.open(image_files[0])

# 나머지 이미지를 열어 리스트에 추가합니다.
image_sequence = [Image.open(img).convert("RGBA") for img in image_files[1:]]
print(image_sequence);
# 이미지들을 WebP로 저장하며 애니메이션으로 만듭니다.
base_image.save('output_animation.webp', save_all=True, append_images=image_sequence, loop=0, duration=100, quality=100)
