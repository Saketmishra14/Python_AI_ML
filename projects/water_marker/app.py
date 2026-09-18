from PIL import Image,ImageDraw,ImageFont
import os


def add_text_watermark_to_folder(
    input_dir,output_dir,watermark_text,position,font_size
):
    
    # create output directory if it is doens't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg",".jpeg",".png",".bmp")):
            image_path=os.path.join(input_dir,filename)
            original=Image.open(image_path)
            width,height=original.size
            
            # create image draw object
            draw=ImageDraw.Draw(original)
            
            # setup font
            font=ImageFont.truetype("super_nought.ttf",size=font_size)
            
            
            
            # get the text dimension
            
            text_width=font.getmask(watermark_text).getbbox()[2]
            text_height=font.getmask(watermark_text).getbbox()[3]
            
            margin=100
            #get the cord to place the watermark in the bottom right corner
            
            a=width-text_width-margin
            b=height-text_height-margin
            
            # apply the watermarker
            
            draw.text((a,b),text=watermark_text,fill="white",font=font)
            
            #see the watermark image in output_directory
            
            output_path=os.path.join(output_dir,f"watermarked_{filename}")
            original.save(output_path)
            
            
            
input="./input_dir"
output="./output_dir"
watermark="@sonyIndia"

add_text_watermark_to_folder(input_dir=input,
    output_dir=output,
    watermark_text=watermark,
    position=(50,50),
    font_size=100
    )