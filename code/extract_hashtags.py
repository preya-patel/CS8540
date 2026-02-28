import json
#input output file paths
f = open("/home/ubuntu/phase1_project/data/tweets_original_data.json", "r", encoding="utf-8")
out = open("/home/ubuntu/phase1_project/data/hashtags.txt", "w", encoding="utf-8")

count = 0

for line in f:
    try:
        tweet=json.loads(line)
        tags=tweet["entities"]["hashtags"]
	#format of hashtag stored eg-#covid
        for t in tags:
            out.write("#" + t["text"].lower() + "\n")
            count=count+1
    except:
        pass

f.close()
out.close()

#total hashtags extracted
print("hashtags extracted:", count)
