cmake_minimum_required(VERSION 3.15)
project(HAL C)

set(BOARD "STM32F411CE" CACHE STRING "Select a board to build CMSIS for")
set(SUPPORTED_BOARDS
    "STM32F411CE"
)

message(CHECK_START "Checking for board support")
if (${BOARD} IN_LIST SUPPORTED_BOARDS)
    message(CHECK_PASS "done")
else ()
    message(FATAL_ERROR "unknown board: ${BOARD}")
endif ()

if (${BOARD} STREQUAL "STM32F411CE")
    set(BOARD_TARGET "STM32F411xE")
endif ()

option(HAL_ADC_MODULE_ENABLED "Enable ADC module" OFF)
option(HAL_CAN_MODULE_ENABLED "Enable CAN module" OFF)
option(HAL_CAN_LEGACY_MODULE_ENABLED "Enable CAN_LEGACY module" OFF)
option(HAL_CRC_MODULE_ENABLED "Enable CRC module" OFF)
option(HAL_CEC_MODULE_ENABLED "Enable CEC module" OFF)
option(HAL_CRYP_MODULE_ENABLED "Enable CRYP module" OFF)
option(HAL_DAC_MODULE_ENABLED "Enable DAC module" OFF)
option(HAL_DCMI_MODULE_ENABLED "Enable DCMI module" OFF)
option(HAL_DMA_MODULE_ENABLED "Enable DMA module" ON)
option(HAL_DMA2D_MODULE_ENABLED "Enable DMA2D module" ON)
option(HAL_ETH_MODULE_ENABLED "Enable ETH module" OFF)
option(HAL_ETH_LEGACY_MODULE_ENABLED "Enable ETH_LEGACY module" OFF)
option(HAL_FLASH_MODULE_ENABLED "Enable FLASH module" ON)
option(HAL_NAND_MODULE_ENABLED "Enable NAND module" OFF)
option(HAL_NOR_MODULE_ENABLED "Enable NOR module" OFF)
option(HAL_PCCARD_MODULE_ENABLED "Enable PCCARD module" OFF)
option(HAL_SRAM_MODULE_ENABLED "Enable SRAM module" OFF)
option(HAL_SDRAM_MODULE_ENABLED "Enable SDRAM module" OFF)
option(HAL_HASH_MODULE_ENABLED "Enable HASH module" OFF)
option(HAL_GPIO_MODULE_ENABLED "Enable GPIO module" ON)
option(HAL_EXTI_MODULE_ENABLED "Enable EXTI module" OFF)
option(HAL_I2C_MODULE_ENABLED "Enable I2C module" OFF)
option(HAL_SMBUS_MODULE_ENABLED "Enable SMBUS module" OFF)
option(HAL_I2S_MODULE_ENABLED "Enable I2S module" OFF)
option(HAL_IWDG_MODULE_ENABLED "Enable IWDG module" OFF)
option(HAL_LTDC_MODULE_ENABLED "Enable LTDC module" OFF)
option(HAL_DSI_MODULE_ENABLED "Enable DSI module" OFF)
option(HAL_PWR_MODULE_ENABLED "Enable PWR module" ON)
option(HAL_QSPI_MODULE_ENABLED "Enable QSPI module" OFF)
option(HAL_RCC_MODULE_ENABLED "Enable RCC module" ON)
option(HAL_RNG_MODULE_ENABLED "Enable RNG module" OFF)
option(HAL_RTC_MODULE_ENABLED "Enable RTC module" ON)
option(HAL_SAI_MODULE_ENABLED "Enable SAI module" OFF)
option(HAL_SD_MODULE_ENABLED "Enable SD module" OFF)
option(HAL_SPI_MODULE_ENABLED "Enable SPI module" OFF)
option(HAL_TIM_MODULE_ENABLED "Enable TIM module" OFF)
option(HAL_UART_MODULE_ENABLED "Enable UART module" OFF)
option(HAL_USART_MODULE_ENABLED "Enable USART module" OFF)
option(HAL_IRDA_MODULE_ENABLED "Enable IRDA module" OFF)
option(HAL_SMARTCARD_MODULE_ENABLED "Enable SMARTCARD module" OFF)
option(HAL_WWDG_MODULE_ENABLED "Enable WWDG module" OFF)
option(HAL_CORTEX_MODULE_ENABLED "Enable CORTEX module" ON)
option(HAL_PCD_MODULE_ENABLED "Enable PCD module" OFF)
option(HAL_HCD_MODULE_ENABLED "Enable HCD module" OFF)
option(HAL_FMPI2C_MODULE_ENABLED "Enable FMPI2C module" OFF)
option(HAL_FMPSMBUS_MODULE_ENABLED "Enable FMPSMBUS module" OFF)
option(HAL_SPDIFRX_MODULE_ENABLED "Enable SPDIFRX module" OFF)
option(HAL_DFSDM_MODULE_ENABLED "Enable DFSDM module" OFF)
option(HAL_LPTIM_MODULE_ENABLED "Enable LPTIM module" OFF)
option(HAL_MMC_MODULE_ENABLED "Enable MMC module" OFF)

