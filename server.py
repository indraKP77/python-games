from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():
    # Create a user with permissions
    authorizer = DummyAuthorizer()
    # Create a user with username "user" and password "12345", and allow read/write access to the "ftp_root" directory
    authorizer.add_user("user", "12345", "./ftp_root", perm="elradfmw")
    # Anonymous user with read-only access
    authorizer.add_anonymous("./ftp_root", perm="elr")

    # Set up FTP handler
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define server and listen on port 2121
    server = FTPServer(("0.0.0.0", 2121), handler)

    print("Starting FTP server on port 2121...")
    server.serve_forever()

if __name__ == "__main__":
    # Ensure the ftp_root directory exists
    import os
    if not os.path.exists("./ftp_root"):
        os.makedirs("./ftp_root")
    start_ftp_server()
