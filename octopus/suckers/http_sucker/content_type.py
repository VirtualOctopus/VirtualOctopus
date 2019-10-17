from enum import Enum


class ContentType(Enum):

    """
    HTTP Content Type enum
    """

    html = "html"       # html
    xml = "xml"         # application xml
    json = "json"       # application json
    text = "text"       # text
    image = "image"     # image source
    binary = "binary"   # binary document, like PDF/word
    unknown = "unknown"
    empty = "empty"     # empty content


def is_text_content(c_type: ContentType) -> bool:
    """
    is text content
    """
    if c_type in [
        ContentType.html,
        ContentType.xml,
        ContentType.json,
        ContentType.text,
    ]:
        return True
    else:
        return False


def is_image(mimetype: str):

    if mimetype.startswith("image/"):
        return True
    else:
        return False


def is_doc(mimetype: str):
    if mimetype.startswith("application/vnd.") or (mimetype == "application/msword" or mimetype == "application/pdf"):
        return True
    else:
        return False
