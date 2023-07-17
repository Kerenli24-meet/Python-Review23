def create_youtube_video(title,description):
	youtube_videoN ={"title": title,"description" : description, "likes": 0,"dislikes":0,"comments":{}}
	return(new_youtube_video)

def likes(youtube_video):
	if "likes" in youtube_video:
		youtube_video{"likes"}+= 1
	return youtube_video

def disikes(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video{"dislikes"}+= 1
	return youtube_video

def add_comment(youtubeVideo,username,comment_text):
	youtubeVideo["comments"] = {username:comment_text}
	return youtubeVideo
NewVideo = create_youtube_video("GET READY WITHH ME","MORNING ROUTINE")
likes(NewVideo)
disikes(NewVideo)
add_comment(NewVideo,"YOU ARE THE BEST!", "VERy GOOD VIDEO")
print(NewVideo)
while NewVideo["likes"] < 495:
	likes(NewVideo)
print(NewVideo)

