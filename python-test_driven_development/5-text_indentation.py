#!/usr/bin/python3
"""Module that defines text_indentation function.
"""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    line = ""
    i = 0
    length = len(text)

    while i < length:
        ch = text[i]

        if ch in separators:
            # احذف الفراغات في نهاية السطر قبل العلامة
            line = line.rstrip()
            line += ch
            print(line, end="\n\n")
            line = ""

            # تخطَّ كل الفراغات بعد العلامة
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue

        # تجاهل الفراغات في بداية السطر
        if not line and ch == " ":
            i += 1
            continue

        line += ch
        i += 1

    # اطبع الباقي إن وجد بدون فراغات في البداية/النهاية
    line = line.strip()
    if line:
        print(line, end="")
