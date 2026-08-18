import warnings

def stichHTMLFile(filepath: str):
    warnings.warn(
        f"Using stitchHTMLFile('{filepath}') is not reccomended\n"
        "Instead you should make your website into 1 file",
        UserWarning,
        2
    )
    with open(filepath, "r") as f:
        htmlCode: str = f.read()

    htmlCodeList = htmlCode.splitlines()

    for index, line in enumerate(htmlCodeList):
        if "link" in line:
            tokens = (
                line.replace("<", "")
                .replace("link", "")
                .replace("/>", "")
                .replace('"', "")
                .strip()
                .split()
            )

            code = {}

            for token in tokens:
                if "rel" in token:
                    code["type"] = token.replace("rel=", "")
                if "href" in token:
                    code["file"] = token.replace("href=", "")

            if code.get("type") == "stylesheet":
                if code.get("file"):
                    with open(code["file"], "r") as f:
                        htmlCodeList[index] = f"<style>\n{f.read()}\n</style>"

        if "script" in line:
            if "src" in line:
                token = (
                    line.replace("<script", "")
                    .replace("src=", "")
                    .removesuffix("/>")
                    .replace('"', "")
                    .strip()
                )
                with open(token, "r") as f:
                    htmlCodeList[index] = f"<script>\n{f.read()}\n</script>"
            else:
                continue

    return "\n".join(htmlCodeList)
