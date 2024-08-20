import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hyeseonl/clearpath_ws/install/clearpath_config'
