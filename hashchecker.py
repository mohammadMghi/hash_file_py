import hashlib

import sys

def check_file_hash(file_path, provided_hash, hash_algorithm='sha256'):
    # Create a hash object based on the specified algorithm
    hash_object = hashlib.new(hash_algorithm)

    # Read the file in binary mode and calculate the hash
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_object.update(chunk)

    # Get the hexadecimal representation of the calculated hash value
    calculated_hash = hash_object.hexdigest()

    # Compare the calculated hash with the provided hash
    if calculated_hash == provided_hash:
        return True
    else:
        return False
 
path = sys.argv[1]
file_hash = sys.argv[2]
is_match = check_file_hash(path, file_hash)
if is_match:
    print("The provided hash matches the calculated hash.")
else:
    print("The provided hash does not match the calculated hash.")
