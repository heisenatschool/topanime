# Top Anime
(H2 Term 1 Spring Final Project)

*Top Anime* is a website showcasing my top 4 favorite anime.

The raw website is under `page/` and the django webserver is under `animeproject/`. The web app is under the url `/topanime`.

Here is a picture of the webpage:
![Image](images/wp_img.png)

New anime can be added via the admin page, and must contain the following attributes:
| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `TITLE`   | Char(max_length = 100) | Anime title |
| `DESCR`   | Char(max_length = 300) | Anime description |
| `IMGPATH` | Char(max_length = 300) | Image path<br>A url reference `https://www.something.com/x.img`<br>A static files reference `\static\images\x.jpeg` |
| `SHOWN`   | Boolean                | Whether the image should be shown or not |
The first four anime with `SHOWN` set to True will display on the website
