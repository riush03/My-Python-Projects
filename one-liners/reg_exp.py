import sys,re
[sys.stdout.write(re.sub('PATTERN','SUBTRACTION',line)) for line in sys.stdin]