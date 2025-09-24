* wsl --install
* wsl --list
* wsl --export Ubuntu c:\Users\eznomha\mywsl\exports\[os name] > export clean instance
* Download wsl version of ubuntu from website and import it
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
make the /etc/resolv.conf file immutable. This means that once the below command is executed, the file cannot be modified, deleted, or renamed until the immutable attribute is removed.

```sudo chattr +i /etc/resolv.conf```

## google chrome
```
cd /tmp $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
sudo dpkg -i google-chrome-stable_current_amd64.deb 
sudo apt install --fix-broken -y
google-chrome
```
