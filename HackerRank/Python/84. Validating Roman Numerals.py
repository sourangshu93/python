regex_pattern = regex_pattern = r"([M]{0,3})?(C[MD]|D?C{0,3})?([X]{0,3}[L]{0,1}[C]{0,1}|[L]{0,1}[X]{0,3})?([I]{0,3}[V]{0,1}[X]{0,1}|[V]{0,1}[I]{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))