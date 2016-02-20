import os.path

import pysoup.utils.assets

class Logger(object):

    def __init__(self, cwd):
        self._log = ''
        self._cwd = cwd

    def log(self, text):
        self._log += '{0}\n'.format(text)

    def log_dependency_results(self, failed_dependencies):
        self.log('Dependency installation failure:')
        for dependency in failed_dependencies:
            self.log(dependency)

    def dump_to_file(self):
        if self._log != '':
            with open(os.path.join(self._cwd, 'soup.log'), 'wb') as f:
                f.write(pysoup.utils.assets.LOGO)
                f.write(self._log)
