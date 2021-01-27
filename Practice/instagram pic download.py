import instaloader
insta=instaloader.Instaloader()
a=input("Enter a username name: ")
insta.download_profile(a,profile_pic_only=True)
