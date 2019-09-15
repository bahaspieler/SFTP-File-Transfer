import pysftp as sftp


cnopts= sftp.CnOpts()
cnopts.hostkeys= None

def sftp_upload():
    try:
        s= sftp.Connection(host='HostAddress',port=22, username='your username', password='your password', cnopts=cnopts)

        remotepath= '/path/to/remoteserver/folder/'
        localpath='path\\to\\your\\files'
        s.put_d(localpath, remotepath)
        s.close()

    except Exception as e:
        print(str(e))
sftp_upload()

