import qrcode
from PIL import Image,ImageDraw,ImageFont
def get_qrcode():
    qr=qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data('http://192.168.2.6:8000')
    qr.make(fit=True)
    image=qr.make_image(fill_color="black", back_color="white")
    image.save('line_chart.png')
    # image=qrcode.make('http://192.168.2.6:8000')

def get_logqrcode():
    #使用PIL打开图片并转换成RGB刻度模式
    img=Image.open('line_chart.png').convert('RGB')
    log=Image.open(r"C:\Users\qlok\Desktop\pic\15743843152335168.png").convert('RGB')
    # log_bg=Image.new('RGB',log.size,'white')
    size=120
    log_bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    w,h=log_bg.size
    draw = ImageDraw.Draw(log_bg)
    draw.ellipse((0,0,w-1,h-1),outline='white',fill='#FF6600')
    #压缩log
    log.thumbnail((80,80))
    log_bg_w,log_bg_h=log_bg.size
    img_w, img_h = img.size
    log_w, log_h = log.size
    offset1=((log_bg_w-log_w)//2,(log_bg_h-log_h)//2)
    offset=((img_w-log_w)//2, (img_h-log_h)//2)
    log_bg.paste(log,offset1)
    log_bg.save('x.png')
    #将log粘贴到二维码上
    img.paste(log_bg, offset, mask=log_bg)
    img.save('x.png')
    img.save('log_line_chart.png')
    text='与此处——洞见别样天色'
    ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype('msyh.ttc', 24)
    except:
        font = ImageFont.load_default()
    box=font.getbbox(text)
    text_w,text_h=box[2]-box[0],box[3]-box[1]
    text_ps=((img_w-text_w)//2,(img_h+5))
    new_h=img_h+text_h+25
    img_w=img.size[0]
    image_combined = Image.new('RGB', (img_w, new_h), color="#0097A7")
    image_combined.paste(img,(0,0))
    draw=ImageDraw.Draw(image_combined)
    draw.text(text_ps,text,font=font,fill='black')
    img=image_combined
    img.save('lok.png')

if __name__ == '__main__':
    get_qrcode()
    get_logqrcode()

