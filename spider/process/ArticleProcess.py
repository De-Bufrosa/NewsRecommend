import util.Request as Request
import util.Time as Time
import util.Driver as Driver
import model.ArticleModel as ArtMod
import model.CustomerModel as CusMod

import logging


class ArticleProcess:
    """ 文章数据的获取与填充填充

    # 20-17-04 依据新的 SQL 修改

    """


    def get_arts_brief_json_by_category(self, category):
        """ 获取文章缩率信息, 不包括文章内容

        # 20-04-17 方法检查 OK

        参考接口:
            http://m.toutiao.com/list/?tag=__all__&ac=wap&count=20&format=json_raw&as=A17538D54D106FF&cp=585DF0A65F0F1E1&min_behot_time=1482491618

        :param category:
            '社会': 'news_society',
            '娱乐': 'news_entertainment',
            '科技': 'news_tech',
            '军事': 'news_military',
            '体育': 'news_sports'
            '汽车': 'news_car',
            '财经': 'news_finance',
            '国际': 'news_world',
            '时尚': 'news_fashion',
            '旅游': 'news_travel',
            '探索': 'news_discovery',
            '育儿': 'news_baby',
            '养生': 'news_regimen',
            '故事': 'news_story',
            '美文': 'news_essay',
            '游戏': 'news_game',
            '历史': 'news_history',
            '美食': 'news_food',
        :return:
            example:
            [
                Object{...},
                Object{...},
                Object{...},
                {
                    "media_name":"呦呦科学馆",
                    "ban_comment":0,
                    "abstract":"大家对屎壳郎都会有所耳闻，屎壳郎的原名是蜣螂（qiāng láng），一种痴迷于推粪球的昆虫，我们一直以来都没有什么正面评价，有时候在评价一个人不好的时候，会把他说成是屎壳郎。虽然屎壳郎在我们这儿，没有什么正面的评价，但是有些地方把它当成是神哦！不是负面的神，而是太阳神！",
                    "image_list":[
                        {
                            "url":"http://p6-tt.byteimg.com/img/pgc-image/a9b944c7417847e687b5f97aeb2798ad~tplv-tt-cs0:640:360.jpg",
                            "width":640,
                            "height":360
                        },
                        {
                            "url":"http://p6-tt.byteimg.com/img/pgc-image/2ca2e18621f942daa6b7e602205b4492~tplv-tt-cs0:525:576.jpg",
                            "width":525,
                            "height":295
                        },
                        {
                            "url":"http://p9-tt.byteimg.com/img/pgc-image/3605e63e394e45b494d2cc5914662a8c~tplv-tt-cs0:628:344.jpg",
                            "width":628,
                            "height":344
                        }
                    ],
                    "datetime":"2020-01-03 20:30",
                    "article_type":0,
                    "more_mode":true,
                    "tag":"news_story",
                    "has_m3u8_video":0,
                    "display_dt":1577527020,
                    "has_mp4_video":0,
                    "aggr_type":1,
                    "cell_type":0,
                    "article_sub_type":0,
                    "bury_count":0,
                    "title":"屎壳郎的故事",
                    "source_icon_style":1,
                    "tip":0,
                    "has_video":false,
                    "share_url":"http://toutiao.com/a6775056296904229390/?app=news_article&is_hit_share_recommend=0",
                    "source":"呦呦科学馆",
                    "comment_count":0,
                    "article_url":"http://toutiao.com/group/6775056296904229390/",
                    "publish_time":1577527020,
                    "group_flags":0,
                    "gallary_image_count":4,
                    "action_extra":"{"channel_id": 3189398979}",
                    "tag_id":"6775056296904229390",
                    "source_url":"/i6775056296904229390/",
                    "display_url":"http://toutiao.com/group/6775056296904229390/",
                    "is_stick":false,
                    "item_id":"6775056296904229390",
                    "repin_count":12,
                    "cell_flag":262155,
                    "source_open_url":"sslocal://profile?uid=566976876133454",
                    "level":0,
                    "digg_count":6,
                    "behot_time":1578054637,
                    "hot":0,
                    "cursor":1578054637999,
                    "url":"http://toutiao.com/group/6775056296904229390/",
                    "user_repin":0,
                    "has_image":true,
                    "video_style":0,
                    "media_info":{
                        "avatar_url":"http://p1.pstatp.com/large/ffe800001f90d3b65398",
                        "media_id":1629031487078411,
                        "name":"呦呦科学馆",
                        "user_verified":true
                    },
                    "group_id":"6775056296904229390"
                },
                Object{...}
            ]

        :param category:
        :return:
        """
        try:
            url = 'http://m.toutiao.com/list/?tag={0}&ac=wap&count=20&format=json_raw&as=A17538D54D106FF&cp=585DF0A65F0F1E1&min_behot_time=1482491618'.format(category)
            headers = {
                "Host": "m.toutiao.com",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
            cookies = {
                "tt_webid": "6754560229981750791",
                "WEATHER_CITY": "%E5%8C%97%E4%BA%AC",
                "csrftoken": "4e76bad8185f77ea8b647e50e3bb0e26",
                "_ga": "GA1.2.268549673.1572668703",
                "__utmz": "24953151.1578051975.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
                "__utma": "24953151.268549673.1572668703.1578051975.1578221568.2",
                "SLARDAR_WEB_ID": "60060dd2-e5b2-470c-b7f4-09b8d877a031",
                "ttcid": "3f7ad0f028c54aa584367115a3fa7cb028",
                "__ac_nonce": "05ecba43c0082bbdfb3e",
                "__ac_signature": "O2auwAAgEBACmHx7dlnWxztnr9AAGWz3dGBVQL.r0H1se1MOmPcu.0Mxo.Y9Zem1qLCx5rV13rttFjnqiBP7d4KfTBbgN8Az4ip.Po5Ht9XBlX2CZW8ZIUZV9blZ9smX461",
                "s_v_web_id": "verify_kamdklmd_rcCyRT2X_ZLBe_4OQI_Brjy_Q7HFKjeCzPbt",
                "__tasessionId": "gx98j8z1x1590404157654",
                "tt_scid": "nLlc9z1mWQgXRhJFHC7i29KXmnHM9sZynN1Ue86iBmH5DPSaDONSaQYQz7mqHMcMf924"
            }


            result = Request.Request(url, headers, cookies).more()['data']
            # print(result)
            logging.info("获取新闻缩率信息 %s 成功" % url)
            return result
        except:
            # logging.exception("获取新闻缩率信息 失败")
            return None


    def set_art(self, art_brief_json, category, art_cus_id, art_mod: ArtMod.ArticleModel):
        """ 插入新闻内容

        # 20-04-17 修改完成

        :param art_brief_json:
        :param category:
        :param art_cus_id:
        :param art_mod:
        :return:
        """
        driver = Driver.Driver.get_chrome_driver()

        try:
            url = "https://www.toutiao.com/a{0}/".format(art_brief_json['item_id'])
            driver.implicitly_wait(3)
            driver.get(url)

            art_mod.art_spider = art_brief_json['item_id']
            try:
                if len(art_brief_json['image_list']) == 0:
                    art_mod.art_image_url = ''
                else:
                    for tar in art_brief_json['image_list']:
                        art_mod.art_image_url = tar['url']
                        break
            except:
                art_mod.art_image_url = ''
            art_mod.art_legal = 1
            art_mod.art_time = Time.Time.time_trans(art_brief_json['publish_time'])
            art_mod.art_cus_id = art_cus_id
            art_mod.art_id = None
            try:
                art_mod.art_tags = art_brief_json['keywords']
            except:
                art_mod.art_tags = ''
            art_mod.art_type = category
            art_mod.art_title = art_brief_json['title']

            art_mod.art_content = driver.find_element_by_class_name("syl-page-article").get_attribute('innerHTML')

            logging.info("设置新闻数据 url=%s 成功" % url)
        except:
            # logging.exception("设置新闻数据 失败")

            raise
        finally:
            driver.close()


    @DeprecationWarning
    def get_art_json(self, art_brief_json):
        """ 获得一则新闻的具体内荣

        参考接口:
            http://m.toutiao.com/i6364969235889783298/info/

        :param art_brief_json:
        :return:
            example:
            {
                "detail_source":"正向娱乐energy",
                "media_user":{
                    "screen_name":"正向娱乐energy",
                    "no_display_pgc_icon":false,
                    "avatar_url":"http://p1.pstatp.com/thumb/ff0600002c7db3631cde",
                    "id":"52681187308",
                    "user_auth_info":{
                        "auth_type":"0",
                        "other_auth":{
                            "interest":"优质娱乐领域创作者"
                        },
                        "auth_info":"青云计划获奖者 优质娱乐领域创作者"
                    }
                },
                "publish_time":1574065021,
                "hotwords":[
                    {
                        "stress_type":0,
                        "hot_word":"录明星整容视频勒索"
                    },
                    {
                        "stress_type":1,
                        "hot_word":"宁静再演孝庄"
                    },
                    ...
                ],
                "labels":[

                ],
                "title":"李诞向左，池子向右，脱口秀背后的悲喜人生",
                "url":"http://toutiao.com/group/6760557790046978567/",
                "high_quality_flag":"0",
                "impression_count":"790339",
                "is_original":true,
                "is_pgc_article":true,
                "content":"<div class="pgc-img">... ... 剩下的都是文章内容的 HTML 形式",
                "source":"正向娱乐energy",
                "comment_count":326,
                "logo_show_strategy":"normal",
                "hupu_content_image_urls":[
                    ""
                ],
                "creator_uid":52408555030
            }
        """
        try:
            art_url = 'http://m.toutiao.com/i{0}/info/'.format(art_brief_json['item_id'])
            headers = {
                "Host": "m.toutiao.com",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }
            result = Request.Request(art_url, headers).more()['data']
            logging.info("获取新闻内容数据 %s 成功" % art_url)
            return result
        except:
            # logging.exception("获取新闻内容数据 失败")
            return None






