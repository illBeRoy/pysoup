from twisted.internet import defer, utils


@defer.inlineCallbacks
def execute_shell_command(command):
    s, e, code = yield utils.getProcessOutputAndValue('/bin/bash',
                                                      args=['-c', command])
    defer.returnValue(code)
