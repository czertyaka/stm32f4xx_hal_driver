from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout

class cmsisRecipe(ConanFile):
    name = "hal"
    version = "1.8.2"

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "Inc/*", "Src/*"

    def validate(self):
        if self.settings.os != "baremetal":
            raise ConanInvalidConfiguration(
                "CMSIS could not be built for profile with operting system"
            )
        elif not self.settings.os.vendor.board:
            raise ConanInvalidConfiguration("CMSIS requires a board to be specified")
        elif not str(self.settings.os.vendor.board).lower().startswith("stm32f4"):
            raise ConanInvalidConfiguration("This recipe is for STM32F4xx boards")

    def requirements(self):
        self.requires("cmsis/5.6")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.variables["BOARD"] = str(self.settings.os.vendor.board).upper()
        tc.variables["CMAKE_C_COMPILER_WORKS"] = True
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["hal"]
