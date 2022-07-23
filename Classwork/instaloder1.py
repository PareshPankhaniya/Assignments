import instaloder

data=instaloder.Istaloder()
username=input("enter  profile name:")
data.downaload_profile(username,profile_pic_only=True)