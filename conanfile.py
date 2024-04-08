from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout

class cmsisRecipe(ConanFile):
    name = "hal"
    version = "1.8.2"

    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "Inc/*", "Src/*"

    options = {
        "HAL_ADC_MODULE_ENABLED": [True, False],
        "HAL_CAN_MODULE_ENABLED": [True, False],
        "HAL_CAN_LEGACY_MODULE_ENABLED": [True, False],
        "HAL_CRC_MODULE_ENABLED": [True, False],
        "HAL_CEC_MODULE_ENABLED": [True, False],
        "HAL_CRYP_MODULE_ENABLED": [True, False],
        "HAL_DAC_MODULE_ENABLED": [True, False],
        "HAL_DCMI_MODULE_ENABLED": [True, False],
        "HAL_DMA_MODULE_ENABLED": [True, False],
        "HAL_DMA2D_MODULE_ENABLED": [True, False],
        "HAL_ETH_MODULE_ENABLED": [True, False],
        "HAL_ETH_LEGACY_MODULE_ENABLED": [True, False],
        "HAL_FLASH_MODULE_ENABLED": [True, False],
        "HAL_NAND_MODULE_ENABLED": [True, False],
        "HAL_NOR_MODULE_ENABLED": [True, False],
        "HAL_PCCARD_MODULE_ENABLED": [True, False],
        "HAL_SRAM_MODULE_ENABLED": [True, False],
        "HAL_SDRAM_MODULE_ENABLED": [True, False],
        "HAL_HASH_MODULE_ENABLED": [True, False],
        "HAL_GPIO_MODULE_ENABLED": [True, False],
        "HAL_EXTI_MODULE_ENABLED": [True, False],
        "HAL_I2C_MODULE_ENABLED": [True, False],
        "HAL_SMBUS_MODULE_ENABLED": [True, False],
        "HAL_I2S_MODULE_ENABLED": [True, False],
        "HAL_IWDG_MODULE_ENABLED": [True, False],
        "HAL_LTDC_MODULE_ENABLED": [True, False],
        "HAL_DSI_MODULE_ENABLED": [True, False],
        "HAL_PWR_MODULE_ENABLED": [True, False],
        "HAL_QSPI_MODULE_ENABLED": [True, False],
        "HAL_RCC_MODULE_ENABLED": [True, False],
        "HAL_RNG_MODULE_ENABLED": [True, False],
        "HAL_RTC_MODULE_ENABLED": [True, False],
        "HAL_SAI_MODULE_ENABLED": [True, False],
        "HAL_SD_MODULE_ENABLED": [True, False],
        "HAL_SPI_MODULE_ENABLED": [True, False],
        "HAL_TIM_MODULE_ENABLED": [True, False],
        "HAL_UART_MODULE_ENABLED": [True, False],
        "HAL_USART_MODULE_ENABLED": [True, False],
        "HAL_IRDA_MODULE_ENABLED": [True, False],
        "HAL_SMARTCARD_MODULE_ENABLED": [True, False],
        "HAL_WWDG_MODULE_ENABLED": [True, False],
        "HAL_CORTEX_MODULE_ENABLED": [True, False],
        "HAL_PCD_MODULE_ENABLED": [True, False],
        "HAL_HCD_MODULE_ENABLED": [True, False],
        "HAL_FMPI2C_MODULE_ENABLED": [True, False],
        "HAL_FMPSMBUS_MODULE_ENABLED": [True, False],
        "HAL_SPDIFRX_MODULE_ENABLED": [True, False],
        "HAL_DFSDM_MODULE_ENABLED": [True, False],
        "HAL_LPTIM_MODULE_ENABLED": [True, False],
        "HAL_MMC_MODULE_ENABLED": [True, False]
    }

    default_options = {
        "HAL_ADC_MODULE_ENABLED": False,
        "HAL_CAN_MODULE_ENABLED": False,
        "HAL_CAN_LEGACY_MODULE_ENABLED": False,
        "HAL_CRC_MODULE_ENABLED": False,
        "HAL_CEC_MODULE_ENABLED": False,
        "HAL_CRYP_MODULE_ENABLED": False,
        "HAL_DAC_MODULE_ENABLED": False,
        "HAL_DCMI_MODULE_ENABLED": False,
        "HAL_DMA_MODULE_ENABLED": True,
        "HAL_DMA2D_MODULE_ENABLED": True,
        "HAL_ETH_MODULE_ENABLED": False,
        "HAL_ETH_LEGACY_MODULE_ENABLED": False,
        "HAL_FLASH_MODULE_ENABLED": True,
        "HAL_NAND_MODULE_ENABLED": False,
        "HAL_NOR_MODULE_ENABLED": False,
        "HAL_PCCARD_MODULE_ENABLED": False,
        "HAL_SRAM_MODULE_ENABLED": False,
        "HAL_SDRAM_MODULE_ENABLED": False,
        "HAL_HASH_MODULE_ENABLED": False,
        "HAL_GPIO_MODULE_ENABLED": True,
        "HAL_EXTI_MODULE_ENABLED": False,
        "HAL_I2C_MODULE_ENABLED": False,
        "HAL_SMBUS_MODULE_ENABLED": False,
        "HAL_I2S_MODULE_ENABLED": False,
        "HAL_IWDG_MODULE_ENABLED": False,
        "HAL_LTDC_MODULE_ENABLED": False,
        "HAL_DSI_MODULE_ENABLED": False,
        "HAL_PWR_MODULE_ENABLED": True,
        "HAL_QSPI_MODULE_ENABLED": False,
        "HAL_RCC_MODULE_ENABLED": True,
        "HAL_RNG_MODULE_ENABLED": False,
        "HAL_RTC_MODULE_ENABLED": True,
        "HAL_SAI_MODULE_ENABLED": False,
        "HAL_SD_MODULE_ENABLED": False,
        "HAL_SPI_MODULE_ENABLED": False,
        "HAL_TIM_MODULE_ENABLED": False,
        "HAL_UART_MODULE_ENABLED": True,
        "HAL_USART_MODULE_ENABLED": True,
        "HAL_IRDA_MODULE_ENABLED": False,
        "HAL_SMARTCARD_MODULE_ENABLED": False,
        "HAL_WWDG_MODULE_ENABLED": False,
        "HAL_CORTEX_MODULE_ENABLED": True,
        "HAL_PCD_MODULE_ENABLED": False,
        "HAL_HCD_MODULE_ENABLED": False,
        "HAL_FMPI2C_MODULE_ENABLED": False,
        "HAL_FMPSMBUS_MODULE_ENABLED": False,
        "HAL_SPDIFRX_MODULE_ENABLED": False,
        "HAL_DFSDM_MODULE_ENABLED": False,
        "HAL_LPTIM_MODULE_ENABLED": False,
        "HAL_MMC_MODULE_ENABLED": False
    }

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
        for opt in self.options.items():
            if opt[0].endswith("MODULE_ENABLED") and opt[1] == "True":
                tc.variables[opt[0]] = True
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
