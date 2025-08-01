import re
from typing import List


def get_lines(s):
    return [i for i in s.split("\n") if i.strip()]


def parse_and_handle(pattern: str, data: List[str], handle):
    for i in data:
        match = re.findall(pattern, i)
        handle(match[0])
