#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(width, height, text, filename, bg_color=(139, 124, 246), text_color=(255, 255, 255)):
    """Create a placeholder image with text"""
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # Try to use a font, fallback to default if not available
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill=text_color, font=font)
    
    # Save the image
    image.save(f'assets/{filename}')
    print(f"Created {filename}")

# Create directory if it doesn't exist
os.makedirs('assets', exist_ok=True)

# Create placeholder images
create_placeholder(400, 400, "Shruti Jayaswal\nProfile Photo", "profile.jpg", (248, 187, 217))
create_placeholder(500, 500, "About\nShruti", "about-image.jpg", (191, 219, 254))
create_placeholder(350, 250, "Agency & Client\nManagement", "project1.jpg", (221, 214, 254))
create_placeholder(350, 250, "E-Learn Hub\nCourse System", "project2.jpg", (187, 247, 208))
create_placeholder(350, 250, "Snake Game\nJavaScript", "project3.jpg", (254, 243, 199))
create_placeholder(350, 250, "Drawing App\nCanvas API", "project4.jpg", (254, 215, 170))

print("All placeholder images created successfully!")