find_package(cmsis REQUIRED)

set(HAL_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/Inc")
set(HAL_SOURCE_DIR "${PROJECT_SOURCE_DIR}/Src")

add_library(hal STATIC)

configure_file(
    "${HAL_INCLUDE_DIR}/stm32f4xx_hal_conf.h.in"
    "${HAL_INCLUDE_DIR}/stm32f4xx_hal_conf.h"
    @ONLY
)
target_compile_definitions(hal PRIVATE "${BOARD_TARGET}")
target_include_directories(hal PRIVATE "${cmsis_INCLUDE_DIRS}")
target_sources(hal PUBLIC
    FILE_SET HEADERS BASE_DIRS "${HAL_INCLUDE_DIR}"
    FILES
        "${HAL_INCLUDE_DIR}/Legacy/stm32f4xx_hal_can_legacy.h"
        "${HAL_INCLUDE_DIR}/Legacy/stm32f4xx_hal_eth_legacy.h"
        "${HAL_INCLUDE_DIR}/Legacy/stm32_hal_legacy.h"
        "${HAL_INCLUDE_DIR}/stm32_assert_template.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_adc_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_adc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_can.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_cec.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_conf.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_cortex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_crc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_cryp_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_cryp.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dac_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dac.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dcmi_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dcmi.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_def.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dfsdm.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dma2d.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dma_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dma.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_dsi.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_eth.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_exti.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_flash_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_flash.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_flash_ramfunc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_fmpi2c_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_fmpi2c.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_fmpsmbus_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_fmpsmbus.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_gpio_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_gpio.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_hash_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_hash.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_hcd.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_i2c_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_i2c.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_i2s_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_i2s.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_irda.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_iwdg.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_lptim.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_ltdc_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_ltdc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_mmc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_nand.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_nor.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_pccard.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_pcd_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_pcd.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_pwr_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_pwr.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_qspi.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_rcc_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_rcc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_rng.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_rtc_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_rtc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_sai_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_sai.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_sd.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_sdram.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_smartcard.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_smbus.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_spdifrx.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_spi.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_sram.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_tim_ex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_tim.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_uart.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_usart.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_hal_wwdg.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_adc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_bus.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_cortex.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_crc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_dac.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_dma2d.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_dma.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_exti.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_fmc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_fmpi2c.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_fsmc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_gpio.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_i2c.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_iwdg.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_lptim.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_pwr.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_rcc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_rng.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_rtc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_sdmmc.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_spi.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_system.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_tim.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_usart.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_usb.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_utils.h"
        "${HAL_INCLUDE_DIR}/stm32f4xx_ll_wwdg.h"
)
target_sources(hal PRIVATE
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_adc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_adc_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_can.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_cec.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_cortex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_crc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_cryp.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_cryp_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dac.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dac_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dcmi.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dcmi_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dfsdm.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dma2d.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dma.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dma_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_dsi.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_eth.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_exti.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_flash.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_flash_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_flash_ramfunc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_fmpi2c.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_fmpi2c_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_fmpsmbus.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_fmpsmbus_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_gpio.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_hash.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_hash_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_hcd.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_i2c.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_i2c_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_i2s.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_i2s_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_irda.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_iwdg.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_lptim.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_ltdc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_ltdc_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_mmc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_msp_template.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_nand.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_nor.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_pccard.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_pcd.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_pcd_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_pwr.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_pwr_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_qspi.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_rcc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_rcc_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_rng.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_rtc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_rtc_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_sai.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_sai_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_sd.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_sdram.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_smartcard.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_smbus.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_spdifrx.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_spi.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_sram.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_tim.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_timebase_rtc_alarm_template.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_timebase_rtc_wakeup_template.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_tim_ex.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_uart.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_usart.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_hal_wwdg.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_adc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_crc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_dac.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_dma2d.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_dma.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_exti.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_fmc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_fmpi2c.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_fsmc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_gpio.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_i2c.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_lptim.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_pwr.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_rcc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_rng.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_rtc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_sdmmc.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_spi.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_tim.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_usart.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_usb.c"
    "${HAL_SOURCE_DIR}/stm32f4xx_ll_utils.c"
)

install(TARGETS hal FILE_SET HEADERS )
