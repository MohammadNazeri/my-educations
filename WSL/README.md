* wsl --install
* wsl --list
* wsl --export Ubuntu c:\Users\eznomha\mywsl\exports\[os name] > export clean instance
* wsl --import [os name] c:\Users\eznomha\mywsl\instances\[os name] c:\Users\eznomha\mywsl\exports\ubuntudocker > create new WSL instance
* wsl --unregister Ubuntu-22.04 > delete instance
* To run vistual studio with docker inside WSL
  * Vistual studio in host > install Remote Development and docker
  * docker in WSL and run 
    * sudo snap install --classic code
    * code .
  * install python3.11 and create venv
   * pip install -r requirements.txt

### WSL network problem
```sudo nano /etc/wsl.conf```
```
[boot]
systemd=true

[network]
generateResolvConf = false
```
