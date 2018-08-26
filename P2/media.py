#coding=utf-8
import webbrowser
class Movie():
    """一个用于描述电影的类"""

    def __init__(self,title,poster_image_url,trailer_url,director,
                 leading_role,release_date):
        """初始化电影类的属性"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
        self.director = director
        self.leading_role = leading_role
        self.release_date = release_date
    def show_trailer(self):
        """打开预告片链接"""
        webbrowser.open(self.trailer_url)