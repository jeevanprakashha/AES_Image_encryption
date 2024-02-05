def extract_email_and_iv(file_stream):
    email_length = int.from_bytes(file_stream.read(2), byteorder='big')
    email = file_stream.read(email_length).decode('utf-8')
    iv = file_stream.read(16)
    return email, iv