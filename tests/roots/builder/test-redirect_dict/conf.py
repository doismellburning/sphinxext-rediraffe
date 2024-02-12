extensions = ["sphinxext.rediraffe"]

master_doc = "index"
exclude_patterns = ["_build"]

html_theme = "basic"

rediraffe_branch = "HEAD~1"
rediraffe_redirects = {
    "lorem": "ipsum",
}
