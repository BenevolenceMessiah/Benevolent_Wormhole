# 🌀 Benevolent Wormhole
A secure, encrypted terminal-based messaging and file transfer system.

## 📖 Table of Contents
- Introduction
- Features
- Project Structure
- Installation
- Usage
- Commands
- Troubleshooting
- Uninstallation
- Contributing
- License

## 📝 Introduction
Benevolent Wormhole is a lightweight, cross-platform program that allows users to securely send messages and transfer files up to 50.25GB between two users anywhere in the world via a terminal interface. It ensures encryption, no logging, and real-time communication.

## ✨ Features
- Secure and Encrypted: All communications are encrypted for security.
- Cross-Platform: Runs on Windows, macOS, and Linux.
- No Logs: Respects user privacy by not keeping logs.
- Large File Transfer: Supports file transfers up to 50.25GB.
- Offline Messaging: Stores messages to send when the recipient is online.
- Runs at Boot: Optionally configured to start automatically.
- NAT Traversal Support: Connect seamlessly even behind NATs.
- Optional Emoji Aesthetics: Includes a Swirl emoji (🌀) in the executable name for a wormhole representation.

## 📁 Project Structure
Here's an overview of the project's file structure:

```bash
Benevolent_Wormhole/
├── .venv/                  # Virtual environment directory
├── Chats/                  # Contains chat folders for each user
│   ├── .gitignore          # Ignores chat folders in Git
│   └── dummy.txt           # Dummy file to ensure directory exists
├── Modules/                # Contains all Python modules
│   ├── __init__.py         # Indicates Modules is a package
│   ├── connection.py       # Handles network connections
│   ├── encryption.py       # Handles encryption/decryption
│   ├── file_transfer.py    # Manages file transfers
│   ├── main.py             # Main program file
│   ├── messaging.py        # Handles messaging functionality
│   ├── nat_traversal.py    # Handles NAT traversal
│   └── utils.py            # Utility functions
├── requirements.txt        # Python dependencies without comments
├── requirements_documented.txt  # Python dependencies with comments
├── install.sh              # Installation script for Unix/Linux/macOS
├── install.bat             # Installation script for Windows
├── start.sh                # Start script for Unix/Linux/macOS
├── start.bat               # Start script for Windows
├── stop.sh                 # Stop script for Unix/Linux/macOS
├── stop.bat                # Stop script for Windows
├── BW                      # Executable script for Unix/Linux/macOS (no extension)
├── BW.bat                  # Executable script for Windows
├── .gitignore              # Git ignore file
└── README.md               # Project documentation
````

## 🛠️ Installation
### Prerequisites
- Python 3.6+
- Git

### Clone the Repository
```bash
git clone https://github.com/BenvolenceMessiah/Benevolent_Wormhole.git
cd Benevolent_Wormhole
```

### Installation on Unix/Linux/macOS
```sh
./install.sh
```

### Installation on Windows
```bat
install.bat
``` 

### Installation Notes
- File Naming with Emojis:

During installation, the script attempts to rename the executable script to include a Swirl emoji (🌀) to represent the wormhole.
If your system does not support emojis in file names, the script will automatically use the standard file name (BW or BW.bat).

- Usage:

Regardless of the underlying file name, you can start the program using the BW command in your terminal or command prompt.

## 🌀 Usage
After installation, you can start the program by typing BW in any terminal.

```bash
BW <username> <key>
```

`username`: The recipient's username.
`key`: Connection key (IP address or access token).

### Example
```bash
BW alice 192.168.1.10
```
This will attempt to connect to user alice at IP address 192.168.1.10.

## 📋 Commands
### Start the Program
Unix/Linux/macOS:

```bash
./start.sh
Windows:

```bat
start.bat
```

### Stop the Program

- Unix/Linux/macOS:

```bash
./stop.sh
```

- Windows:

```bat
stop.bat
```

### Help
```bash
BW -h
```

## 📤 Sending Messages and Files
- Sending Messages: Simply type your message and press Enter.
- Sending Files: Type the full path to the file and press Enter. The program will handle the file transfer.

### Offline Messaging
If the recipient is offline, you'll be prompted to store the message:

```bash
Do you want to send a message anyway? (y/n):
Yes: Your message will be stored and sent when the recipient is online.
No: The message will not be sent or stored.
```

## 🛠️ Troubleshooting
### Emoji File Name Issues
Problem: If your system does not support emojis in file names, the installation script may fail to rename the executable to include the Swirl emoji.
Solution: The installation script is designed to handle this scenario. It will automatically fall back to using the standard file name (BW or BW.bat), and you can continue to use the program without any issues.

### Execution Errors
Problem: Encountering errors when running `BW` command.
Solution:
- Ensure that the installation script completed successfully.
- Verify that the alias (Unix) or PATH addition (Windows) is correctly set.
- For Unix/Linux/macOS, try sourcing your shell configuration file:

```bash
source ~/.bashrc  # or ~/.zshrc if using Zsh
```

### Port Issues
Problem: Unable to establish a connection due to port blocking.

Solution:

- Ensure that port 65432 is open on your firewall and router.
- The program uses NAT traversal techniques, but manual port forwarding may be necessary in some cases.

### Dependencies Not Installed
Problem: ModuleNotFoundError when running the program.

Solution:

Ensure that all dependencies are installed by running:

```bash
pip install -r requirements.txt
```

