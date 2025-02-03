import instaloader

# Create an Instaloader instance
loader = instaloader.Instaloader()

# Replace these with your Instagram credentials
username = "shailesh_0x1A"
password = "Avks@1234"

# Replace this with the target Instagram username
target_username = "yugaa_shey"

try:
    # Log in to your Instagram account
    loader.login(username, password)
    print("Logged in successfully!")


    # Load the target profile
    profile = instaloader.Profile.from_username(loader.context, target_username)

    print(profile.full_name)
    print(profile.biography_hashtags)

    print(f"Followers of {target_username}:")
    for follower in profile.get_followers():
        print(follower.username)
    print(f"{target_username} Follows : ")
    for following in profile.get_followees():
        print(following.username)

except instaloader.exceptions.ConnectionException as e:
    print("Failed to connect to Instagram:", e)
except instaloader.exceptions.BadCredentialsException:
    print("Invalid username or password.")
except instaloader.exceptions.LoginRequiredException:
    print("Login required to access this profile's followers.")
except Exception as e:
    print("An error occurred:",e)
