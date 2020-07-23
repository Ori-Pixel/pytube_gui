# pytube_gui
A standalone youtube downloader using pytube3.

## V0.0.01 How to Run the Application
1. Run application

2. Enter youtube video URL. Accepted urls are in the following format:

`https://youtube.com/watch?v={video_id}`
`https://youtube.com/embed/{video_id}`
`https://youtu.be/{video_id}`

3. Select "Load Video Quality." This will open a new window with available video and audio formats. Select your desired video/audio format. This closes the window. A download button will appear only after a video quality is selected.

4. Select download folder. If this option is not selected, it will download into the directory the application is stored.

4. Hit download now.

##Quirks and issues
###Secondary window opens but there are no options.
If you do not enter an appropriate video url, the application may open the new window, but no options will be available. Close the top level window and enter a functioning youtube url again.

###Buttons stay pressed or application is not responding
The Application may perform slowly based on internet connection. If the button is depressed, it is working in the backend. Especially on video download, it will remain pressed until the video is saved (which can take a very long time).

##Future Update Plans
1. Playlist downloading.
2. Video URL queueing
3. URL csv/txt file downloading
4. Adding more video sites alongside youtube with site parser