## 🧹 Uninstallation
To uninstall Benevolent Wormhole:

- Delete the `Benevolent_Wormhole` directory.

- Remove startup entries:
    - Unix/Linux/macOS: Remove the crontab entry.

```bash
crontab -e
```

    - Delete the line containing `start.sh.`


- Windows: Delete the scheduled task.

```bat
schtasks /Delete /TN "Benevolent_Wormhole" /F
```
    - Remove the BW alias or PATH addition:

Unix/Linux/macOS:

1. Edit your shell configuration file (`~/.bashrc`, `~/.zshrc`, or `~/.profile`) and remove the line containing the `BW` alias.

2. Reload the shell configuration:

```bash
source ~/.bashrc  # or ~/.zshrc
```

- Windows:
1. Remove the directory from the system PATH.

## 🤝 Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

### 📄 License
This project is licensed under the MIT License.

### 💡 Notes
Ensure that both users have the program installed and are connected to the internet.
For security, always verify the recipient's IP address or access token before initiating a connection.
No Docker Usage: This project does not use Docker or containerization technologies. Installation and execution are handled via the provided scripts and Python virtual environments.

### 📧 Support
For any questions or issues, please open an issue on the GitHub repository.

### 🌟 Additional Acknowledgments
Cryptography for encryption functionalities.
TQDM for progress bars during file transfers.
miniupnpc for NAT traversal support.
Requests for HTTP requests handling.
psutil for system monitoring.
The open-source community for continuous support.

🔗 Links
GitHub Repository: Benevolent Wormhole
Documentation: Read the Docs
Emojis Legend
🌀: High-level overviews and important sections.
📖: Table of contents or navigation aids.
📝: Introductions or summaries.
✨: Highlighting features.
📁: File structures and project layouts.
🛠️: Installation and setup instructions.
📋: Commands and usage.
📤: Sending or uploading actions.
📥: Receiving or downloading actions.
🧹: Cleanup or uninstallation instructions.
🤝: Collaboration and contributing.
📄: Legal or license information.
💡: Additional notes or tips.
📧: Contact or support information.
🌟: Acknowledgments or credits.
😊: Friendly sign-offs or messages.

### Annotations for Each File:
- `.venv/`: The virtual environment directory containing all Python dependencies.
- `Chats/`: Directory where chat histories and file transfers are stored per user.
- `Chats/.gitignore`: Prevents chat data from being tracked by Git.
- `Chats/dummy.txt`: Ensures the Chats directory exists in the repository.
- `Modules/`: Contains all the Python modules necessary for the program.
- `Modules/__init__.py`: Indicates that Modules is a Python package.
- `Modules/connection.py`: Handles establishing and accepting network connections.
- `Modules/encryption.py`: Manages encryption and decryption of messages.
- `Modules/file_transfer.py`: Handles sending and receiving files with progress bars.
- `Modules/main.py`: The main program that orchestrates the application's functionality.
- `Modules/messaging.py`: Manages sending and receiving of messages.
- `Modules/nat_traversal.py`: Handles NAT traversal for peer-to-peer connections.
- `Modules/utils.py`: Contains utility functions like checking if a user is online.
- `requirements.txt`: Lists all Python dependencies without comments.
- `requirements_documented.txt`: Provides explanations for each Python dependency.
- `install.sh` / `install.bat`: Scripts to install the program on Unix/Linux/macOS and Windows.
- `start.sh` / `start.bat`: Scripts to start the program.
- `stop.sh` / `stop.bat`: Scripts to stop the program.
- `BW`: Executable script for Unix/Linux/macOS (without extension).
- `BW.bat`: Executable script for Windows.
- `.gitignore`: Specifies files and directories that Git should ignore.
- `README.md`: Provides detailed documentation and instructions for the project.

## 📦 Dependencies
The following Python packages are required:

- `cryptography==3.4.7`: For encryption and decryption of messages and files.
- `pyyaml==5.4.1`: For handling YAML files (offline messages storage).
- `tqdm==4.60.0`: For displaying progress bars during file transfers.
- `miniupnpc==2.1`: For NAT traversal to establish peer-to-peer connections.
- `requests==2.25.1`: For making HTTP requests (used in NAT traversal and external IP checks).
- `psutil==5.8.0`: For advanced process and system monitoring (used in stop scripts).

Note: Modules like socket, threading, and argparse are part of Python's standard library and do not typically need to be installed via pip.

## 🔒 Security Considerations
- Encryption: All communications are encrypted using symmetric encryption provided by the cryptography library.
- SSL/TLS: Optionally, SSL/TLS can be used for socket connections to enhance security.
- No Logging: The program does not write any logs to disk, ensuring user privacy.
- Port Usage: The default port 65432 is used for connections. Ensure this port is not blocked by your firewall.

## 💡 Additional Notes

####System Compatibility:

- The program is designed to work on Unix/Linux/macOS and Windows systems.
- Emoji file names may not be supported on all filesystems, particularly on Windows.

- Dependencies Installation (preliminary tests are postive so far!):

- All dependencies are installed automatically during the installation process via the install.sh or install.bat scripts.

- Installation and execution are handled via the provided scripts and Python virtual environments.

### 😊 Thank You for Using Benevolent Wormhole!
I hope this program enhances your secure communication needs. Feel free to contribute or reach out with feedback.

#### 🌐 Disclaimer
This program is provided "as is" without any warranties. Use it responsibly and ensure compliance with local laws and regulations.

