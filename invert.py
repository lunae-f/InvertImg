import os
from PIL import Image, ImageOps

# Dockerコンテナ内のディレクトリパス
INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'

def invert_images():
    """
    INPUT_DIR内のすべての画像の色を反転させ、OUTPUT_DIRに保存する
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created directory: {OUTPUT_DIR}")

    print(f"Processing images from: {INPUT_DIR}")
    
    for filename in os.listdir(INPUT_DIR):
        # サポートする画像形式を限定
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                input_path = os.path.join(INPUT_DIR, filename)
                output_path = os.path.join(OUTPUT_DIR, filename)

                with Image.open(input_path) as img:
                    # RGBモードでない場合は変換（透過情報などを保持するため）
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # 色を反転させる
                    inverted_img = ImageOps.invert(img)
                    
                    # 結果を保存
                    inverted_img.save(output_path)
                    print(f"  - Inverted and saved: {filename}")

            except Exception as e:
                print(f"Could not process {filename}: {e}")

    print("Image processing complete.")

if __name__ == '__main__':
    invert_images()