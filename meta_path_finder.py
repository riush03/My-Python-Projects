"""
  Meta path finder is an object that will allow you to load custom objects
  as will as standard .py(python) files
"""
import os.path
import sys

class MetaPathFinder(object):

    def find_on_path(self,file_name):
        targ_file = ["%s/__init__.hy","%s.hy"]
        dir_path = "/".join(file_name.split("."))

        for f_path in sys.path:
            f_path = os.path.abspath(f_path)
            for fp in targ_file:
                composed_pat = fp % ("%s%s"%(f_path,dir_path))
                if os.path.exists(composed_pat):
                    return composed_pat

    def find_file(self,file_name,path=None):
        path = self.find_on_path(file_name)
