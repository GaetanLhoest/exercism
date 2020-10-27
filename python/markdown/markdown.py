import re

BOLD_REGEX = '(.*)__(.*)__(.*)'
BOLD_TAGS = ('<strong>', '</strong>')


ITALIC_REGEX = '(.*)_(.*)_(.*)'
ITALIC_TAGS = ('<em>', '</em>')

LIST_TAGS = ('<li>', '</li>', '<ul>', '</ul>')


def convert(line, regex, tags):
    match = re.match(regex, line)
    if match:
        return match.group(1) + tags[0] + \
            match.group(2) + tags[1] + match.group(3)
    return line


def extract_list_element(line):
    match = re.match(r'\* (.*)', line)
    if match:
        return match.group(1)
    return None


def format_paragraph(line):
    m = re.match('<h|<ul|<p|<li', line)
    if not m:
        return '<p>' + line + '</p>'
    return line


def format_list(line, start_list=False, end_list=False, end_text=False):
    if end_list:
        return LIST_TAGS[3] + line
    if end_text:
        return line + LIST_TAGS[3]

    line = LIST_TAGS[0] + line + LIST_TAGS[1]
    if start_list:
        line = LIST_TAGS[2] + line

    return line


def convert_titles(line):
    if re.match('###### (.*)', line) is not None:
        return '<h6>' + line[7:] + '</h6>'
    elif re.match('## (.*)', line) is not None:
        return '<h2>' + line[3:] + '</h2>'
    elif re.match('# (.*)', line) is not None:
        return '<h1>' + line[2:] + '</h1>'
    return line


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    for line in lines:
        line = convert_titles(line)
        line = convert(line, BOLD_REGEX, BOLD_TAGS)
        line = convert(line, ITALIC_REGEX, ITALIC_TAGS)
        list_element = extract_list_element(line)

        if list_element:
            line = list_element
            if not in_list:
                in_list = True
                line = format_list(line, start_list=True)
            else:
                line = format_list(line)
        else:
            line = format_paragraph(line)
            if in_list:
                in_list = False
                line = format_list(line, end_list=True)

        res += line
    if in_list:
        res = format_list(res, end_text=True)
    return res
