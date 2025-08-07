from wtfml.constants import SUPPORTED_TAGS
from wtfml.constants import ERROR_MESSAGES
from errors import NameError

def validate_structure():
    ...

def validate_tag(tag: str):
    if tag not in SUPPORTED_TAGS:
        raise NameError(ERROR_MESSAGES["UNSUPPORTED_TAG"].replace("TAG", tag))



if __name__ == '__main__':
    print(validate_tag("MSG"))