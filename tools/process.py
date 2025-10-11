import os

# Get parent process of python
pid = os.getppid()

# Need to check at startup
print(f"Parent Process ID: {pid}")
