import traceback
import sys

try:
    import backend.main
except Exception as e:
    traceback.print_exc(file=sys.stdout)
