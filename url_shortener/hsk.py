#! /usr/bin/env python
# hsk.py
# David Prager Branner
# 20140527, works.

"""Supplies lists of the most common Chinese characters."""

# This module supplies list of the characters in the domain of the "New" 
# (March, 2010) Hanyu Shuiping Kaoshi (HSK) level 6.
#
#   Variable simp contains the 2635 characters in the simplified set;
#   trad contains the 2671 characters in the corresponding traditional set.
#
# Both sets sorted in traditional radical order.

simp = ['一',  '丁',  '七',  '万',  '丈',  '三',  '上',  '下',  '不',  '与',  '丐',  '丑',  '专',  '且',  '世',  '丘',  '丙',  '业',  '丛',  '东',  '丝',  '丢',  '两',  '严',  '丧',  '个',  '中',  '丰',  '串',  '临',  '丸',  '为',  '主',  '丽',  '举',  '久',  '么',  '义',  '之',  '乌',  '乎',  '乏',  '乐',  '乒',  '乓',  '乖',  '乘',  '乙',  '九',  '乞',  '也',  '习',  '乡',  '书',  '买',  '乱',  '乳',  '了',  '予',  '争',  '事',  '二',  '于',  '亏',  '云',  '互',  '五',  '井',  '亚',  '些',  '亡',  '交',  '亦',  '产',  '享',  '京',  '亭',  '亮',  '亲',  '人',  '亿',  '什',  '仁',  '仅',  '仇',  '今',  '介',  '仍',  '从',  '仓',  '仔',  '他',  '仗',  '付',  '仙',  '代',  '令',  '以',  '仪',  '们',  '仰',  '件',  '价',  '任',  '份',  '仿',  '企',  '伍',  '伏',  '伐',  '休',  '众',  '优',  '伙',  '会',  '伞',  '伟',  '传',  '伤',  '伦',  '伪',  '伯',  '估',  '伴',  '伶',  '伸',  '伺',  '似',  '但',  '位',  '低',  '住',  '体',  '何',  '余',  '佛',  '作',  '你',  '佣',  '佩',  '佳',  '使',  '侈',  '例',  '供',  '依',  '侠',  '侣',  '侦',  '侧',  '侨',  '侮',  '侵',  '便',  '促',  '俊',  '俐',  '俗',  '俘',  '保',  '信',  '俩',  '俭',  '修',  '俯',  '俱',  '倍',  '倒',  '倘',  '候',  '借',  '倡',  '倦',  '债',  '值',  '倾',  '假',  '偏',  '做',  '停',  '健',  '偶',  '偷',  '偿',  '傅',  '傍',  '储',  '催',  '傲',  '傻',  '像',  '僵',  '僻',  '儿',  '允',  '元',  '兄',  '充',  '兆',  '先',  '光',  '克',  '免',  '兑',  '兔',  '党',  '兜',  '兢',  '入',  '全',  '八',  '公',  '六',  '共',  '关',  '兴',  '兵',  '其',  '具',  '典',  '养',  '兼',  '兽',  '内',  '册',  '再',  '冒',  '写',  '军',  '农',  '冠',  '冤',  '冬',  '冰',  '冲',  '决',  '况',  '冷',  '冻',  '净',  '凄',  '准',  '凉',  '凌',  '减',  '凑',  '凝',  '几',  '凡',  '凭',  '凶',  '凸',  '凹',  '出',  '击',  '刀',  '分',  '切',  '刊',  '刑',  '划',  '列',  '则',  '刚',  '创',  '初',  '删',  '判',  '利',  '别',  '刮',  '到',  '制',  '刷',  '券',  '刹',  '刺',  '刻',  '剂',  '削',  '前',  '剔',  '剖',  '剥',  '剧',  '剩',  '剪',  '副',  '割',  '劈',  '力',  '劝',  '办',  '功',  '加',  '务',  '劣',  '动',  '助',  '努',  '劫',  '励',  '劲',  '劳',  '势',  '勃',  '勇',  '勉',  '勘',  '勤',  '勺',  '勾',  '勿',  '匀',  '包',  '匆',  '化',  '北',  '匙',  '匪',  '匹',  '区',  '医',  '十',  '千',  '升',  '午',  '半',  '华',  '协',  '卑',  '卓',  '单',  '卖',  '南',  '博',  '占',  '卡',  '卧',  '卫',  '印',  '危',  '即',  '却',  '卷',  '卸',  '厂',  '厅',  '历',  '厉',  '压',  '厌',  '厕',  '厘',  '厚',  '原',  '厢',  '厦',  '厨',  '去',  '县',  '参',  '又',  '叉',  '及',  '友',  '双',  '反',  '发',  '叔',  '取',  '受',  '变',  '叙',  '叛',  '叠',  '口',  '古',  '句',  '另',  '叨',  '只',  '叫',  '召',  '叭',  '叮',  '可',  '台',  '史',  '右',  '叶',  '号',  '司',  '叹',  '叼',  '吁',  '吃',  '各',  '合',  '吉',  '吊',  '同',  '名',  '后',  '吐',  '向',  '吓',  '吗',  '吝',  '吞',  '吟',  '否',  '吧',  '吨',  '吩',  '含',  '听',  '启',  '吵',  '吸',  '吹',  '吻',  '吼',  '呀',  '呆',  '呈',  '告',  '呕',  '员',  '呢',  '周',  '味',  '呵',  '呻',  '呼',  '命',  '咀',  '咋',  '和',  '咐',  '咖',  '咙',  '咨',  '咬',  '咱',  '咳',  '咸',  '咽',  '哀',  '品',  '哄',  '哆',  '哇',  '哈',  '响',  '哎',  '哑',  '哟',  '哥',  '哦',  '哨',  '哪',  '哭',  '哲',  '哺',  '哼',  '唆',  '唇',  '唉',  '唐',  '唠',  '售',  '唯',  '唱',  '唾',  '啃',  '商',  '啊',  '啡',  '啤',  '啥',  '啦',  '啬',  '啰',  '啸',  '喂',  '善',  '喇',  '喉',  '喊',  '喘',  '喜',  '喝',  '喷',  '喻',  '嗅',  '嗓',  '嗦',  '嗨',  '嗯',  '嗽',  '嘈',  '嘉',  '嘛',  '嘱',  '嘲',  '嘴',  '嘿',  '器',  '噪',  '嚏',  '嚷',  '嚼',  '四',  '回',  '因',  '团',  '园',  '困',  '围',  '固',  '国',  '图',  '圆',  '圈',  '土',  '圣',  '在',  '地',  '场',  '圾',  '址',  '均',  '坏',  '坐',  '坑',  '块',  '坚',  '坛',  '坝',  '坟',  '坡',  '坦',  '垂',  '垃',  '垄',  '型',  '垫',  '埋',  '城',  '域',  '培',  '基',  '堂',  '堆',  '堕',  '堡',  '堤',  '堪',  '堵',  '塌',  '塑',  '塔',  '塘',  '塞',  '填',  '境',  '墅',  '墓',  '墙',  '增',  '墟',  '墨',  '壁',  '壤',  '士',  '壮',  '声',  '壳',  '壶',  '处',  '备',  '复',  '夏',  '夕',  '外',  '多',  '夜',  '够',  '大',  '天',  '太',  '夫',  '央',  '失',  '头',  '夸',  '夹',  '夺',  '奇',  '奈',  '奉',  '奋',  '奏',  '奔',  '奖',  '套',  '奠',  '奢',  '奥',  '女',  '奴',  '奶',  '她',  '好',  '如',  '妄',  '妆',  '妇',  '妈',  '妒',  '妙',  '妥',  '妨',  '妹',  '妻',  '姆',  '始',  '姐',  '姑',  '姓',  '委',  '姥',  '姨',  '姻',  '姿',  '威',  '娃',  '娇',  '娘',  '娱',  '娶',  '婆',  '婚',  '婪',  '婴',  '媒',  '媳',  '嫁',  '嫂',  '嫉',  '嫌',  '嫩',  '子',  '孔',  '孕',  '字',  '存',  '孙',  '孝',  '季',  '孤',  '学',  '孩',  '宁',  '它',  '宅',  '宇',  '守',  '安',  '完',  '宏',  '宗',  '官',  '宙',  '定',  '宜',  '宝',  '实',  '宠',  '审',  '客',  '宣',  '室',  '宪',  '宫',  '宰',  '害',  '宴',  '宵',  '家',  '容',  '宽',  '宾',  '宿',  '寂',  '寄',  '密',  '富',  '寒',  '寓',  '寞',  '察',  '寸',  '对',  '寺',  '寻',  '导',  '寿',  '封',  '射',  '将',  '尊',  '小',  '少',  '尔',  '尖',  '尘',  '尚',  '尝',  '尤',  '尬',  '就',  '尴',  '尸',  '尺',  '尽',  '尾',  '局',  '屁',  '层',  '居',  '屈',  '屉',  '届',  '屋',  '屏',  '屑',  '展',  '属',  '屡',  '履',  '山',  '屿',  '岁',  '岂',  '岔',  '岗',  '岛',  '岩',  '岳',  '岸',  '峡',  '峭',  '峰',  '峻',  '崇',  '崖',  '崩',  '崭',  '嵌',  '川',  '州',  '巡',  '工',  '左',  '巧',  '巨',  '巩',  '差',  '己',  '已',  '巴',  '巷',  '巾',  '币',  '市',  '布',  '帅',  '帆',  '师',  '希',  '帐',  '帖',  '帘',  '帜',  '帝',  '带',  '席',  '帮',  '常',  '帽',  '幅',  '幕',  '幢',  '干',  '平',  '年',  '并',  '幸',  '幻',  '幼',  '幽',  '广',  '庄',  '庆',  '庇',  '床',  '序',  '库',  '应',  '底',  '店',  '庙',  '府',  '庞',  '废',  '度',  '座',  '庭',  '康',  '庸',  '廉',  '廊',  '廓',  '延',  '建',  '开',  '异',  '弃',  '弄',  '弊',  '式',  '引',  '弟',  '张',  '弥',  '弦',  '弯',  '弱',  '弹',  '强',  '归',  '当',  '录',  '形',  '彩',  '彰',  '影',  '役',  '彻',  '彼',  '往',  '征',  '径',  '待',  '很',  '徊',  '律',  '徒',  '得',  '徘',  '徙',  '御',  '循',  '微',  '德',  '心',  '必',  '忆',  '忌',  '忍',  '志',  '忘',  '忙',  '忠',  '忧',  '快',  '念',  '忽',  '怀',  '态',  '怎',  '怒',  '怕',  '怖',  '怜',  '思',  '怠',  '急',  '性',  '怨',  '怪',  '怯',  '总',  '恋',  '恍',  '恐',  '恒',  '恕',  '恢',  '恨',  '恩',  '恭',  '息',  '恰',  '恳',  '恶',  '恼',  '悄',  '悉',  '悔',  '悟',  '悠',  '患',  '悦',  '您',  '悬',  '悲',  '悼',  '情',  '惊',  '惋',  '惑',  '惕',  '惜',  '惠',  '惦',  '惧',  '惨',  '惩',  '惫',  '惭',  '惮',  '惯',  '惰',  '想',  '惹',  '愁',  '愈',  '愉',  '意',  '愚',  '感',  '愣',  '愤',  '愧',  '愿',  '慈',  '慌',  '慎',  '慕',  '慢',  '慧',  '慨',  '慰',  '慷',  '憋',  '憾',  '懂',  '懒',  '戏',  '成',  '我',  '戒',  '或',  '战',  '戚',  '截',  '戴',  '户',  '房',  '所',  '扁',  '扇',  '手',  '才',  '扎',  '扑',  '扒',  '打',  '扔',  '托',  '扛',  '扣',  '执',  '扩',  '扫',  '扬',  '扭',  '扮',  '扯',  '扰',  '扶',  '批',  '找',  '承',  '技',  '抄',  '把',  '抑',  '抒',  '抓',  '投',  '抖',  '抗',  '折',  '抚',  '抛',  '抢',  '护',  '报',  '披',  '抬',  '抱',  '抵',  '抹',  '押',  '抽',  '拄',  '担',  '拆',  '拉',  '拌',  '拍',  '拐',  '拒',  '拓',  '拔',  '拖',  '拘',  '拙',  '招',  '拜',  '拟',  '拢',  '拣',  '拥',  '拦',  '拧',  '拨',  '择',  '括',  '拳',  '拼',  '拽',  '拾',  '拿',  '持',  '挂',  '指',  '按',  '挎',  '挑',  '挖',  '挚',  '挠',  '挡',  '挣',  '挤',  '挥',  '挨',  '挪',  '挫',  '振',  '挺',  '挽',  '捆',  '捉',  '捍',  '捎',  '捏',  '捐',  '捕',  '捞',  '损',  '捡',  '换',  '捣',  '捧',  '据',  '捷',  '掀',  '授',  '掉',  '掌',  '掏',  '掐',  '排',  '掘',  '掠',  '探',  '接',  '控',  '推',  '掩',  '措',  '掰',  '掷',  '揉',  '揍',  '描',  '提',  '插',  '握',  '揭',  '援',  '搀',  '搁',  '搂',  '搅',  '搏',  '搓',  '搜',  '搞',  '搬',  '搭',  '携',  '摄',  '摆',  '摇',  '摊',  '摔',  '摘',  '摧',  '摩',  '摸',  '撑',  '撒',  '撕',  '撞',  '撤',  '播',  '擅',  '操',  '擎',  '擦',  '攀',  '攒',  '支',  '收',  '改',  '攻',  '放',  '政',  '故',  '效',  '敌',  '敏',  '救',  '教',  '敞',  '敢',  '散',  '敬',  '数',  '敲',  '整',  '敷',  '文',  '斑',  '斗',  '料',  '斜',  '斟',  '斤',  '斥',  '斩',  '断',  '斯',  '新',  '方',  '施',  '旁',  '旅',  '旋',  '族',  '旗',  '无',  '既',  '日',  '旦',  '旧',  '旨',  '早',  '旬',  '旱',  '时',  '旷',  '旺',  '昂',  '昆',  '昌',  '明',  '昏',  '易',  '昔',  '星',  '映',  '春',  '昧',  '昨',  '是',  '昼',  '显',  '晃',  '晋',  '晒',  '晓',  '晕',  '晚',  '晤',  '晨',  '普',  '景',  '晰',  '晴',  '晶',  '智',  '晾',  '暂',  '暄',  '暑',  '暖',  '暗',  '暧',  '暴',  '曝',  '曲',  '更',  '曾',  '替',  '最',  '月',  '有',  '朋',  '服',  '朗',  '望',  '朝',  '期',  '木',  '未',  '末',  '本',  '术',  '朴',  '朵',  '机',  '朽',  '杀',  '杂',  '权',  '杆',  '李',  '材',  '村',  '杖',  '杜',  '束',  '杠',  '条',  '来',  '杯',  '杰',  '松',  '板',  '极',  '构',  '枉',  '析',  '枕',  '林',  '枚',  '果',  '枝',  '枪',  '枯',  '架',  '某',  '染',  '柔',  '柜',  '查',  '柬',  '柱',  '柴',  '柿',  '标',  '栋',  '栏',  '树',  '校',  '株',  '样',  '核',  '根',  '格',  '栽',  '桃',  '框',  '案',  '桌',  '桑',  '桔',  '档',  '桥',  '桨',  '桶',  '梁',  '梢',  '梦',  '梨',  '梯',  '械',  '梳',  '检',  '棉',  '棋',  '棍',  '棒',  '棕',  '森',  '棵',  '椅',  '植',  '椎',  '椒',  '椭',  '楚',  '楼',  '概',  '榜',  '榨',  '模',  '横',  '橙',  '橡',  '欠',  '次',  '欢',  '欣',  '欧',  '欲',  '欺',  '款',  '歇',  '歉',  '歌',  '止',  '正',  '此',  '步',  '武',  '歧',  '歪',  '歹',  '死',  '殃',  '殊',  '残',  '殖',  '殴',  '段',  '殿',  '毁',  '毅',  '母',  '每',  '毒',  '比',  '毕',  '毛',  '毫',  '毯',  '氏',  '民',  '氓',  '气',  '氛',  '氢',  '氧',  '水',  '永',  '汁',  '求',  '汇',  '汉',  '汗',  '江',  '池',  '污',  '汤',  '汰',  '汹',  '汽',  '沃',  '沉',  '沐',  '沙',  '沛',  '沟',  '没',  '沧',  '沫',  '沮',  '河',  '沸',  '油',  '治',  '沼',  '沾',  '沿',  '泄',  '泉',  '泊',  '泌',  '法',  '泛',  '泡',  '波',  '泥',  '注',  '泪',  '泰',  '泳',  '泻',  '泼',  '泽',  '洁',  '洋',  '洒',  '洗',  '洞',  '津',  '洪',  '洲',  '活',  '洽',  '派',  '流',  '浅',  '浇',  '浊',  '测',  '济',  '浏',  '浑',  '浓',  '浪',  '浮',  '浴',  '海',  '浸',  '涂',  '消',  '涉',  '涌',  '涕',  '涛',  '润',  '涨',  '涮',  '液',  '涵',  '淀',  '淆',  '淋',  '淘',  '淡',  '深',  '混',  '淹',  '添',  '清',  '渐',  '渔',  '渗',  '渠',  '渡',  '渣',  '温',  '港',  '渴',  '游',  '渺',  '湖',  '湾',  '湿',  '溃',  '溅',  '溉',  '源',  '溜',  '溪',  '溶',  '滋',  '滑',  '滔',  '滚',  '滞',  '满',  '滤',  '滥',  '滨',  '滩',  '滴',  '漂',  '漆',  '漏',  '演',  '漠',  '漫',  '潜',  '潮',  '澄',  '澈',  '澡',  '激',  '濒',  '瀑',  '灌',  '火',  '灭',  '灯',  '灰',  '灵',  '灶',  '灾',  '灿',  '炉',  '炎',  '炒',  '炭',  '炮',  '炸',  '点',  '炼',  '烁',  '烂',  '烈',  '烘',  '烛',  '烟',  '烤',  '烦',  '烧',  '烫',  '热',  '烹',  '焦',  '焰',  '然',  '煌',  '煎',  '煤',  '照',  '煮',  '熄',  '熊',  '熏',  '熟',  '熨',  '熬',  '燃',  '燥',  '爆',  '爬',  '爱',  '父',  '爷',  '爸',  '爽',  '片',  '版',  '牌',  '牙',  '牛',  '牢',  '牧',  '物',  '牲',  '牵',  '特',  '牺',  '犬',  '犯',  '状',  '犹',  '狂',  '狈',  '狗',  '狠',  '狡',  '独',  '狭',  '狮',  '狱',  '狼',  '猎',  '猖',  '猛',  '猜',  '猪',  '猫',  '献',  '猴',  '猾',  '率',  '玉',  '王',  '玩',  '环',  '现',  '玻',  '珍',  '珠',  '班',  '球',  '理',  '琢',  '琴',  '璃',  '瓜',  '瓣',  '瓦',  '瓶',  '瓷',  '甘',  '甚',  '甜',  '生',  '用',  '甩',  '甭',  '田',  '由',  '甲',  '申',  '电',  '男',  '画',  '畅',  '界',  '畏',  '畔',  '留',  '畜',  '略',  '番',  '畴',  '疆',  '疏',  '疑',  '疗',  '疙',  '疤',  '疫',  '疯',  '疲',  '疼',  '疾',  '病',  '症',  '痒',  '痕',  '痛',  '痪',  '痹',  '瘤',  '瘦',  '瘩',  '瘫',  '瘸',  '瘾',  '癌',  '登',  '白',  '百',  '皂',  '的',  '皆',  '皇',  '皮',  '皱',  '盆',  '盈',  '益',  '盐',  '监',  '盒',  '盖',  '盗',  '盘',  '盛',  '盟',  '目',  '盯',  '盲',  '直',  '相',  '盼',  '盾',  '省',  '眉',  '看',  '真',  '眠',  '眨',  '眯',  '眶',  '眼',  '着',  '睁',  '睛',  '睡',  '督',  '睦',  '睬',  '睹',  '瞎',  '瞒',  '瞧',  '瞩',  '瞪',  '瞻',  '矛',  '知',  '矩',  '短',  '矮',  '石',  '矿',  '码',  '砍',  '研',  '砖',  '破',  '砸',  '础',  '硕',  '硬',  '确',  '碌',  '碍',  '碎',  '碑',  '碗',  '碧',  '碰',  '碳',  '磁',  '磅',  '磋',  '磕',  '磨',  '示',  '礼',  '社',  '祖',  '祝',  '神',  '祥',  '票',  '祸',  '禁',  '福',  '离',  '禽',  '秀',  '私',  '秃',  '秋',  '种',  '科',  '秒',  '秘',  '租',  '秤',  '秩',  '积',  '称',  '移',  '稀',  '程',  '稍',  '税',  '稚',  '稠',  '稳',  '稻',  '稿',  '穴',  '究',  '穷',  '空',  '穿',  '突',  '窃',  '窄',  '窗',  '窜',  '窝',  '立',  '竖',  '站',  '竞',  '竟',  '章',  '童',  '竭',  '端',  '竹',  '笑',  '笔',  '符',  '笨',  '第',  '笼',  '等',  '筋',  '筐',  '筑',  '筒',  '答',  '策',  '筛',  '筷',  '筹',  '签',  '简',  '算',  '管',  '箭',  '箱',  '篇',  '篮',  '篷',  '簸',  '籍',  '米',  '类',  '粉',  '粒',  '粗',  '粘',  '粥',  '粮',  '粹',  '精',  '糊',  '糕',  '糖',  '糟',  '系',  '紊',  '素',  '索',  '紧',  '紫',  '累',  '繁',  '纠',  '红',  '纤',  '约',  '级',  '纪',  '纬',  '纯',  '纲',  '纳',  '纵',  '纷',  '纸',  '纹',  '纺',  '纽',  '线',  '练',  '组',  '绅',  '细',  '织',  '终',  '绍',  '绎',  '经',  '绑',  '绒',  '结',  '绕',  '绘',  '给',  '络',  '绝',  '统',  '绣',  '继',  '绩',  '绪',  '续',  '绳',  '维',  '绸',  '综',  '绿',  '缀',  '缓',  '缔',  '编',  '缘',  '缚',  '缝',  '缠',  '缩',  '缴',  '缺',  '罐',  '网',  '罕',  '罚',  '罢',  '罩',  '罪',  '置',  '署',  '羊',  '美',  '羞',  '羡',  '群',  '羽',  '翅',  '翔',  '翘',  '翻',  '翼',  '耀',  '老',  '考',  '者',  '而',  '耍',  '耐',  '耕',  '耗',  '耳',  '耸',  '耻',  '耽',  '聊',  '聋',  '职',  '联',  '聘',  '聚',  '聪',  '肃',  '肆',  '肉',  '肌',  '肖',  '肚',  '股',  '肢',  '肤',  '肥',  '肩',  '肪',  '肯',  '育',  '肴',  '肺',  '肿',  '胀',  '胁',  '胃',  '胆',  '背',  '胎',  '胖',  '胜',  '胞',  '胡',  '胳',  '胶',  '胸',  '能',  '脂',  '脆',  '脉',  '脏',  '脑',  '脖',  '脚',  '脱',  '脸',  '脾',  '腐',  '腔',  '腥',  '腮',  '腰',  '腹',  '腻',  '腾',  '腿',  '膀',  '膊',  '膏',  '膛',  '膜',  '膝',  '膨',  '臂',  '臣',  '自',  '臭',  '至',  '致',  '舅',  '舆',  '舌',  '舍',  '舒',  '舔',  '舞',  '舟',  '航',  '般',  '舰',  '舱',  '舶',  '船',  '艇',  '艘',  '良',  '艰',  '色',  '艳',  '艺',  '节',  '芒',  '芦',  '花',  '芽',  '苍',  '苏',  '苗',  '苟',  '若',  '苦',  '英',  '苹',  '茂',  '范',  '茎',  '茫',  '茶',  '草',  '荐',  '荒',  '荡',  '荣',  '荧',  '药',  '莫',  '获',  '菌',  '菜',  '萄',  '萌',  '营',  '落',  '著',  '葡',  '董',  '葫',  '葬',  '蒂',  '蒙',  '蒸',  '蓄',  '蓝',  '蓬',  '蔑',  '蔓',  '蔬',  '蔼',  '蔽',  '蕉',  '蕴',  '薄',  '薪',  '藏',  '虎',  '虏',  '虐',  '虑',  '虚',  '虫',  '虹',  '虽',  '蚀',  '蛇',  '蛋',  '蛮',  '蜂',  '蜜',  '蜡',  '蝴',  '蝶',  '融',  '螺',  '蠢',  '血',  '衅',  '行',  '衍',  '衔',  '街',  '衡',  '衣',  '补',  '表',  '衫',  '衬',  '衰',  '衷',  '袋',  '袍',  '袖',  '袜',  '被',  '袭',  '袱',  '裁',  '裂',  '装',  '裔',  '裕',  '裙',  '裤',  '裳',  '裹',  '西',  '要',  '覆',  '见',  '观',  '规',  '觅',  '视',  '览',  '觉',  '角',  '解',  '触',  '言',  '誉',  '誓',  '警',  '譬',  '计',  '订',  '认',  '讥',  '讨',  '让',  '训',  '议',  '讯',  '记',  '讲',  '讳',  '讶',  '许',  '论',  '讼',  '讽',  '设',  '访',  '证',  '评',  '识',  '诈',  '诉',  '诊',  '词',  '译',  '试',  '诗',  '诚',  '话',  '诞',  '询',  '该',  '详',  '诧',  '诫',  '诬',  '语',  '误',  '诱',  '说',  '诵',  '请',  '诸',  '诺',  '读',  '诽',  '课',  '谁',  '调',  '谅',  '谈',  '谊',  '谋',  '谍',  '谎',  '谐',  '谓',  '谜',  '谢',  '谣',  '谤',  '谦',  '谨',  '谬',  '谱',  '谴',  '谷',  '豆',  '象',  '豪',  '豫',  '貌',  '贝',  '负',  '贡',  '财',  '责',  '贤',  '败',  '账',  '货',  '质',  '贩',  '贪',  '贫',  '贬',  '购',  '贯',  '贴',  '贵',  '贷',  '贸',  '费',  '贺',  '贼',  '贿',  '赁',  '赂',  '资',  '赋',  '赌',  '赏',  '赔',  '赖',  '赚',  '赛',  '赞',  '赠',  '赢',  '赤',  '走',  '赴',  '赶',  '起',  '趁',  '超',  '越',  '趋',  '趟',  '趣',  '足',  '趴',  '跃',  '跌',  '跑',  '距',  '跟',  '跨',  '跪',  '路',  '跳',  '践',  '踊',  '踌',  '踏',  '踢',  '踩',  '踪',  '蹈',  '蹋',  '蹦',  '蹬',  '蹲',  '躁',  '躇',  '身',  '躬',  '躲',  '躺',  '车',  '轨',  '转',  '轮',  '软',  '轰',  '轻',  '载',  '较',  '辅',  '辆',  '辈',  '辉',  '辐',  '辑',  '输',  '辖',  '辙',  '辛',  '辜',  '辞',  '辟',  '辣',  '辨',  '辩',  '辫',  '辰',  '辱',  '边',  '辽',  '达',  '迁',  '迄',  '迅',  '过',  '迈',  '迎',  '运',  '近',  '返',  '还',  '这',  '进',  '远',  '违',  '连',  '迟',  '迫',  '述',  '迷',  '迸',  '迹',  '追',  '退',  '送',  '适',  '逃',  '选',  '逊',  '透',  '逐',  '递',  '途',  '逗',  '通',  '逛',  '逝',  '速',  '造',  '逢',  '逮',  '逻',  '逼',  '遇',  '遍',  '遏',  '道',  '遗',  '遣',  '遥',  '遭',  '遮',  '遵',  '避',  '邀',  '那',  '邮',  '邻',  '郁',  '郊',  '郎',  '郑',  '部',  '都',  '鄙',  '酌',  '配',  '酒',  '酗',  '酝',  '酬',  '酱',  '酷',  '酸',  '酿',  '醉',  '醋',  '醒',  '采',  '释',  '里',  '重',  '野',  '量',  '金',  '鉴',  '针',  '钉',  '钓',  '钞',  '钟',  '钢',  '钥',  '钦',  '钩',  '钱',  '钻',  '铁',  '铃',  '铅',  '铜',  '铭',  '银',  '铸',  '铺',  '链',  '销',  '锁',  '锅',  '锈',  '锋',  '锐',  '错',  '锤',  '锦',  '键',  '锲',  '锻',  '镇',  '镜',  '镶',  '长',  '门',  '闪',  '闭',  '问',  '闯',  '闲',  '间',  '闷',  '闹',  '闻',  '阂',  '阅',  '阐',  '阔',  '队',  '防',  '阳',  '阴',  '阵',  '阶',  '阻',  '阿',  '附',  '际',  '陆',  '陈',  '陋',  '陌',  '降',  '限',  '陡',  '院',  '除',  '险',  '陪',  '陵',  '陶',  '陷',  '隆',  '随',  '隐',  '隔',  '隘',  '隙',  '障',  '隧',  '隶',  '难',  '雄',  '雅',  '集',  '雇',  '雌',  '雕',  '雨',  '雪',  '零',  '雷',  '雹',  '雾',  '需',  '震',  '霉',  '霍',  '霜',  '霞',  '露',  '霸',  '青',  '静',  '非',  '靠',  '面',  '革',  '鞋',  '鞠',  '鞭',  '韧',  '音',  '页',  '顶',  '项',  '顺',  '须',  '顽',  '顾',  '顿',  '颁',  '颂',  '预',  '领',  '颇',  '颈',  '频',  '颖',  '颗',  '题',  '颜',  '额',  '颠',  '颤',  '风',  '飘',  '飙',  '飞',  '食',  '餐',  '饥',  '饪',  '饭',  '饮',  '饰',  '饱',  '饲',  '饶',  '饺',  '饼',  '饿',  '馅',  '馆',  '馈',  '馋',  '馒',  '首',  '香',  '马',  '驰',  '驱',  '驳',  '驶',  '驻',  '驾',  '骂',  '骄',  '验',  '骑',  '骗',  '骚',  '骤',  '骨',  '高',  '髦',  '鬼',  '魂',  '魄',  '魅',  '魔',  '鱼',  '鲁',  '鲜',  '鸟',  '鸡',  '鸣',  '鸭',  '鸽',  '麦',  '麻',  '黄',  '黎',  '黑',  '默',  '鼓',  '鼠',  '鼻',  '齐',  '齿',  '龄',  '龙']

