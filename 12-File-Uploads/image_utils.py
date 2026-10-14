import uuid
from io import BytesIO
from pathlib import Path
from PIL import Image,ImageOps

PROFILE_PICS_DIR = Path(__file__).parent.parent / "static" / "profile_pics"