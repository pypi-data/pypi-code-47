# Import section
import hashlib,binascii

# Functions
def md5_data(data):

    """ Function used to calculate the MD5 hash of the provided binary data """
    md5 = hashlib.md5()
    md5.update(binary_data)
    return md5.digest()


# Calculate the MD5 value for the specified string
def md5_string(source):
    """ This function is used to generate the MD5 Hash for specified source """
    m = hashlib.md5()
    m.update(source.encode())
    return m.hexdigest()

# Calculate the file's MD5
def md5_file(filename):
    """ This function is used to calculate MD5 has for specified file """
    with open(filename,"rb") as f:
        data = f.read()
        md5 = hashlib.md5()
        md5.update(data)
        hash = md5.digest()
        return binascii.hexlify(hash)
