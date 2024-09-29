#!/usr/bin/env python3
"""a function called filter_datum that returns the log message obfuscated"""
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    pattern = r'(' + '|'.join(fields) + r')=' + r'[^;]*'
    return re.sub(
        pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)
