import redis
conn = redis.Redis()
conn.zadd("zzh:1:baidu:queue","(dp1\nVurl\np2\nVhttp://www.moe.edu.cn/jyb_xxgk/moe_1777/moe_1779/\np3\nsVexpires\np4\nI0\nsS'ts'\np5\nF1516955068.9022441\nsVpriority\np6\nI1\nsVcallback\np7\nVparse_inform_index\np8\nsVmeta\np9\n(dp10\nVsecond_page_css\np11\n(dp12\nVbody\np13\nVtrue\np14\nsVtitle\np15\nVh1\np16\nssVfirst_page_css\np17\n(dp18\nVsecond_page_url\np19\nVa::attr(href)\np20\nsVtime\np21\nVspan\np22\nsVlist_from\np23\nV.scy_lbsj-right-nr ul li\np24\nsVtitle\np25\nVa::attr(title)\np26\nsssVspider_type\np27\nVzzh\np28\nsVmaxdepth\np29\nI0\ns.",1)