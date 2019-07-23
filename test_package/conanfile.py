import os

from conans import ConanFile
from six import StringIO


class LcovTestConan(ConanFile):
    def test(self):
        output = StringIO()
        lcov_path = os.path.join(self.deps_cpp_info["lcov_installer"].rootpath, "bin", "lcov")
        self.run("{} --version".format(lcov_path), output=output, run_environment=True)
        self.output.info("Installed: %s" % str(output.getvalue()))
        ver = str(self.requires["lcov_installer"].ref.version)

        value = str(output.getvalue())
        lcov_version = value.split('\n')[0]
        self.output.info("Expected value: {}".format(ver))
        self.output.info("Detected value: {}".format(lcov_version))
        assert (ver in lcov_version)