trad = ['一', '丁', '七', '丈', '三', '上', '下', '不', '丐', '且', '世', '丘', '丙', '丟', '並', '中', '串', '丸', '主', '久', '之', '乎', '乏', '乒', '乓', '乖', '乘', '乙', '九', '乞', '也', '乳', '亂', '了', '予', '事', '二', '于', '互', '五', '井', '些', '亞', '亡', '交', '亦', '享', '京', '亭', '亮', '人', '什', '仁', '仇', '今', '介', '仍', '仔', '他', '仗', '付', '仙', '代', '令', '以', '仰', '件', '任', '份', '仿', '企', '伍', '伏', '伐', '休', '伯', '估', '伴', '伶', '伸', '伺', '似', '但', '位', '低', '住', '何', '余', '佛', '作', '你', '佩', '佳', '使', '侃', '侄', '來', '侈', '例', '供', '依', '侮', '侵', '侶', '便', '促', '俊', '俐', '俗', '俘', '保', '俠', '信', '修', '俯', '俱', '倆', '倉', '個', '倍', '們', '倒', '倔', '倘', '候', '借', '倡', '倦', '倫', '值', '假', '偉', '偏', '做', '停', '健', '側', '偵', '偶', '偷', '傅', '傍', '傑', '傘', '備', '催', '傭', '傲', '傳', '債', '傷', '傻', '傾', '僅', '像', '僑', '僞', '僥', '僵', '價', '僻', '儀', '億', '儉', '儒', '償', '優', '儲', '允', '元', '兄', '充', '兆', '先', '光', '克', '兌', '免', '兒', '兔', '兜', '兢', '入', '內', '全', '兩', '八', '公', '六', '共', '兵', '其', '具', '典', '兼', '冊', '再', '冒', '冠', '冤', '冬', '冰', '冷', '准', '凍', '凝', '凡', '凶', '凸', '凹', '出', '刀', '分', '切', '刊', '刑', '列', '初', '判', '別', '利', '刪', '刮', '到', '制', '刷', '券', '刹', '刺', '刻', '則', '削', '前', '剔', '剖', '剛', '剝', '剩', '剪', '副', '割', '創', '劃', '劇', '劈', '劍', '劑', '力', '功', '加', '劣', '助', '努', '劫', '勁', '勃', '勇', '勉', '動', '勘', '務', '勝', '勞', '勢', '勤', '勵', '勸', '勺', '勻', '勾', '勿', '包', '匆', '化', '北', '匙', '匹', '區', '十', '千', '升', '午', '半', '卑', '卓', '協', '南', '博', '占', '卡', '印', '危', '即', '卷', '卸', '卻', '厘', '厚', '原', '厭', '厲', '去', '參', '又', '叉', '及', '友', '反', '叔', '取', '受', '叛', '叢', '口', '古', '句', '另', '叨', '只', '叫', '召', '叭', '叮', '可', '台', '史', '右', '司', '叼', '吃', '各', '合', '吉', '吊', '同', '名', '后', '吐', '向', '君', '吝', '吞', '吟', '否', '吧', '吩', '含', '吵', '吸', '吹', '吻', '吼', '呀', '呆', '呈', '告', '呢', '周', '味', '呵', '呻', '呼', '命', '咀', '咋', '和', '咐', '咖', '咨', '咬', '咱', '咳', '咽', '哀', '品', '哄', '哆', '哇', '哈', '哎', '員', '哥', '哦', '哨', '哪', '哭', '哲', '哺', '哼', '唆', '唇', '唉', '唐', '唠', '售', '唯', '唱', '唾', '啃', '商', '啊', '問', '啓', '啞', '啡', '啤', '啥', '啦', '啬', '啰', '喂', '善', '喇', '喉', '喊', '喘', '喚', '喜', '喝', '喧', '喪', '單', '喻', '嗅', '嗎', '嗓', '嗦', '嗨', '嗯', '嗽', '嘈', '嘉', '嘔', '嘗', '嘛', '嘩', '嘯', '嘲', '嘴', '嘿', '器', '噪', '噴', '噸', '嚇', '嚏', '嚨', '嚴', '嚷', '嚼', '囑', '四', '回', '因', '困', '固', '圈', '國', '圍', '園', '圓', '圖', '團', '土', '在', '地', '圾', '址', '均', '坐', '坑', '坡', '坦', '垂', '垃', '型', '埋', '城', '域', '執', '培', '基', '堂', '堅', '堆', '堡', '堤', '堪', '報', '場', '堵', '塊', '塌', '塑', '塔', '塗', '塘', '塞', '填', '塵', '境', '墅', '墊', '墓', '墜', '增', '墟', '墨', '墮', '墳', '壁', '壇', '壓', '壞', '壟', '壤', '壩', '士', '壯', '壺', '壽', '夏', '夕', '外', '多', '夜', '夠', '夢', '夥', '大', '天', '太', '夫', '央', '失', '夾', '奇', '奈', '奉', '奏', '奔', '套', '奠', '奢', '奧', '奪', '奮', '女', '奴', '奶', '她', '好', '如', '妄', '妒', '妙', '妝', '妥', '妨', '妹', '妻', '姆', '始', '姐', '姑', '姓', '委', '姥', '姨', '姻', '姿', '威', '娃', '娘', '娛', '娶', '婆', '婚', '婦', '婪', '媒', '媳', '媽', '嫁', '嫂', '嫉', '嫌', '嫩', '嬌', '嬰', '子', '孔', '孕', '字', '存', '孝', '季', '孤', '孩', '孫', '學', '它', '宅', '宇', '守', '安', '完', '宏', '宗', '官', '宙', '定', '宜', '客', '宣', '室', '宮', '宰', '害', '宴', '宵', '家', '容', '宿', '寂', '寄', '密', '富', '寒', '寓', '寞', '察', '寢', '實', '審', '寫', '寬', '寵', '寶', '寸', '寺', '封', '射', '將', '專', '尊', '尋', '對', '導', '小', '少', '尖', '尚', '尤', '尬', '就', '尴', '尺', '尾', '局', '屁', '居', '屆', '屈', '屋', '屍', '屏', '屑', '展', '屜', '屢', '層', '履', '屬', '山', '岔', '岩', '岸', '峭', '峰', '島', '峻', '峽', '崇', '崖', '崗', '崩', '嵌', '嶄', '嶼', '嶽', '川', '州', '巡', '巢', '工', '左', '巧', '巨', '差', '己', '已', '巴', '巷', '巾', '市', '布', '帆', '希', '帖', '帝', '帥', '師', '席', '帳', '帶', '常', '帽', '幅', '幕', '幟', '幢', '幣', '幫', '干', '平', '年', '幸', '幹', '幻', '幼', '幽', '幾', '庇', '床', '序', '底', '店', '府', '度', '座', '庫', '庭', '康', '庸', '廁', '廂', '廈', '廉', '廊', '廓', '廚', '廟', '廠', '廢', '廣', '廳', '延', '建', '弄', '弊', '式', '引', '弟', '弦', '弱', '張', '強', '彈', '彌', '彎', '彙', '形', '彩', '彰', '影', '役', '彼', '往', '征', '待', '很', '徊', '律', '後', '徑', '徒', '得', '徘', '徙', '從', '復', '循', '微', '德', '徹', '心', '必', '忌', '忍', '志', '忘', '忙', '忠', '快', '念', '忽', '怎', '怒', '怕', '怖', '思', '怠', '急', '性', '怨', '怪', '怯', '恍', '恐', '恒', '恕', '恢', '恥', '恨', '恩', '恭', '息', '恰', '悄', '悅', '悉', '悔', '悟', '悠', '患', '您', '悲', '悶', '悼', '情', '惋', '惑', '惕', '惜', '惠', '惡', '惦', '惰', '惱', '想', '惹', '愁', '愈', '愉', '意', '愚', '愛', '感', '愣', '愧', '慈', '態', '慌', '慎', '慕', '慘', '慚', '慢', '慣', '慧', '慨', '慮', '慰', '慶', '慷', '憂', '憊', '憋', '憐', '憑', '憚', '憤', '憲', '憶', '憾', '懂', '懇', '應', '懲', '懶', '懷', '懸', '懼', '戀', '成', '我', '戒', '或', '戚', '截', '戰', '戲', '戴', '戶', '房', '所', '扁', '扇', '手', '才', '扒', '打', '扔', '托', '扛', '扣', '扭', '扮', '扯', '扶', '批', '找', '承', '技', '抄', '把', '抑', '抒', '抓', '投', '抖', '抗', '折', '抛', '披', '抱', '抵', '抹', '押', '抽', '拄', '拆', '拉', '拌', '拍', '拐', '拒', '拓', '拔', '拖', '拘', '拙', '招', '拜', '括', '拳', '拼', '拽', '拾', '拿', '持', '挂', '指', '按', '挎', '挑', '挖', '挨', '挪', '挫', '振', '挺', '挽', '捆', '捉', '捍', '捎', '捏', '捐', '捕', '捧', '捷', '掀', '掃', '授', '掉', '掌', '掏', '掐', '排', '掘', '掙', '掠', '探', '接', '控', '推', '掩', '措', '掰', '揀', '揉', '揍', '描', '提', '插', '揚', '換', '握', '揭', '揮', '援', '損', '搏', '搓', '搖', '搗', '搜', '搞', '搬', '搭', '搶', '摔', '摘', '摟', '摧', '摩', '摯', '摸', '撇', '撈', '撐', '撒', '撓', '撕', '撞', '撤', '撥', '撫', '播', '撲', '撼', '撿', '擁', '擅', '擇', '擊', '擋', '操', '擎', '擔', '據', '擠', '擡', '擦', '擬', '擰', '擱', '擲', '擴', '擺', '擾', '攀', '攏', '攔', '攙', '攜', '攝', '攢', '攤', '攪', '支', '收', '改', '攻', '放', '政', '故', '效', '敏', '救', '敗', '敘', '教', '敞', '敢', '散', '敬', '敲', '整', '敵', '敷', '數', '文', '斑', '料', '斜', '斟', '斤', '斥', '斬', '斯', '新', '斷', '方', '於', '施', '旁', '旅', '旋', '族', '旗', '既', '日', '旦', '旨', '早', '旬', '旱', '旺', '昂', '昆', '昌', '明', '昏', '易', '昔', '星', '映', '春', '昧', '昨', '是', '時', '晃', '晉', '晚', '晝', '晤', '晨', '普', '景', '晰', '晴', '晶', '智', '晾', '暄', '暈', '暑', '暖', '暗', '暢', '暧', '暫', '暴', '曆', '曉', '曝', '曠', '曬', '曲', '更', '書', '曾', '替', '最', '會', '月', '有', '朋', '服', '朗', '望', '朝', '期', '木', '未', '末', '本', '朵', '朽', '杆', '李', '材', '村', '杖', '杜', '束', '杠', '杯', '東', '松', '板', '枉', '析', '枕', '林', '枚', '果', '枝', '枯', '架', '某', '染', '柔', '查', '柬', '柱', '柴', '柿', '校', '株', '核', '根', '格', '栽', '桃', '框', '案', '桌', '桑', '桔', '桶', '梁', '條', '梢', '梨', '梯', '械', '梳', '棄', '棉', '棋', '棍', '棒', '棕', '棟', '森', '棵', '椅', '植', '椎', '椒', '楚', '業', '極', '概', '榜', '榨', '榮', '構', '槍', '槳', '樂', '樓', '標', '模', '樣', '樸', '樹', '橋', '橙', '機', '橡', '橢', '橫', '檔', '檢', '櫃', '欄', '權', '欠', '次', '欣', '欲', '欺', '欽', '款', '歇', '歉', '歌', '歎', '歐', '歡', '止', '正', '此', '步', '武', '歧', '歪', '歲', '歷', '歸', '歹', '死', '殃', '殊', '殖', '殘', '段', '殺', '殼', '殿', '毀', '毅', '毆', '母', '每', '毒', '比', '毛', '毫', '毯', '氏', '民', '氓', '氛', '氣', '氧', '水', '永', '汁', '求', '汗', '汙', '江', '池', '汰', '決', '汽', '沃', '沈', '沐', '沒', '沖', '沙', '沛', '沫', '沮', '河', '沸', '油', '治', '沼', '沾', '沿', '況', '泄', '泉', '泊', '泌', '法', '泛', '泡', '波', '泣', '泥', '注', '泰', '泳', '洋', '洗', '洞', '津', '洪', '洲', '洶', '活', '洽', '派', '流', '浏', '浪', '浮', '浴', '海', '浸', '消', '涉', '涕', '涮', '液', '涵', '涼', '淆', '淋', '淒', '淘', '淚', '淡', '淨', '淩', '深', '混', '淹', '淺', '添', '清', '減', '渠', '渡', '渣', '測', '港', '渴', '游', '渺', '渾', '湊', '湖', '湧', '湯', '溉', '源', '溜', '溝', '溪', '溫', '溶', '滄', '滅', '滋', '滑', '滔', '滯', '滲', '滴', '滾', '滿', '漁', '漂', '漆', '漏', '演', '漠', '漢', '漫', '漲', '漸', '潇', '潑', '潔', '潛', '潤', '潮', '潰', '澀', '澄', '澆', '澈', '澡', '澤', '澱', '激', '濁', '濃', '濕', '濟', '濤', '濫', '濱', '濺', '濾', '瀉', '瀑', '瀕', '灌', '灑', '灘', '灣', '火', '灰', '災', '炊', '炎', '炒', '炫', '炭', '炮', '炸', '為', '烈', '烏', '烘', '烤', '烹', '無', '焦', '焰', '然', '煉', '煌', '煎', '煙', '煤', '照', '煩', '煮', '熄', '熊', '熏', '熟', '熨', '熬', '熱', '燃', '燈', '燒', '燙', '營', '燥', '燦', '燭', '爆', '爍', '爐', '爛', '爬', '爭', '爲', '父', '爸', '爺', '爽', '爾', '牆', '片', '版', '牌', '牙', '牛', '牢', '牧', '物', '牲', '特', '牽', '犧', '犬', '犯', '狀', '狂', '狗', '狠', '狡', '狹', '狼', '狽', '猛', '猜', '猴', '猶', '猾', '獄', '獅', '獎', '獨', '獲', '獵', '獸', '獻', '率', '玉', '王', '玩', '玻', '珍', '珠', '班', '現', '球', '理', '琢', '琴', '璃', '環', '瓜', '瓣', '瓦', '瓶', '瓷', '甘', '甚', '甜', '生', '産', '用', '甩', '甭', '甯', '田', '由', '甲', '申', '男', '界', '畏', '畔', '留', '畜', '畢', '略', '番', '畫', '異', '當', '疆', '疇', '疊', '疏', '疑', '疙', '疤', '疫', '疲', '疼', '疾', '病', '症', '痕', '痛', '痹', '瘋', '瘓', '瘤', '瘦', '瘩', '瘸', '瘾', '療', '癌', '癢', '癱', '登', '發', '白', '百', '皂', '的', '皆', '皇', '皮', '皺', '盆', '盈', '益', '盒', '盛', '盜', '盟', '盡', '監', '盤', '目', '盯', '盲', '直', '相', '盼', '盾', '省', '眉', '看', '真', '眠', '眨', '眯', '眶', '眼', '睛', '睜', '睡', '督', '睦', '睬', '睹', '瞄', '瞎', '瞞', '瞧', '瞪', '瞬', '瞻', '矚', '矛', '知', '矩', '短', '矮', '石', '砍', '研', '破', '砸', '硬', '碌', '碎', '碑', '碗', '碩', '碰', '碳', '確', '碼', '磁', '磅', '磋', '磕', '磚', '磨', '礎', '礙', '礦', '示', '社', '祖', '祝', '神', '祥', '票', '禁', '禍', '福', '禦', '禮', '禽', '禿', '秀', '私', '秋', '科', '秒', '秘', '租', '秤', '秩', '移', '稀', '稅', '程', '稍', '稚', '稠', '種', '稱', '稻', '稼', '稿', '積', '穎', '穩', '穴', '究', '空', '穿', '突', '窄', '窗', '窩', '窮', '竄', '竅', '竈', '竊', '立', '站', '竟', '章', '童', '竭', '端', '競', '竹', '笑', '符', '笨', '第', '筆', '等', '筋', '筐', '筒', '答', '策', '筷', '算', '管', '箭', '箱', '節', '範', '篇', '築', '篩', '篷', '簡', '簸', '簽', '簾', '籃', '籌', '籍', '籠', '籲', '米', '粉', '粒', '粗', '粘', '粥', '粹', '精', '糊', '糕', '糖', '糙', '糟', '糧', '系', '糾', '紀', '約', '紅', '紊', '紋', '納', '紐', '純', '紙', '級', '紛', '素', '紡', '索', '紫', '紮', '累', '細', '紳', '紹', '終', '組', '結', '絕', '絡', '給', '絨', '統', '絲', '綁', '經', '綜', '綠', '綢', '維', '綱', '網', '綴', '緊', '緒', '線', '緝', '締', '緣', '編', '緩', '緯', '練', '縛', '縣', '縫', '縮', '縱', '總', '績', '繁', '織', '繞', '繡', '繩', '繪', '繳', '繹', '繼', '續', '纏', '纖', '缺', '罐', '罕', '罩', '罪', '置', '罰', '署', '罵', '罷', '羊', '美', '羞', '群', '羨', '義', '羽', '翅', '習', '翔', '翹', '翻', '翼', '耀', '老', '考', '者', '而', '耍', '耐', '耕', '耗', '耳', '耽', '聊', '聖', '聘', '聚', '聞', '聯', '聰', '聲', '聳', '職', '聽', '聾', '肅', '肆', '肉', '肌', '肖', '肚', '股', '肢', '肥', '肩', '肪', '肯', '育', '肴', '肺', '胃', '背', '胎', '胖', '胞', '胡', '胳', '胸', '能', '脂', '脅', '脆', '脈', '脖', '脫', '脹', '脾', '腐', '腔', '腥', '腦', '腫', '腰', '腳', '腸', '腹', '腿', '膀', '膊', '膏', '膚', '膛', '膜', '膝', '膠', '膨', '膩', '膽', '臂', '臉', '臣', '臥', '臨', '自', '臭', '至', '致', '舅', '與', '興', '舉', '舊', '舌', '舍', '舒', '舔', '舞', '舟', '航', '般', '舶', '船', '艇', '艘', '艙', '艦', '良', '艱', '色', '芒', '花', '芽', '苗', '苟', '若', '苦', '英', '茂', '茫', '茶', '草', '荒', '莊', '莖', '莫', '菌', '菜', '華', '萄', '萌', '萎', '萬', '落', '葉', '著', '葡', '董', '葬', '葷', '蒂', '蒙', '蒸', '蒼', '蓄', '蓋', '蓬', '蔑', '蔓', '蔚', '蔬', '蔽', '蕉', '蕩', '蕾', '薄', '薦', '薪', '藍', '藏', '藐', '藝', '藥', '藹', '蘇', '蘊', '蘋', '虎', '虐', '處', '虛', '虜', '號', '虧', '虹', '蛇', '蛋', '蜂', '蜜', '蝕', '蝴', '蝶', '融', '螞', '蟲', '蟻', '蠟', '蠢', '蠻', '血', '衆', '行', '衍', '術', '街', '衛', '衡', '衣', '表', '衫', '衰', '衷', '袋', '袍', '袖', '被', '袱', '裁', '裂', '裏', '裔', '裕', '裙', '補', '裝', '裡', '裳', '裹', '複', '褲', '襪', '襯', '襲', '西', '要', '覆', '見', '規', '覓', '視', '親', '覺', '覽', '觀', '角', '解', '觸', '言', '訂', '計', '訊', '討', '訓', '記', '訝', '訟', '訪', '設', '許', '訴', '診', '詐', '評', '詞', '詢', '試', '詩', '詫', '話', '該', '詳', '誇', '認', '誓', '誕', '誘', '語', '誠', '誡', '誣', '誤', '誦', '說', '誰', '課', '誹', '誼', '調', '談', '請', '諒', '論', '諜', '諧', '諱', '諷', '諸', '諾', '謀', '謂', '謊', '謎', '謗', '謙', '講', '謝', '謠', '謬', '謹', '證', '譏', '識', '譜', '警', '譬', '譯', '議', '譴', '護', '譽', '讀', '變', '讓', '谷', '豆', '豈', '豎', '豐', '豔', '象', '豪', '豫', '豬', '貌', '貓', '貝', '負', '財', '貢', '貧', '貨', '販', '貪', '貫', '責', '貴', '貶', '買', '貸', '費', '貼', '貿', '賀', '賂', '賃', '賄', '資', '賊', '賓', '賞', '賠', '賢', '賣', '賦', '質', '賬', '賭', '賴', '賺', '購', '賽', '贈', '贊', '贏', '赤', '走', '赴', '起', '趁', '超', '越', '趕', '趟', '趣', '趨', '足', '趴', '跌', '跑', '距', '跟', '跨', '跪', '路', '跳', '踏', '踐', '踢', '踩', '踴', '蹈', '蹋', '蹤', '蹦', '蹬', '蹲', '躁', '躍', '身', '躬', '躲', '躺', '車', '軌', '軍', '軟', '較', '載', '輔', '輕', '輛', '輝', '輩', '輪', '輯', '輸', '輻', '輿', '轄', '轅', '轉', '轍', '轟', '辛', '辜', '辟', '辣', '辦', '辨', '辭', '辮', '辯', '辰', '辱', '農', '迄', '迅', '迎', '近', '返', '迫', '述', '迷', '迸', '迹', '追', '退', '送', '逃', '逆', '透', '逐', '途', '逗', '這', '通', '逛', '逝', '速', '造', '逢', '連', '逮', '進', '逼', '遇', '遊', '運', '遍', '過', '遏', '道', '達', '違', '遙', '遜', '遞', '遠', '遣', '適', '遭', '遮', '遲', '遵', '遷', '選', '遺', '遼', '避', '邀', '邁', '還', '邊', '邏', '那', '郁', '郊', '郎', '部', '郵', '都', '鄉', '鄙', '鄭', '鄰', '酌', '配', '酒', '酗', '酬', '酷', '酸', '醉', '醋', '醒', '醜', '醞', '醫', '醬', '釀', '釁', '采', '釋', '重', '野', '量', '金', '釘', '針', '釣', '鈍', '鈎', '鈔', '鈣', '鈴', '鉛', '銀', '銅', '銘', '銜', '銳', '銷', '鋒', '鋪', '鋼', '錄', '錘', '錢', '錦', '錯', '鍋', '鍛', '鍵', '鎖', '鎮', '鏈', '鏡', '鏽', '鐘', '鐵', '鑄', '鑒', '鑰', '鑲', '鑽', '锲', '長', '門', '閃', '閉', '開', '閑', '間', '閡', '閱', '闊', '闖', '關', '闡', '阱', '防', '阻', '阿', '附', '陋', '陌', '降', '限', '陡', '院', '陣', '除', '陪', '陰', '陳', '陵', '陶', '陷', '陸', '陽', '隆', '隊', '階', '隔', '隘', '隙', '際', '障', '隧', '隨', '險', '隱', '隸', '隻', '雀', '雄', '雅', '集', '雇', '雌', '雕', '雖', '雙', '雜', '雞', '離', '難', '雨', '雪', '雲', '零', '雷', '雹', '電', '需', '震', '霍', '霜', '霞', '霧', '露', '霸', '靈', '青', '靜', '非', '靠', '面', '革', '鞋', '鞏', '鞠', '鞭', '韌', '音', '響', '頁', '頂', '項', '順', '須', '頌', '預', '頑', '頒', '頓', '頗', '領', '頭', '頸', '頻', '顆', '題', '額', '顏', '願', '顛', '類', '顧', '顫', '顯', '風', '飄', '飛', '食', '飯', '飲', '飼', '飽', '飾', '餃', '餅', '養', '餐', '餓', '餡', '館', '饅', '饋', '饑', '饒', '饞', '饪', '首', '香', '馬', '馳', '駁', '駐', '駕', '駛', '騎', '騙', '騰', '騷', '驅', '驕', '驗', '驚', '驟', '骨', '髒', '體', '高', '髦', '鬥', '鬧', '鬼', '魂', '魄', '魅', '魔', '魚', '魯', '鮮', '鳥', '鳴', '鴉', '鴨', '鴿', '鹹', '鹽', '麗', '麥', '麻', '麼', '黃', '黎', '黑', '默', '點', '黨', '黴', '鼓', '鼠', '鼻', '齊', '齒', '齡', '龍', '龐']