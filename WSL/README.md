wsl --install
wsl --list
wsl --export Ubuntu-22.04 c:\mywsl\exports\wsl-clean-instance-ubuntu2204 > export clean instance
wsl --import project01 c:\mywsl\instances\project01 c:\mywsl\exports\wsl-clean-instance-ubuntu2204 > create new WSL instance
wsl --unregister Ubuntu-22.04 > delete instance

