#!/usr/bin/env python3
"""
System Uptime Script
Generated with GitHub Copilot assistance and improved for security and reliability.
"""

import subprocess
import platform
import sys
from datetime import timedelta


def get_system_uptime():
    """
    Get system uptime in a cross-platform way.
    Returns uptime in seconds or None if unable to determine.
    """
    try:
        system = platform.system().lower()
        
        if system == "linux" or system == "darwin":  # Linux or macOS
            # Use 'uptime' command for Unix-like systems
            result = subprocess.run(
                ['uptime', '-s'], 
                capture_output=True, 
                text=True, 
                check=True,
                timeout=10
            )
            
            if result.returncode == 0:
                # Parse uptime output
                uptime_output = result.stdout.strip()
                print(f"System uptime start time: {uptime_output}")
                
                # Alternative: get uptime in seconds
                result_seconds = subprocess.run(
                    ['cat', '/proc/uptime'], 
                    capture_output=True, 
                    text=True, 
                    check=True,
                    timeout=5
                )
                
                if result_seconds.returncode == 0:
                    uptime_seconds = float(result_seconds.stdout.split()[0])
                    return uptime_seconds
                    
        elif system == "windows":
            # Use systeminfo command for Windows
            result = subprocess.run(
                ['systeminfo', '/FO', 'CSV'], 
                capture_output=True, 
                text=True, 
                check=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # Parse Windows systeminfo output
                lines = result.stdout.strip().split('\n')
                for line in lines[1:]:  # Skip header
                    if 'System Boot Time' in line:
                        boot_time = line.split(',')[1].strip('"')
                        print(f"System Boot Time: {boot_time}")
                        return boot_time
                        
        else:
            print(f"Unsupported operating system: {system}")
            return None
            
    except subprocess.TimeoutExpired:
        print("Error: Command timed out")
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def format_uptime(uptime_seconds):
    """
    Format uptime seconds into human-readable format.
    """
    if uptime_seconds is None:
        return "Unable to determine uptime"
    
    try:
        # Convert seconds to timedelta for easy formatting
        uptime_delta = timedelta(seconds=int(uptime_seconds))
        
        days = uptime_delta.days
        hours, remainder = divmod(uptime_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        # Build human-readable string
        parts = []
        if days > 0:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes > 0:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if seconds > 0:
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")
        
        if parts:
            return ", ".join(parts)
        else:
            return "Less than a second"
            
    except Exception as e:
        print(f"Error formatting uptime: {e}")
        return "Error formatting uptime"


def main():
    """
    Main function to get and display system uptime.
    """
    print("System Uptime Information")
    print("=" * 25)
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print("-" * 25)
    
    # Get uptime
    uptime = get_system_uptime()
    
    if isinstance(uptime, (int, float)):
        # Format and display uptime
        formatted_uptime = format_uptime(uptime)
        print(f"System Uptime: {formatted_uptime}")
        print(f"Uptime (seconds): {uptime:.2f}")
    else:
        print("Could not retrieve system uptime information")
        
    print("-" * 25)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error in main: {e}")
        sys.exit(1)
