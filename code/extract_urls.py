import json
#input output file paths
f=open("/home/ubuntu/phase1_project/data/tweets_original_data.json", "r", encoding="utf-8")
out=open("/home/ubuntu/phase1_project/data/urls.txt", "w", encoding="utf-8")

count=0

for line in f:
    try:
        tweet=json.loads(line)

        #normal urls
        urls=tweet["entities"]["urls"]
        for u in urls:
            out.write(u["expanded_url"]+"\n")
            count=count+1

        #media urls-images/videos
        if "media" in tweet["entities"]:
            media=tweet["entities"]["media"]
            for m in media:
                out.write(m["url"]+"\n")
                count=count+1
    except:
        pass

f.close()
out.close()
#total urls extracted
print("urls extracted:", count)
