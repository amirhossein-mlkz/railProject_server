import platform
import subprocess
import os

from PySide6.QtCore import Signal, QObject

from Tranform.sharingConstans import StatusCodes


class pingWorker(QObject):
    result_signal = Signal(int)

    def __init__(self, ip) -> None:
        super().__init__()
        self.ip = ip
    
    def run(self,):
        res = self.__get_ping(self.ip)
        if not res:
            self.result_signal.emit(StatusCodes.pingAndConnectionStatusCodes.NOT_CONNECT)
            return
        else:

            self.result_signal.emit(StatusCodes.pingAndConnectionStatusCodes.SUCCESS)

    def __get_ping(self, ip):
        if platform.system().lower() == "windows":
            param = "-n"
        else:
            param = "-c"
        
        try:
            # اجرای دستور پینگ
            output = subprocess.run(["ping", param, "1", ip], capture_output=True, text=True)
            print(output, '\n')
            # بررسی returncode
            if 'ttl' in output.stdout.lower():
                return True
            else:
                return False

        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        







class shareMapping(QObject):

    def __init__(self, username, password, drive_letter, ) -> None:
        super().__init__()

    def map_network_drive(self):
        command = f'net use {self.drive_letter} {self.network_path} /user:{self.username} {self.password}'
        os.system(command)

    def disconnect_network_drive(self):
        os.system(f'net use {self.drive_letter} /delete')

    def  is_drive_mapped(self):
        try:
            output = subprocess.check_output(f'net use {self.drive_letter}', shell=True, stderr=subprocess.STDOUT).decode()
            return self.network_path in output
        except subprocess.CalledProcessError:
            return False
        
    
    def get_mapped_drives(self,):
        try:
            output = subprocess.check_output('net use', shell=True).decode() 
            
            lines = output.splitlines()
            all_drives = []

            for line in lines:
                if (   line.lower().startswith("ok") 
                    or line.lower().startswith("unavailable") 
                    or line.lower().startswith("disconnected")
                    ):
                    parts = line.split()
                    if len(parts) >= 3:
                        drive_letter = parts[1]
                        network_path = parts[2]
                        available = False
                        connect = False
                        if parts[0].lower() == 'ok':
                            available = True
                            connect = True
                        elif parts[0].lower() == 'unavailable':
                            available = False
                            connect = False

                        elif parts[0].lower() == 'disconnected':
                            available = True
                            connect = False

                        all_drives.append({
                            "drive_letter": drive_letter,
                            "network_path": network_path,
                            "available": available,
                            'connect': connect,
                        })


        except subprocess.CalledProcessError as e:
            print("خطا در اجرای دستور 'net use':", e)
        
        finally:
            return all_drives
    
    def check_drived_is_mapped(self, ip:str):
        drives = self.get_mapped_drives()
        for drive in drives:
            if ip in drive['network_path']:
                return drive
        return None
    
    def map_network(self, ip, share_path, username, password, drive_letter='Z:'):
        share_path = f'\\\\{ip}\\{share_path}'

        if username and password:
            command = f'net use {drive_letter} {share_path} /user:{username} {password}'
        else:
            command = f'net use {drive_letter} {share_path}'

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if 'completed successfully' in result.stdout:
                return True
            
            if 'error 85' in result.stderr:
                print('Error: map exist drive')
                return False
            return False
        
        except Exception as e:
            print(f"error: {e}")
            return False