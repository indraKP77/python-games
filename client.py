from ftplib import FTP

def connect_ftp_server(server, username, password):
    try:
        ftp = FTP(server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to FTP server at {server}.")
        return ftp
    except Exception as e:
        print(f"Failed to connect: {e}")
        return None

def list_files(ftp):
    try:
        print("Files on the server:")
        files = ftp.nlst()
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error listing files: {e}")

def upload_file(ftp, local_file, remote_file):
    try:
        with open(local_file, 'rb') as f:
            ftp.storbinary(f"STOR {remote_file}", f)
        print(f"File '{local_file}' uploaded successfully as '{remote_file}'.")
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_file(ftp, remote_file, local_file):
    try:
        with open(local_file, 'wb') as f:
            ftp.retrbinary(f"RETR {remote_file}", f.write)
        print(f"File '{remote_file}' downloaded successfully as '{local_file}'.")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    # Connect to the FTP server
    ftp = connect_ftp_server("localhost", "user", "12345")
    if ftp:
        list_files(ftp)

        # Example: Upload a file
        upload_file(ftp, "test_upload.txt", "uploaded_test.txt")

        # Example: Download a file
        download_file(ftp, "uploaded_test.txt", "test_download.txt")

        # Close the connection
        ftp.quit()
