import hashlib
import sys

def calculate_file_hash(filename):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Open the file in binary mode and read it in chunks
    with open(filename, 'rb') as file:
        # Read the file in smaller chunks to minimize memory usage
        chunk_size = 4096
        for chunk in iter(lambda: file.read(chunk_size), b''):
            # Update the hash object with the chunk
            sha256_hash.update(chunk)

    # Get the resulting hash value
    hash_value = sha256_hash.hexdigest()

    return hash_value
file_address = sys.argv[1]
file_hash = calculate_file_hash(file_address)
print("File hash:", file_hash)
