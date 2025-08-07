"""
OPENING_TAG = OPTAG
CLOSING_TAG = CLTAG
CONTENT = CNTNT





parsed = {
WTFML: {
    FILE: {
        attributes: {
            hash: "SHA256",
            encryption: "fernet"
            }
        location: "/location/of/file"
        }
    }
}

"""


from wtfml.constants import SUPPORTED_TAGS
from wtfml.validator import validate_structure
from wtfml.validator import validate_tag
import re

# Regex to find opening tags, including those with attributes
tag_with_attributes_pattern = r"<(\w+)\s+([^>]+)>"
tag_without_attributes_pattern = r"<(\w+)>"
close_tag_pattern = r"</(\w+)>"
content_pattern = r"(?<=^|>)\s*([^<]+?)\s*(?=<|$)"

def parse_wtfml(raw_text: str):
    tokens = []

    with open(raw_text) as f:
        content = f.read()

        cleaned_content = " ".join(re.findall(r"\S+", content))

        for match in re.finditer(r"(<[^>]+>)|([^<]+)", cleaned_content):  # Group1: tags & Group2: Content
            # print(match)
            start, end = match.span()
            matched_content = cleaned_content[start:end]

            if match.group(1):  # Tags
                open_tag_with_attributes = re.match(tag_with_attributes_pattern, matched_content)

                if open_tag_with_attributes:
                    tag_name = open_tag_with_attributes.group(1)

                    validate_tag(tag_name)

                    attributes_str:list[str] = open_tag_with_attributes.group(2)
                    attributes = {}

                    for attr_match in re.finditer(r'(\w+)="([^"]*)"', attributes_str):
                        attributes[attr_match.group(1)] = attr_match.group(2)
                    tokens.append(("OPTAG", tag_name, attributes))

                else:
                    open_tag_without_attributes = re.match(tag_without_attributes_pattern, matched_content)

                    if open_tag_without_attributes:
                        tag_name = open_tag_without_attributes.group(1)
                        tokens.append(("OPTAG", tag_name))

                    else:
                        closed_tag_without_attributes = re.match(close_tag_pattern, matched_content)
                        tag_name = closed_tag_without_attributes.group(1)
                        tokens.append(("CLTAG", tag_name))


            elif match.group(2):
                tokens.append(("CNTNT", matched_content)) if matched_content != " " else ...

    return tokens




if __name__ == "__main__":
    file = "../tests/test_files/test_1.wtfml"
    print(parse_wtfml(file))
