import webbrowser, os, sys, random, string

platforms = {
    "facebook": "https://m.facebook.com/login.php",
    "twitter": "https://mobile.twitter.com/login",
    "instagram": "https://www.instagram.com/accounts/login/",
    "linkedin": "https://www.linkedin.com/checkpoint/rp/signin",
    "reddit": "https://www.reddit.com/login",
    "tiktok": "https://www.tiktok.com/login/phone",
}

def generate_phishing_link(platform):
    if platform in platforms:
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        return platforms[platform] + "?phish=" + random_str
    else:
        return None

selected_platform = input("Enter the platform name (facebook, twitter, instagram, linkedin, reddit, tiktok): ")
phishing_link = generate_phishing_link(selected_platform)

if phishing_link:
    print("Here's the phishing link:", phishing_link)
    input("Press Enter to open the link...")
    webbrowser.open(phishing_link)
else:
    print("Invalid platform selected.")

def save_credentials(platform, username, password):
    with open("details.txt", "a") as file:
        file.write(f"{platform}: {username},{password}\n")

# Example usage:
username = input("Enter your username: ")
password = input("Enter your password: ")
save_credentials(selected_platform, username, password)
