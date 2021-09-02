import platform
import os


def select_webdriver_by_os_and_browser(driverName):

    osType = platform.system()
    listOfBrowser = ["chrome_beta", "chrome_canary", "chrome_ga", "geko_ga", "msedge_ga"]

    if osType == "Windows":
        winDirName = os.path.abspath("../../drivers/webdrivers_for_win")
        sepDriverName = driverName.replace("driver", "")
        if sepDriverName in listOfBrowser:
            for i in listOfBrowser:
                if i == sepDriverName:
                    absDriverPath = os.path.abspath(winDirName + f"/{driverName}/{driverName.split('_')[0]}.exe")
    if osType == "Darwin" or osType == "Linux":
        macDirName = os.path.abspath("../../drivers/webdrivers_for_mac")
        sepDriverName = driverName.replace("driver", "")
        if sepDriverName in listOfBrowser:
            for i in listOfBrowser:
                if i == sepDriverName:
                    absDriverPath = os.path.abspath(macDirName + f"/{driverName}/{driverName.split('_')[0]}")

    return absDriverPath


