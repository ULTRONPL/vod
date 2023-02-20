#działa tylko na odcinki seriali jak narazie
import requests
import re
while True:
    link_z = input()
    link_bez = link_z.replace("\\", "")
    print(link_bez, "<--- link bez (\)")
    id_z = link_bez.split("/")[-1]
    print(id_z)
    falszywe_id = id_z.split(",")[-1]
    print(falszywe_id, "<--- nieprawdziwe id video")
    link_api_id = "https://vod.tvp.pl/api/products/vods/" + str(falszywe_id) + "?lang=pl&platform=BROWSER"
    print(link_api_id)
    r = requests.get(link_api_id)
    print(r, "<--- jeśli wartość 200 to poprawnie udało uzyskać strone")
    strona_z_id = r.content
    file = open("id.txt", "w")
    file.write(str(strona_z_id))
    file.close()
    with open("id.txt", "r") as id_file:
        first_line = id_file.readline()
        id_video_z = first_line[47:57]
        print(id_video_z)
        id_video = id_video_z.replace('"', "")
        print(id_video)
        file = open("id.txt", "w")
        file.write(str(id_video))
        file.close()
    link_video_strona = "https://vod.tvp.pl/sess/TVPlayer2/api.php?id=" + str(id_video) + "&@method=getTvpConfig&@callback=callback"
    print(link_video_strona)
    videosite = requests.get(link_video_strona)
    strona_video_plik = videosite.content
    video_strona_bez = str(strona_video_plik).replace("\\", "")
    print(video_strona_bez)
    file = open("video_strona.txt", "w")
    file.write(str(video_strona_bez))
    file.close()    
    with open("video_strona.txt") as file:    
        for line in file:
            pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
            urls = re.findall(pattern, line)
            urls_all = print(urls)
    url_bez_enter = str(urls).replace(',', '\n')
    print(url_bez_enter, "\n                                                                                                            pliki tylko .mp4 reszta nieważna \n                                                                                                            video-(większy numer=lepsza jakość).mp4")

    
    
