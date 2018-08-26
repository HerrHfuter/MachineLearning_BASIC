#coding=utf-8
import media
import fresh_tomatoes

film1 = media.Movie('无问西东',
                    'https://tc.sinaimg.cn/maxwidth.2048/tc.service.weibo.com/www_people_com_cn/362bb805d7240eb6812a70203c02f76f.jpg',
                    'http://v.youku.com/v_show/id_XMzMxNDUwNzI0MA==.html?spm=a2h0j.8191423.chasing.1~3~A',
                    '李芳芳','章子怡、黄晓明、张震、王力宏','2018年01月12日')
film2 = media.Movie('芳华',
                    'https://p1.ssl.qhmsg.com/dr/270_500_/t01bbbb527c07a8e5a1.png?size=436x613',
                    'http://v.youku.com/v_show/id_XMzAyMTgxNzA3Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.1',
                    '冯小刚','黄轩、苗苗','2017年12月15日')
film3 = media.Movie('战狼2',
                    'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2494701965.webp',
                    'http://v.youku.com/v_show/id_XMjQ4Mzc4ODQwOA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1',
                    '吴京','吴京','2017年7月27日')
film4 = media.Movie('绣春刀II：修罗战场',
                    'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2492665487.webp',
                    'http://v.youku.com/v_show/id_XMjg2NDY0MDU4NA==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1',
                    '路阳','张震、杨幂','2017年7月19日')
film5 = media.Movie('摔跤吧！爸爸',
                    'https://img3.doubanio.com/view/photo/m/public/p2457983084.webp',
                    'http://v.youku.com/v_show/id_XMjc0NTMwODQwMA==.html?spm=a2h0j.8191423.chasing.1~3!2~A',
                    '尼特什·提瓦瑞','阿米尔·汗','2017年5月5日')
film6 = media.Movie('速度与激情8',
                    'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2444256500.webp',
                    'http://v.youku.com/v_show/id_XMjYxNDkwOTg4MA==.html?spm=a2h0j.8191423.module_basic_relation.5~5!2~5~5!10~5~5~A',
                    'F·加里·格雷','范·迪塞尔、道恩·强森','2017年4月14日')
movies = [film1,film2,film3,film4,film5,film6]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.__doc__)