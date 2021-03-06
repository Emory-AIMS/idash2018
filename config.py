from pathlib import Path
import json

NUM_NODE = 4

auth = None
with open('auth.json') as f:
    auth = json.load(f)

# print(auth)
# config = {
#     "rpcuser": 'multichainrpc',
#     "rpcpasswd": 'emory',
#     "rpchost": '127.0.0.1',
#     "rpcport": 8570,
#     "chainname": 'chain1'
# }

# time, node, ID, ref-ID, user, activity, resource
ATTRIBUTE = ['T', 'N', 'I', 'r', 'U', 'A', 'R']
ATTRIBUTE_NAME = ['Timestamp', 'Node', 'ID',
                  'Ref-ID', 'User', 'Activity', 'Resource']
ATTRIBUTE_TYPE = {'Timestamp': int, 'Node': int, 'ID': int,
                  'Ref-ID': int, 'User': int, 'Activity': str, 'Resource': str}

ATTRIBUTE_INDEX = {'Timestamp': 0, 'Node': 1, 'ID': 2,
                   'Ref-ID': 3, 'User': 4, 'Activity': 5, 'Resource': 6}

ATT_S2F = {short: full for short, full in zip(ATTRIBUTE, ATTRIBUTE_NAME)}

FILE_SIZE = 100

datadir = Path('./testData').joinpath(str(FILE_SIZE))

MAX_RESULT = NUM_NODE * FILE_SIZE

ENCODE_FORMAT = 'ascii'

NLEVEL = 1
SCALE = 10000
STEP = 100
PREFIX = 'ts'

DATA = 'Node'


DELIMITER = '\t'
