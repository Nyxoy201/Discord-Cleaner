import os
from colorama import Fore
import time
import psutil
import subprocess


blue = Fore.BLUE
white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

normal_content = "module.exports = require('./core.asar');"

def kill_discord():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] and 'discord' in proc.info['name'].lower():
            proc.kill()

def restart_discord(latest_app_path, version):
    discord_exe = {
        "Discord": os.path.join(latest_app_path, "Discord.exe"),
        "DiscordCanary": os.path.join(latest_app_path, "DiscordCanary.exe"),
        "DiscordPTB": os.path.join(latest_app_path, "DiscordPTB.exe")
    }

    if version in discord_exe and os.path.exists(discord_exe[version]):
        exe_path = discord_exe[version]
        subprocess.Popen(
            [exe_path],
            creationflags=subprocess.CREATE_NO_WINDOW,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

def check_injection(content):
    return content != normal_content


def check_clean_discord():
    main = os.path.basename(os.path.expanduser("~"))
    
    discord_paths = {
        "Discord": f"C:\\Users\\{main}\\AppData\\Local\\Discord\\",
        "DiscordCanary": f"C:\\Users\\{main}\\AppData\\Local\\DiscordCanary\\",
        "DiscordPTB": f"C:\\Users\\{main}\\AppData\\Local\\DiscordPTB\\"
    }

    for version, path in discord_paths.items():
        if os.path.exists(path):
            print(f"[{green}FOUND{white}] Path found for {blue + version}.{white}")
            print(f"[{green}STARTING{white}] Starting Checking for Injections...\n")
            time.sleep(1)
            
            app_folders = [d for d in os.listdir(path) if d.startswith("app-")]

            if app_folders:
                latest_app = max(app_folders, key=lambda x: x.split("-")[1])
                latest_app_path = os.path.join(path, latest_app)
                modules_path = os.path.join(latest_app_path, "modules")
                
                if os.path.exists(modules_path):
                    core_folders = [d for d in os.listdir(modules_path) if d.startswith("discord_desktop_core")]

                    if core_folders:
                        latest_core_folder = max(core_folders)
                        index_js_path = os.path.join(modules_path, latest_core_folder, "discord_desktop_core", "index.js")
                        print(f"[{green}INDEX PATH{white}] {index_js_path}\n")
                        print(f"[{green}CHECKING{white}] Checking If Injected...")
                        time.sleep(1)
                        
                        with open(index_js_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                        
                        if check_injection(content):
                            print(f"[{red}FOUND INJECTION{white}] Possible Injection Found.\n")
                            dump_choice = input(f"[{blue}SAVE{white}] Dump the file ? (yes or 'Enter' to skip): ").strip().lower()
                            
                            if dump_choice == "yes":
                                dump_filename = input(f"[{blue}FILE{white}] Enter file name: ").strip()
                                dump_filename = f"{dump_filename}.js"
                                with open(dump_filename, 'w', encoding='utf-8') as dump_file:
                                    dump_file.write(content)
                                print(f"[{green}DUMPED{white}] File dumped successfully as {dump_filename} in the current directory.\n")
                            
                            print(f"[{green}CLEANING{white}] Cleaning The File, Please Wait...")
                            time.sleep(2)
                            with open(index_js_path, 'w', encoding='utf-8') as file:
                                file.write(normal_content)
                            print(f"[{green}SAFE{white}] Possible Injection Successfully Deleted. \n")
                            print(f"[{green}RESTART{white}] Restarting {version} to apply changes...")
                            print("""
------------------------------------------------------------------------
""")

                            kill_discord()
                            restart_discord(latest_app_path, version)
                        else:
                            print(f"[{green}SAFE{white}] No Injection Detected.")
                            print("""
------------------------------------------------------------------------
""")
                    else:
                        print(f"[{red}ERROR{white}] Core Folder not found in {version}.")
                        print("""
------------------------------------------------------------------------
""")
                else:
                    print(f"[{red}ERROR{white}] Modules Folder not found in {version}.")
                    print("""
------------------------------------------------------------------------
""")
            else:
                print(f"[{red}ERROR{white}] App Folder not found in {version}.")
                print("""
------------------------------------------------------------------------
""")



def check_injection_discord():
    main = os.path.basename(os.path.expanduser("~"))
    
    discord_paths = {
        "Discord": f"C:\\Users\\{main}\\AppData\\Local\\Discord\\",
        "DiscordCanary": f"C:\\Users\\{main}\\AppData\\Local\\DiscordCanary\\",
        "DiscordPTB": f"C:\\Users\\{main}\\AppData\\Local\\DiscordPTB\\"
    }

    for version, path in discord_paths.items():
        if os.path.exists(path):
            print(f"[{green}FOUND{white}] Path found for {blue + version}.{white}")
            print(f"[{green}STARTING{white}] Starting Checking for Injections...\n")
            time.sleep(1)
            
            app_folders = [d for d in os.listdir(path) if d.startswith("app-")]

            if app_folders:
                latest_app = max(app_folders, key=lambda x: x.split("-")[1])
                latest_app_path = os.path.join(path, latest_app)
                modules_path = os.path.join(latest_app_path, "modules")
                
                if os.path.exists(modules_path):
                    core_folders = [d for d in os.listdir(modules_path) if d.startswith("discord_desktop_core")]

                    if core_folders:
                        latest_core_folder = max(core_folders)
                        index_js_path = os.path.join(modules_path, latest_core_folder, "discord_desktop_core", "index.js")
                        print(f"[{green}INDEX PATH{white}] {index_js_path}\n")
                        print(f"[{green}CHECKING{white}] Checking If Injected...")
                        time.sleep(1)
                        
                        with open(index_js_path, 'r', encoding='utf-8') as file:
                            content = file.read()
                        
                        if check_injection(content): 
                            print(f"[{red}FOUND INJECTION{white}] Possible Injection Found.\n")
                            dump_choice = input(f"[{blue}SAVE{white}] Dump the file ? (yes or 'Enter' to skip): ").strip().lower()
                            
                            if dump_choice == "yes":
                                dump_filename = input(f"[{blue}FILE{white}] Enter file name: ").strip()
                                dump_filename = f"{dump_filename}.js"
                                with open(dump_filename, 'w', encoding='utf-8') as dump_file:
                                    dump_file.write(content)
                                print(f"[{green}DUMPED{white}] File dumped successfully as {dump_filename} in the current directory.\n")
                        else:
                            print(f"[{green}SAFE{white}] No Injection Detected.")
                            print("""
------------------------------------------------------------------------
""")
                    else:
                        print(f"[{red}ERROR{white}] Core Folder not found in {version}.")
                        print("""
------------------------------------------------------------------------
""")
                else:
                    print(f"[{red}ERROR{white}] Modules Folder not found in {version}.")
                    print("""
------------------------------------------------------------------------
""")
            else:
                print(f"[{red}ERROR{white}] App Folder not found in {version}.")
                print("""
------------------------------------------------------------------------
""")


def clean_discord_version(version):
    main = os.path.basename(os.path.expanduser("~"))
    
    discord_paths = {
        "1": ("Discord", f"C:\\Users\\{main}\\AppData\\Local\\Discord\\"),
        "2": ("DiscordCanary", f"C:\\Users\\{main}\\AppData\\Local\\DiscordCanary\\"),
        "3": ("DiscordPTB", f"C:\\Users\\{main}\\AppData\\Local\\DiscordPTB\\")
    }
    
    if version in discord_paths:
        version_name, path = discord_paths[version]
        
        if os.path.exists(path):
            print(f"[{green}FOUND{white}] Path found for {blue + version_name}.{white}")
            print(f"[{green}STARTING{white}] Cleaning Process for {version_name}...\n")
            time.sleep(1)
            
            app_folders = [d for d in os.listdir(path) if d.startswith("app-")]

            if app_folders:
                latest_app = max(app_folders, key=lambda x: x.split("-")[1])
                latest_app_path = os.path.join(path, latest_app)
                modules_path = os.path.join(latest_app_path, "modules")
                
                if os.path.exists(modules_path):
                    core_folders = [d for d in os.listdir(modules_path) if d.startswith("discord_desktop_core")]

                    if core_folders:
                        latest_core_folder = max(core_folders)
                        index_js_path = os.path.join(modules_path, latest_core_folder, "discord_desktop_core", "index.js")
                        print(f"[{green}INDEX PATH{white}] {index_js_path}\n")
                        
                        print(f"[{green}CLEANING{white}] Cleaning The File, Please Wait...")
                        time.sleep(2)
                        normal_content = "module.exports = require('./core.asar');"
                        with open(index_js_path, 'w', encoding='utf-8') as file:
                            file.write(normal_content)
                        print(f"[{green}SAFE{white}] File cleaned successfully.\n")
                        
                        print(f"[{green}RESTART{white}] Restarting {version_name} to apply changes...")
                        print("""
------------------------------------------------------------------------
""")
                        
                        kill_discord()
                        restart_discord(latest_app_path, version_name)
                    else:
                        print(f"[{red}ERROR{white}] Core Folder not found in {version_name}.")
                        print("""
------------------------------------------------------------------------
""")
                else:
                    print(f"[{red}ERROR{white}] Modules Folder not found in {version_name}.")
                    print("""
------------------------------------------------------------------------
""")
            else:
                print(f"[{red}ERROR{white}] App Folder not found in {version_name}.")
                print("""
------------------------------------------------------------------------
""")
        else:
            print(f"[{red}ERROR{white}] Path not found for {version_name}.")
            print("""
------------------------------------------------------------------------
""")
            
help = f"""                     [{blue}HELP MENU{white}] 

[{blue}DEVELOPER{white}] Nyxoy
[{blue}GITHUB{white}] https://github.com/Nyxoy

[{blue}CHECK INJECTIONS{white}] This script will inspect the discord index to analyze if any possible malicious code has been injected into it.
[{blue}CLEAN INJECTIONS{white}] This script will clean the discord index to remove any possible malicious code injected into it.

[{red}WARNING{white}] If Stealed, remember to use this script to remove possible discord injections, check if there is a subprocess     
"""