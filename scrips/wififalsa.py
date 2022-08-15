import os 

header = """
 _____ ___    _    _____      ___   __   
|_   _/ _ \  / \  |  ___|    ( _ ) / /_  
  | || | | |/ _ \ | |_ _____ / _ \| '_ \ 
  | || |_| / ___ \|  _|_____| (_) | (_) |
  |_| \___/_/   \_\_|        \___/ \___/ 
                                         
"""
print(header)


def init():
	ap_iface = input("[?] Please enter the name of your wireless interface (for the AP): ")
    net_iface = input("[?] Please enter the name of your internet connected interface: ")
    network_manager_cfg = "[main]\nplugins=keyfile\n\n[keyfile]\nunmanaged-devices=interface-name:" + ap_iface + "\n"print("[I] Backing up NetworkManager.cfg...")
    os.system("sudo cp /etc/NetworkManager/NetworkManager.conf /etc/NetworkManager/NetworkManager.conf.backup")
    print("[I] Editing NetworkManager.cfg...")
    write_file("/etc/NetworkManager/NetworkManager.conf", network_manager_cfg )
    print("[I] Restarting NetworkManager...")
    os.system("sudo service network-manager restart")
    os.system("sudo ifconfig " + ap_iface + " up")

init()
