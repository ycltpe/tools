import pytesseract
from PIL import Image

# 设置 Tesseract 语言为中文简体
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # 设置 tesseract 路径
lang = 'chi_sim'  # 指定中文简体语言包

# 读取图片
img = Image.open('image.png')

# 使用Tesseract进行OCR识别
# 使用 Tesseract 进行中文文字识别
text = pytesseract.image_to_string(img, lang=lang)

# 输出识别结果
print(text)
