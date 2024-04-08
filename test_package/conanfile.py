import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.build import can_run


class HALTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def validate(self):
        if not self.settings.os.vendor.board:
            raise ConanInvalidConfiguration("CMSIS requires a board to be specified")
        elif self.settings.os.vendor.board != "stm32f411ce":
            raise ConanInvalidConfiguration(
                "This test package will only work with STM32F411CE board!"
            )

    def requirements(self):
        self.requires(self.tested_reference_str)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.variables["CMAKE_C_COMPILER_WORKS"] = True
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self)

    def test(self):
        pass
