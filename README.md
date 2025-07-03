# System Uptime Script - GitHub Copilot Experience

## Overview
This repository contains a Python script that displays system uptime information, created as part of a GitHub Copilot learning exercise.

## Files
- `copilot_test.py` - Main system uptime script
- `README.md` - This documentation file

## GitHub Copilot Experience

### What Copilot Originally Suggested
When I asked GitHub Copilot to "Create a script to print system uptime", it initially suggested a basic Python script using:

```python
import os
import platform

def get_uptime():
    if platform.system() == "Linux":
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.read().split()[0])
    elif platform.system() == "Windows":
        uptime = os.popen('systeminfo | find "System Boot Time"').read()
    return uptime_seconds
```

### Modifications and Improvements Made

I significantly improved the original Copilot suggestion for better **security and reliability**:

#### 1. **Security Improvements**
- **Replaced `os.popen()`** with `subprocess.run()` to avoid shell injection vulnerabilities
- **Added command timeouts** to prevent hanging processes
- **Input validation** and proper error handling

#### 2. **Reliability Improvements**
- **Cross-platform compatibility** (Linux, macOS, Windows)
- **Exception handling** for all subprocess calls
- **Graceful error messages** instead of crashes
- **Function-based architecture** for better maintainability

#### 3. **Feature Enhancements**
- **Human-readable time formatting** (days, hours, minutes, seconds)
- **Detailed system information** display
- **Multiple fallback methods** for different operating systems
- **Proper exit codes** and keyboard interrupt handling

#### 4. **Code Quality**
- **Type hints and documentation** for better code clarity
- **Modular functions** for specific tasks
- **PEP 8 compliance** for Python coding standards
- **Error logging** and user-friendly messages

## How to Run the Script

### Prerequisites
- Python 3.6 or higher
- Operating System: Linux, macOS, or Windows

### Running the Script

#### On Linux/macOS:
```bash
# Make the script executable
chmod +x copilot_test.py

# Run the script
python3 copilot_test.py
# or
./copilot_test.py
```

#### On Windows:
```cmd
# Run with Python
python copilot_test.py
```

#### Using PowerShell:
```powershell
python .\copilot_test.py
```

### Expected Output
```
System Uptime Information
=========================
Operating System: Linux 5.15.0
Platform: Linux-5.15.0-72-generic-x86_64-with-glibc2.35
-------------------------
System uptime start time: 2025-07-01 09:30:45
System Uptime: 1 day, 14 hours, 25 minutes, 30 seconds
Uptime (seconds): 138330.45
-------------------------
```

## Testing

### Manual Testing Steps
1. **Basic functionality**: Run the script on different operating systems
2. **Error handling**: Test with insufficient permissions
3. **Timeout testing**: Verify commands don't hang indefinitely
4. **Cross-platform**: Test on Linux, Windows, and macOS if available

### Test Results
- ✅ **Linux**: Successfully reads `/proc/uptime` and formats output
- ✅ **Windows**: Uses `systeminfo` command with proper parsing
- ✅ **Error handling**: Gracefully handles permission and command errors
- ✅ **Security**: No shell injection vulnerabilities with `subprocess.run()`

## Why These Improvements Matter

### Security Benefits
- **No shell injection**: `subprocess.run()` with list arguments is safer than `os.popen()`
- **Timeout protection**: Prevents malicious commands from hanging the script
- **Input validation**: Reduces risk of unexpected behavior

### Reliability Benefits  
- **Cross-platform**: Works consistently across different operating systems
- **Error recovery**: Script continues functioning even if some commands fail
- **User experience**: Clear error messages instead of cryptic exceptions

### Maintainability Benefits
- **Modular design**: Easy to add new features or fix specific functions
- **Documentation**: Clear docstrings and comments for future developers
- **Standards compliance**: Follows Python best practices

## Learning Outcomes

### GitHub Copilot Strengths
- **Quick prototyping**: Generated functional code quickly
- **Basic structure**: Provided good starting point for the script
- **Platform awareness**: Suggested platform-specific approaches

### Areas for Human Improvement
- **Security considerations**: Copilot didn't initially suggest secure alternatives
- **Error handling**: Required manual addition of comprehensive exception handling
- **Code quality**: Needed restructuring for maintainability and readability
- **User experience**: Enhanced with better formatting and informative output

## Conclusion

GitHub Copilot provided an excellent starting point, but human expertise was essential for creating a **production-ready, secure, and reliable** script. The combination of AI assistance and human judgment resulted in a robust solution that's both functional and secure.

---

**Author**: [Your Name]  
**Date**: July 2, 2025  
**Course**: GitHub Copilot Learning Exercise
