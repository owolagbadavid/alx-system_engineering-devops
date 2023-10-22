cmd


* Connect to the sandbox environment using SFTP with the given hostname username, and password.
* Navigate to the target directory on the sandbox environment.
* Upload the screenshots from your local machine using the SFTP put command. The syntax of the put command is:
```put local_file [remote_file]```

where ```local_file``` is the name or path of the file on your local machine and remote_file is the name or path of the file on the sandbox environment. If you omit ```remote_file```, the file will be uploaded with the same name as ```local_file```.