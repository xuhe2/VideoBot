from ddddocr import DdddOcr
from PIL import Image


def captcha_solver(img_path: str, captcha_len: int = None) -> str:
    ocr: DdddOcr = DdddOcr()
    with open(img_path, 'rb') as f:
        img_bytes: bytes = f.read()
    res: str = ocr.classification(img_bytes)

    if captcha_len is not None and len(res) != captcha_len:  # 如果验证码长度不是captcha_len位
        raise ValueError(f'验证码长度错误，应为{captcha_len}位')

    return res


# 截图
def screenshot(img_path: str, l: int, t: int, r: int, b: int) -> None:
    img: Image.Image = Image.open(img_path)
    img = img.crop((l, t, r, b))  # 截取图像
    img.save(img_path)  # 保存图像
    img.close()  # 关闭图像


if __name__ == '__main__':
    screenshot('zjooc.png')
    print(captcha_solver('zjooc.png'))
