import requests
import re
while True:
    #fake id
    link_z = input()
    link_bez = link_z.replace("\\", "")
    id_z = link_bez.split("/")[-1]
    falszywe_id = id_z.split(",")[-1]
    #real id
    link_api_id = "https://vod.tvp.pl/api/products/vods/" + str(falszywe_id) + "?lang=pl&platform=BROWSER"
    r = requests.get(link_api_id)
    strona_z_id = r.content
    file = open("data\\id.txt", "w")
    file.write(str(strona_z_id))
    file.close()
    with open("data\\id.txt", "r") as id_file:
        first_line = id_file.readline()
        id_video_z = first_line[35:65]
        #print(id_video_z)
        id_video = re.sub("[^0-9^.]", "", id_video_z)
        #print(id_video)
        file = open("data\\id.txt", "w")
        file.write(str(id_video))
        file.close()
    #api
    link_video_strona = "https://vod.tvp.pl/sess/TVPlayer2/api.php?id=" + str(id_video) + "&@method=getTvpConfig&@callback=callback"
    headers = {"Accept": "application/json"}
    videosite = requests.get(link_video_strona, headers=headers)
    json_data = videosite.json()
    replace = str(json_data).replace(",", "\n")
    final = str(replace).replace("'", "")
    mp4_links = re.findall("https?:\/\/\S+\.mp4", final)
    for link in mp4_links:
        print(link)
    print("video-(większy numer=lepsza jakość).mp4")
    

    while True:
        pass
