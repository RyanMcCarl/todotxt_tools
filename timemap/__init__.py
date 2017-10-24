import os
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

__all__ = ['task', 'todotxt_cleanup', 'regexes', 'todotxt_utils']

if __name__ == '__main__':
    todotxt_cleanup.main()