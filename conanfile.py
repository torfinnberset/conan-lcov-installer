import os

from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LcovConan(ConanFile):
    name = "lcov_installer"
    version = "1.14"
    license = "GPL"
    author = "Torfinn Berset <torfinn@bloomlife.com>"
    url = "https://github.com/torfinnberset/conan-lcov-installer"
    homepage = "http://ltp.sourceforge.net/coverage/lcov.php"
    description = "A graphical front-end for GCC's coverage testing tool gcov"
    topics = ("coverage", "testing", "gnu", "tool", "perl")
    settings = ()  # written in perl

    _filename = F"lcov-{version}"

    _version_sha256 = {
        "1.14": "14995699187440e0ae4da57fe3a64adc0a3c5cf14feab971f8db38fb7d8f071a"
    }

    def source(self):
        url = F"https://datapacket.dl.sourceforge.net/project/ltp/" \
              F"Coverage%20Analysis/LCOV-{self.version}/{self._filename}.tar.gz"
        tools.get(url, sha256=self._version_sha256[self.version])

    def package(self):
        with tools.chdir(self._filename):
            self.output.info(F"Patching and installing lcov")
            tools.replace_path_in_file("Makefile", "/usr/local", self.package_folder)

            env_build = AutoToolsBuildEnvironment(self)
            env_build.make(target="install")

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
        self.output.success("Added lcov to $PATH")
