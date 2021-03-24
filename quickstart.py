import os
import sys
from natsort import natsorted #good for sorting string array containing strings and numbers
from pathlib import Path #used to get home directory and works on all platforms
#best human sort method
try:
  #import module
  from pydrive.auth import GoogleAuth
  from pydrive.drive import GoogleDrive
  
except ModuleNotFoundError:
  import subprocess
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pydrive'])


# Authenticate the client
gauth = GoogleAuth()
# gauth.LocalWebserverAuth() #Creates local webserver and auto handles authentication.


# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
  # Authenticate if they're not there
  gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
  # Refresh them if expired
  gauth.Refresh()
else:
  # Initialize the saved creds
  gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)


file_list = []
homeDir = str(Path.home())
file_toUpload = os.chdir(f'{homeDir}\\Documents\\Wuxiaworld\\keyboard immortal\\Chapters')
# file_toUpload = os.chdir(f'{homeDir}\\Documents\\Wuxiaworld\\Mages are too OP\\Chapters')
dirlist = os.listdir()
dirlist = natsorted(dirlist)
cur_chapter = dirlist[-1] #### Need to move this out later, to leave this exclusively for uploads

drive_folderId = '1A4vM2aYOegQiMXNZZv8xU0jjt4x6x8vX'



fileObject_list = drive.ListFile({'q': f"'{drive_folderId}' in parents and trashed=false"}).GetList()

for file_object in fileObject_list: # get list of file names in the drive folder
  file_list.append(file_object['title'])


for file in dirlist:  # check if file from folder already exists in drive folder
  if file not in file_list:
    drive_folder = drive.CreateFile({'parents': [{'id' : drive_folderId}]}) 
    #https://stackoverflow.com/questions/56434084/google-pydrive-uploading-a-file-to-specific-folder
    drive_folder.SetContentFile(file)
    drive_folder.Upload()

  else:
    continue
  # print(file)
  


# for file1 in file_list:

#   print(f'File name: {file1["title"]} \n File id: {file1["id"]}')
#   for files in dirlist:
#     print(files)


# # Try to load saved client credentials
# gauth.LoadCredentialsFile("mycreds.txt")
# if gauth.credentials is None:
#   # Authenticate if they're not there
#   gauth.LocalWebserverAuth()
# elif gauth.access_token_expired:
#   # Refresh them if expired
#   gauth.Refresh()
# else:
#   # Initialize the saved creds
#   gauth.Authorize()
# # Save the current credentials to a file
# gauth.SaveCredentialsFile("mycreds.txt")



# textfile = drive.CreateFile({'title': 'Hello.txt'})
# # textfile.SetContentFile('eng.txt') # this allows you to choose a file to upload
# textfile.SetContentString('hello world') # this allows you to set content of file
# textfile.Upload()
# folder_metadata = {
#   'title': '@Voice',
#   # The mimetype defines this new file as a folder, so don't change this.
#   'mimeType': 'application/vnd.google-apps.folder'
# }
# folder = drive.CreateFile(folder_metadata)
# folder.Upload()

# # Get folder info and print to screen.
# folder_title = folder['title']
# folder_id = folder['id']

# print(f"title: {folder_title} id: {folder_id}")

# # Upload file to folder
# # f = drive.CreateFile({
# #   'parents': [{'id': folder_id}],
# #   'title': 'Keyboard Immortal Chapter 1'
# #   })

# # Make sure to add the path to the file to upload below.
# f.SetContentFile('C:\\Users\\h.feahn\\Documents\\Wuxiaworld\\Keyboard Immortal\\Chapters\\KI Chapter 173 Earth Seal WuxiaWorld.html')
# f.Upload()

# Auto-iterate through all files that matches this query
# file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
# for file1 in file_list:
#     print('title: {}, id: {}'.format(file1['title'], file1['id']))

# # Paginate file lists by specifying number of max results
# for file_list in drive.ListFile({'maxResults': 10}):
#     print('Received {} files from Files.list()'.format(len(file_list))) # <= 10
#     for file1 in file_list:
#         print('title: {}, id: {}'.format(file1['title'], file1['id']))
