import requests
import getpass

def configure_session_and_url(shared_folder_name=None, owner=None): ### insert group folder name or leave empty for personal root
  '''
  interactively setup your sciencedata.dk homeurl, username and password
  in the case of shared folder, inquire for its owner as well
  '''
  sciencedata_homeurl = "https://sciencedata.dk/files/" ### your personal homeurl 
  username = input("sciencedata.dk username (format '123456@au.dk'): ")
  password = getpass.getpass("sciencedata.dk password: ")
  ### establish a request session
  s = requests.Session()
  s.auth = (username, password)
  root_folder_url = sciencedata_homeurl
  if s.get(sciencedata_homeurl).ok:
    print("personal connection established")
    if shared_folder_name != None:
      ### SETTING FOR SHARED FOLDER (you either have to be its owner, or at least know username of its owner)
      shared_folder_owner_url = "https://sciencedata.dk/files/" + shared_folder_name + "/"
      if s.get(shared_folder_owner_url).ok: ### if you are owner of the shared folder 
        root_folder_url = shared_folder_owner_url ### use the url as the endpoint
        print("connection with shared folder established with you as its owner")
      else: # otherwise use endpoint for "shared with me"
        if owner==None:
          owner = input("\"" + shared_folder_name + "\" owner's username: ") ### in the case Vojtech is folder owner
        shared_folder_member_url = "https://sciencedata.dk/sharingin/" + owner + "/" + shared_folder_name + "/" 
        if s.get(shared_folder_member_url).ok:
          root_folder_url = shared_folder_member_url
          print("connection with shared folder established with you as its ordinary user")
        else:
          print("connection with shared folder failed")
  print("endpoint variable has been configured to: " + root_folder_url)
  return s, root_folder_url
