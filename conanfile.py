from conans import ConanFile, AutoToolsBuildEnvironment, tools


class LcovConan(ConanFile):
    name = "lcov"
    version = "1.14"
    license = "GPL"
    author = "Torfinn Berset <torfinn@bloomlife.com>"
    url = "https://github.com/torfinnberset/conan-lcov-installer"
    homepage = "http://ltp.sourceforge.net/coverage/lcov.php"
    description = "A graphical front-end for GCC's coverage testing tool gcov"
    topics = ("coverage", "testing", "gnu", "tool", "perl")
    settings = ()  # written in perl

    _filename = F"lcov-{version}"

    def source(self):
        url = F"https://datapacket.dl.sourceforge.net/project/ltp/" \
              F"Coverage%20Analysis/LCOV-{self.version}/{self._filename}.tar.gz"
        tools.get(url)

    def package(self):
        with tools.chdir(self._filename):
            self.output.info(F"Patching and installing lcov")
            tools.replace_path_in_file("Makefile", "/usr/local", self.package_folder)

            env_build = AutoToolsBuildEnvironment(self)
            env_build.make(target="install")
