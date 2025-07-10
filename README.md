
#  SSHIFTER

A Python based SSH brute force tool designed to bypass SSH authentication. It uses the `paramiko` library to connect to an SSH server and tries passwords from a provided wordlist.
<img src="https://socialify.git.ci/PavinDas/sshifter/image?description=1&font=KoHo&language=1&name=1&owner=1&pattern=Solid&theme=Dark" alt="Socket" width="640" height="320" />

  

**Note**: This tool is for **educational purposes only**. Unauthorized use of this tool to attack systems without explicit permission is illegal and unethical. Always obtain proper authorization before testing any system.

  

##  Features

- Attempts SSH login with a given username and a list of passwords.

- Supports custom IP address, username, and password file input.

- Displays real time feedback on password attempts.

- Includes a timeout for SSH connections to prevent hanging.

  

##  Requirements

- Python 3.x

- Required Python libraries:

-  `paramiko`

-  `colorama`

  

##  Installation

1. Clone the repository:

```bash

git clone https://github.com/PavinDas/sshifter

```

2. Navigate to the project directory:

```bash

cd sshifter

```

3. Install the required dependencies:

```bash

pip install -r requirements.txt

```

  

##  Usage

1. Run the script:

```bash

python sshifter

```

2. Enter the target IP address, username, and path to the password wordlist when prompted.

3. The tool will attempt to connect to the SSH server with each password in the wordlist.

  

###  Example

```bash

Enter  ip  address:  192.168.1.100

Enter  username:  admin

Enter  password  path:  passwords.txt

```

  

###  Sample Password File

[Click here ](https://github.com/PavinDas/WiFried/releases/download/Wordlist/wordlist.txt) to download the password list

  

##  Disclaimer

This tool is intended for **educational and ethical security testing purposes only**. The creator is not responsible for any misuse or illegal activities conducted with this tool. Always ensure you have explicit permission to test the target system.

  

##  Author

-  **Creator**: Pavin Das

-  **GitHub**: [PavinDas](https://github.com/PavinDas)

-  **Instagram**: [pavin__das](https://www.instagram.com/pavin__das)
