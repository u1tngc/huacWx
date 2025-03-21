#PGM-ID:WX0S0101
#PGM-NAME:[P]WX天気ID検索

def get_wx(wx_code,cd):
    if cd == 1:
        wx = {
            "200" : "弱い雷雨",
            "201" : "雷雨",
            "202" : "強い雷雨",
            "210" : "弱い雷",
            "211" : "雷",
            "212" : "強い雷",
            "221" : "時折雷",
            "230" : "雷を伴う弱い霧雨",
            "231" : "雷を伴う霧雨",
            "232" : "雷を伴う強い霧雨",
            "300" : "弱い霧雨",
            "301" : "霧雨",
            "302" : "強い霧雨",
            "310" : "弱い雨と霧雨",
            "311" : "雨と霧雨",
            "312" : "強い雨と霧雨",
            "313" : "驟雨と霧雨",
            "314" : "強い驟雨と霧雨",
            "321" : "驟雨性の霧雨",
            "500" : "小雨",
            "501" : "雨",
            "502" : "強い雨",
            "503" : "非常に強い雨",
            "504" : "猛烈な雨", 
            "511" : "雨氷",
            "520" : "弱い驟雨",
            "521" : "驟雨",
            "522" : "強い驟雨",
            "531" : "時折驟雨",
            "600" : "弱い雪",
            "601" : "雪",
            "602" : "強い雪",
            "611" : "凍雨",
            "612" : "驟雨性の凍雨",
            "615" : "弱いみぞれ",
            "616" : "みぞれ",
            "620" : "弱い驟雨性の雪",
            "621" : "驟雨性の雪",
            "622" : "強い驟雨性の雪",
            "701" : "靄",
            "711" : "煙",
            "721" : "煙霧",
            "731" : "砂塵旋風",
            "741" : "霧",
            "751" : "砂",
            "761" : "塵",
            "762" : "火山灰",
            "771" : "スコール",
            "781" : "竜巻",
            "800" : "快晴",
            "801" : "晴（FEW）",
            "802" : "晴（SCT）",
            "803" : "晴（BKN）",
            "804" : "曇（OVC）"
        }
        str = wx[wx_code]     
    elif cd == 2:
        wx_code =int(wx_code)
        png_url = './fonts/wx_png/'
        if wx_code >= 200 and wx_code < 300:
            png_url += '11d.png'
        elif wx_code >= 300 and wx_code < 400:
            png_url += '09d.png'
        elif wx_code >= 500 and wx_code < 600:
            png_url += '10d.png'
        elif wx_code >= 600 and wx_code < 700:
            png_url += '13d.png'
        elif wx_code >= 700 and wx_code < 800:
            png_url += '50d.png'
        elif wx_code == 800:
            png_url += '01d.png'
        elif wx_code == 801:
            png_url += '02d.png'
        elif wx_code == 802:
            png_url += '03d.png'
        elif wx_code == 803:
            png_url += '04d.png'
        elif wx_code == 804:
            png_url += '04d.png'
        str = png_url
    return str