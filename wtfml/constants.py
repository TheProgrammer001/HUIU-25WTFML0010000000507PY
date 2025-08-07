SUPPORTED_TAGS = {
    "WTFML", "FILE", "NAME", "SIZE", "HASH", "CONTENT", "MSG", "CMD", "TARGET", "ENCRYPTION", "ALGORITHM", "AUTHOR"
}

VERSION_RULES = {
    "1.0.0": {
        "FILE": ["NAME", "SIZE", "CONTENT"]
    }
}

DEFAULT_ENCODING = "utf-8"

ERROR_MESSAGES = {
    "MISSING_NAME": "Missing <NAME> tag in <FILE>",
    "MISSING_SIZE": "MISSING <SIZE> tag in <FILE>",
    "MISSING_CONTENT": "Missing <CONTENT> tag in <FILE>",
    "UNSUPPORTED_TAG": "<TAG> is not a supported tag"
}