import os, pickle

import googleapiclient.discovery

# Antes de usar, você precisa de uma developer key do YT
# DEVELOPER_KEY = "SUA_KEY"

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    nextPageToken = ''

    comments = []
    while True:

        request = youtube.commentThreads().list(
            part="snippet",
            allThreadsRelatedToChannelId="UCaqc3TH-ZdPw7OTIlndvSgQ",
            pageToken=nextPageToken
        )
        response = request.execute()

        # for k in response['items'][0]['snippet'].keys():
        #     print(k)
        for item in response['items']:
            # print('--------------------------')
            # print(item['snippet']['topLevelComment']['snippet']['textOriginal'])
            # print('--------------------------')
            comments.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])
        
        print(f"Read {len(comments)} already ...")

        try:
            nextPageToken = response['nextPageToken']
        except:
            break

    with open('comments', 'wb') as fp:
        pickle.dump(comments, fp)

if __name__ == "__main__":
    main()