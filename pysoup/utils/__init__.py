import os.path

from twisted.internet import defer, utils


@defer.inlineCallbacks
def execute_shell_command(command):
    s, e, code = yield utils.getProcessOutputAndValue('/bin/bash',
                                                      args=['-c', command])
    defer.returnValue(code)

def get_asset(asset_name):
    assets_dir = os.path.join(os.path.dirname(__file__), '../../assets')
    with open(os.path.join(assets_dir, asset_name), 'rb') as f:
        contents = f.read()

    return contents
