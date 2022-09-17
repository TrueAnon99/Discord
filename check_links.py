#!/usr/bin/env python

import logging
import sys
import re
from pathlib import Path

LINK_REGEX = re.compile("(/(.+).html)")
log = logging.getLogger(__name__)


def main():
    readme_page_links = set()
    docs_folder = Path.cwd() / "docs"
    readme_path = docs_folder / "README.md"
    with readme_path.open(mode="r") as readme_fp:
        for line in readme_fp:
            link_match = LINK_REGEX.search(line)
            if not link_match:
                continue
            readme_page_links.add(link_match.group(1))

    log.info("README has %d links", len(readme_page_links))

    pages = set()
    for page_path in docs_folder.glob("**/*"):
        if not page_path.is_file():
            continue

        if "README.md" in str(page_path):
            continue

        if ".vuepress/config.js" in str(page_path):
            continue

        built_link = page_path.parent / (page_path.stem + ".html")
        relative_page = built_link.relative_to(docs_folder)
        pages.add("/" + str(relative_page))

    log.info("we have %d pages", len(pages))

    unlinked = pages - readme_page_links

    log.error("there are %d unlinked pages from README", len(unlinked))
    for unlinked_page in unlinked:
        log.error("%r is not linked from README", unlinked_page)
    if unlinked:
        return 1

    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sys.exit(main())
