import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yash/steer_ws/src/swerve-steer/install/swerve-steer'
