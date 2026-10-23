from pathlib import Path
import encode
image_path = Path.home() / "Desktop/Base64/Encoder/GHC_Logo.png"
encode.encode(str(image_path))
image_path2 = Path.home() / "Desktop/Base64/Encoder/testing_image.png"
encode.encode(str(image_path2))
