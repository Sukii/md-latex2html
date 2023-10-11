import sys
import re
import markdown
import latex2mathml.converter
file = sys.argv[1]
f=open(file)
input = "".join(f.readlines())

ls = re.split(r"[$]+",input)
sm = ""
for i,s in enumerate(ls):
    if i%2 == 1:
        mml = latex2mathml.converter.convert(s)
        sm += mml
    else:
        sm += s



html = markdown.markdown(sm, extensions=['md_in_html'])


print("""
<!DOCTYPE html>
<html>
  <head>
  <meta charset='utf-8'>
</head>
<body>
""")
print(html)
print("""
</body>
</html>""")
