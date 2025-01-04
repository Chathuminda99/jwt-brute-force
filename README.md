## 🔒 JWT-Force: The Token Breaker 🔓

```
      _       _     _                 
     | |     (_)   | |           
     | |      _  __| | ___ _ __  
     | |     | |/ _` |/ _ \ '_ \ 
     | |____ | | (_| |  __/ | | |
     \_____/ |_|\__,_|\___|_| |_|

   Brute Force Your Way Through JWTs!  
```

## Overview

This script attempts to brute force the secret key used to sign a given JWT (JSON Web Token) by using a dictionary attack. It helps security researchers and penetration testers validate the strength of JWT implementations.

## Features

- 🔍 Identifies the hashing algorithm used in the JWT header.
- 🗝️ Supports dictionary-based brute force to find the secret key.
- 📊 Displays progress updates during brute-forcing.
- ⚙️ Handles invalid UTF-8 characters gracefully in the dictionary file.

## Requirements

- 🐍 Python 3.6 or later
- 📦 `PyJWT` library installed (`pip install PyJWT`)

## Installation

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/chathuminda99/jwt-brute-force.git
   cd jwt-brute-force
   ```
2. ⚙️ Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python3 crackmyjwt.py -t <JWT_TOKEN> -d <DICTIONARY_FILE>
```

### Arguments

- 🔑 `-t, --token`: The JWT token to brute force.
- 📖 `-d, --dictionary`: Path to the dictionary file containing potential secret keys.

### Example

```bash
python3 crackmyjwt.py -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... -d wordlist.txt
```

## Progress Display

📊 The script provides progress updates at 10% intervals based on the size of the dictionary, ensuring users know how far the brute force has progressed.

## Error Handling

- 🛡️ Handles invalid UTF-8 characters in dictionary files using `errors="ignore"`.
- 🚨 Detects missing or inaccessible dictionary files.
- ❌ Exits gracefully if errors occur during decoding.

## License

📜 This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

⚠️ This tool is intended for educational and security testing purposes only. Use it responsibly and only with proper authorization. Unauthorized use of this tool is illegal.

