# re.match()
import re

m = re.match(r'py',"current python version")
print(m)


# re.search()

m = re.search(r'PY',"current python version",re.IGNORECASE)
print(m)
