#!/usr/bin/env python
# -*- coding: utf_8 -*-
import os
import subprocess
import sys
import time
import re
import codecs


def gen_release_note(changelog_path, releasenote_path):
    regex = r"^(## version.*?)[^#]#"
    test_str = codecs.open(changelog_path, "r", "utf-8").read()
    matches = re.findall(regex, test_str, re.MULTILINE | re.DOTALL)
    if matches and len(matches) > 0:
        # print(matches[0])
        codecs.open(releasenote_path, "w", "utf-8").write(matches[0])


if __name__ == '__main__':
    try:
        changelog_path = os.path.join(os.getcwd(), "docs", "Changelog.md")
        releasenote_path = os.path.join(os.getcwd(), "RELEASE.md")
        gen_release_note(changelog_path, releasenote_path)

        print("Done.")
    except Exception as e:
        print(e)
