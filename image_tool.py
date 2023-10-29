from PIL import Image
from pathlib import Path

class ImageTool:
    
    def convert_format(source, destination):
        image = Image.open(source)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        destination_path = Path(destination)
        if not destination_path.parent.exists():
            destination_path.parent.mkdir(parents=True, exist_ok=True)
            
        image.save(destination)
