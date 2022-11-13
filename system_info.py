# *****************************************************************************
# Name: Jason D. F. D'Oyley
# Date: November 12, 2022
# Assignment: GP 3 - Task 3 System Information
# Task Description: Use Python to get and display system information.
# *****************************************************************************
import platform

print("Student ID#: JASDOY5736")
print(f"Operating system: {platform.platform()}")
print(f"Type: {platform.machine()}")
print(f"Computer Name: {platform.node()}")
print(f"Processor: {platform.processor()}")
print(f"Edition: {platform.win32_edition()}")