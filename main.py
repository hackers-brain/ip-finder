# flags parser introduction
import argparse

flgs = argparse.ArgumentParser()
flags = flgs.add_mutually_exclusive_group(required=True)
flags.add_argument("-i", "--ip", help=" Enter IP Address.")

act = flgs.parse_args()

print(f" IP : {act.ip}")


# groups.py
# import argparse
#
# my_parser = argparse.ArgumentParser()
# my_group = my_parser.add_mutually_exclusive_group(required=True)
#
# my_group.add_argument('-v', '--verbose', action='store_true')
# my_group.add_argument('-s', '--silent', action='store_true')
#
# args = my_parser.parse_args()
#
# print(vars(args))


