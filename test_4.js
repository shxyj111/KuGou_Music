// 模拟 Canvas 2D 渲染上下文
function CanvasRenderingContext2D() {
  // ==================== 绘图属性 ====================
  // 填充颜色（默认黑色）
  this.fillStyle = "#000000";

  // 描边颜色（默认黑色）
  this.strokeStyle = "#000000";

  // 线条宽度（默认 1 像素）
  this.lineWidth = 1;

  // ==================== 基础绘图方法 ====================
  // 填充矩形（参数：x, y, width, height）
  this.fillRect = function() {
    console.log("[模拟] 填充矩形", ...arguments);
    // 实际实现可以记录调用参数或执行空操作
  };

  // 描边矩形（参数：x, y, width, height）
  this.strokeRect = function() {
    console.log("[模拟] 绘制描边矩形", ...arguments);
  };

  // ==================== 路径操作 ====================
  // 开始新路径
  this.beginPath = function() {
    console.log("[模拟] 开始新路径");
  };

  // 移动笔触（参数：x, y）
  this.moveTo = function() {
    console.log("[模拟] 移动笔触到坐标", ...arguments);
  };

  // 绘制直线（参数：x, y）
  this.lineTo = function() {
    console.log("[模拟] 绘制直线到坐标", ...arguments);
  };

  // 绘制圆弧（参数：x, y, radius, startAngle, endAngle, anticlockwise）
  this.arc = function() {
    console.log("[模拟] 绘制圆弧", ...arguments);
  };

  // 填充路径
  this.fill = function() {
    console.log("[模拟] 填充路径");
  };

  // 描边路径
  this.stroke = function() {
    console.log("[模拟] 描边路径");
  };

  // ==================== 状态管理 ====================
  // 保存当前绘图状态（颜色/变换等）
  this.save = function() {
    console.log("[模拟] 保存绘图状态");
    // 实际实现可以用栈保存当前状态
  };

  // 恢复最近保存的绘图状态
  this.restore = function() {
    console.log("[模拟] 恢复绘图状态");
    // 从状态栈中弹出并恢复
  };

  // ==================== 图像操作 ====================
  // 绘制图像（参数：image, dx, dy, dWidth, dHeight）
  this.drawImage = function() {
    console.log("[模拟] 绘制图像", arguments[0].constructor.name);
    // 可记录被绘制图像的类型（如 HTMLCanvasElement）
  };

  // ==================== 高级特性 ====================
  // 获取图像数据（返回模拟数据）
  this.getImageData = function() {
    console.log("[模拟] 获取图像数据");
    return {
      data: new Uint8ClampedArray(4 * 300 * 150) // 300x150 透明像素
    };
  };

  // 应用变换矩阵（参数：a, b, c, d, e, f）
  this.transform = function() {
    console.log("[模拟] 应用矩阵变换", ...arguments);
  };
  this.fillText = function (ele){
      console.log('毁灭吧', ele)
  }
}
canvas2d = new CanvasRenderingContext2D()
// 定义一个模拟的 HTMLCanvasElement 构造函数（可能用于测试或替换原生对象）
function HTMLCanvasElement() {
    // 定义 getContext 方法：模拟获取画布绘图上下文
    this.getContext = function (ele) {
        // 输出调试信息（中文提示可能用于特定测试场景）
        console.log('阿尔法行不行啊', ele);
        // 当请求 2D 上下文时，返回预定义的 canvas2d 对象（注意：canvas2d 需在外部定义）
        if (ele == '2d') {
            return canvas2d;
        }
    };
    // 定义 toDataURL 方法：模拟画布数据导出功能（此处仅为空实现）
    this.toDataURL = function (ele) {
        // 输出调试信息（中文提示表示该方法被调用）
        console.log('回答我，look in my eyes', ele);
    };
    // 定义非标准的 getAttributeNames 方法（注意：原生方法无参数，此处可能设计异常）
    this.getAttributeNames = function (ele) {
        // 输出调试信息（中文提示可能用于追踪调用）
        console.log('tell me; why? 世上无难事，不如早放弃', ele);
    };
    // 设置画布宽度属性（注意：拼写错误，应为 width 而非 widh，这将导致属性失效）
    this.width = 666;
    // 设置画布高度属性（正确拼写）
    this.height = 666;
    // 初始化样式对象（模拟 HTML 元素的 style 属性，用于 CSS 样式存储）
    this.style = {};
}
canvas = new HTMLCanvasElement()
document = {
    createElement:function (ele){
        console.log('阿尔法牛逼', ele)
        if (ele == 'canvas'){
            return canvas
        }
    }
}
function abc(option, callback) {
    function noListenShowDialog() {
        var mid = KgUser.getKgMid()
            , searchEngine = location.search
            , sourceid = "";
        ~searchEngine.indexOf("frombaidu") ? sourceid = 20690201 : ~searchEngine.indexOf("from_sogou") ? sourceid = 20690202 : ~searchEngine.indexOf("from_360") && (sourceid = 20690203),
        tunnelPush({
            page_id: 3e3,
            mid: mid,
            source_id: sourceid,
            hash: option.hash
        }, !0),
        _this.toggleSound();
        _this.downloadError({
            type: "current",
            handle: "play",
            text: "当前歌曲仅能试听片段，完整播放需要前往酷狗APP"
        })
    }
    var _this = this;
    if (audioName = $(".audioName"),
    $content = $(".content"),
    $blurBg = $("#blurBg"),
    defaultImg = "https://www.kugou.com/yy/static/images/play/default.jpg",
    $(".btnArea2").show(),
    (void 0 === option.img || "" == option.img || null == option.img || !option.play_url && 2 != (3 & option.privilege)) && (option.img = defaultImg),
    -1 == location.href.indexOf("song-36") && ("ie" == utility.getBrowser().type ? ($content[0].style.cssText = $content[0].style.cssText + "background-image: url('https://www.kugou.com/yy/static/images/iebg.jpg');",
    $blurBg.hide(),
    _this.resizeUI()) : ($blurBg[0].style.cssText = "background-image: url('" + replaceHttpsImg(option.img) + "');",
    $(".module-bg").css({
        "background-image": "url('" + replaceHttpsImg(option.img) + "')",
        "background-size:": "100% " + $("#blurBg").height(),
        "background-position": "left bottom"
    }))),
    option.have_album && (option.play_url || 2 == (3 & option.privilege))) {
        var albumName_a = $(".albumName a")
            , albumImg_a = $(".albumImg a")
            , barAlbumImg_a = $(".bar-albumImg a")
            , albumLink = "https://www.kugou.com/album/info/" + option.encode_album_id + "/";
        $(".albumName").show(),
        albumName_a.length > 0 ? albumName_a.text(option.album_name).attr("title", option.album_name).attr("href", albumLink) : $(".albumName").html('<span class="fl fontColor">专辑：</span><a class="fl" href="' + albumLink + '" title="' + option.album_name + '">' + option.album_name + "</a>"),
        albumImg_a.length > 0 ? (albumImg_a.attr("title", option.album_name).attr("href", albumLink),
        albumImg_a.find("img").attr("src", replaceHttpsImg(option.img))) : $(".albumImg").html('<a class="fl" target="_blank" href="' + albumLink + '"title="' + option.album_name + '"><img onerror="this.onerror=null;this.src=' + replaceHttpsImg(option.img) + '"  src=' + replaceHttpsImg(option.img) + "></a>"),
        barAlbumImg_a.length > 0 ? (barAlbumImg_a.attr("title", option.album_name).attr("href", albumLink),
        barAlbumImg_a.find("img").attr("src", replaceHttpsImg(option.img))) : $(".bar-albumImg").html('<a target="_blank" href="' + albumLink + '"title="' + option.album_name + '"><img onerror="this.onerror=null;this.src=' + replaceHttpsImg(option.img) + '" src=' + replaceHttpsImg(option.img) + "></a>")
    } else
        $(".albumName").hide(),
        $(".albumImg,.bar-albumImg").html('<img src="' + replaceHttpsImg(option.img) + '">');
    option.have_mv ? $(".btnMv").attr("href", "https://www.kugou.com/mv/" + option.e_video_id + "/").show() : $(".btnMv").hide(),
    (void 0 === option.audio_name || "" == option.audio_name || null == option.audio_name || !option.play_url && 2 != (3 & option.privilege)) && (option.audio_name = "酷狗音乐 - 就是歌多"),
    $("#songName,.audioName").html(utility.htmlEncode2(option.audio_name)).attr("title", option.audio_name),
    $("#songNameTemp:hidden").html(utility.playEncode(option.audio_name)).attr("title", option.audio_name),
    clearInterval(fanxingAdT),
    fanxingAdT = setInterval(function() {
        _this.fanxingAjax(option.audio_name)
    }, 2e4),
    _this.fanxingAjax(option.audio_name);
    var $singerName = $(".singerName")
        , singerHtml = '<span class="fontColor">歌手：</span>'
        , authors = ""
        , authorsTitle = "";
    $(option.authors).each(function(index) {
        "1" == $(this)[0].is_publish && "0" != $(this)[0].author_id && $(this)[0].e_author_id ? singerHtml += '<a target="_blank" href="https://www.kugou.com/singer/info/' + $(this)[0].e_author_id + '/" title="' + $(this)[0].author_name + '">' + $(this)[0].author_name + "</a>" : "1" == $(this)[0].is_publish && "0" != $(this)[0].author_id ? singerHtml += '<a target="_blank" href="https://www.kugou.com/singer/' + $(this)[0].author_id + '.html" title="' + $(this)[0].author_name + '">' + $(this)[0].author_name + "</a>" : singerHtml += $(this)[0].author_name,
        authors += $(this)[0].author_name + "_",
        authorsTitle += $(this)[0].author_name + "、"
    }),
    '<span class="fontColor">歌手：</span>' == singerHtml || !option.play_url && 2 != (3 & option.privilege) ? $singerName.hide() : $singerName.show().html(singerHtml).attr("title", authorsTitle);
    var rSongName = option.song_name || option.audio_name
        , rAuthor = option.author_name ? option.author_name + "_" : authors;
    if ("" != rSongName && null != rSongName && "undefined" != rSongName) {
        var rTitle = rSongName + "_" + rAuthor + "高音质在线试听_" + rSongName + "歌词|歌曲下载_酷狗音乐 ";
        document.title != rTitle && (document.title = rTitle)
    } else
        document.title = "酷狗音乐";
    option.audio_name && (_this.globalParam.songName = utility.htmlEncode2(option.audio_name)),
    audioName.width() > 430 && audioName.css({
        width: "430px",
        overflow: "hidden",
        whiteSpace: "nowrap",
        float: "left",
        textOverflow: "ellipsis"
    }),
    $(".no_song").remove();
    var word = option.lyrics.replace(/%/g, "\\")
        , word = word.replace(/\ufeff/g, "")
        , songword = word.replace(/\[(.*)\]/g, '</p><p class="ie8FontColor">').replace(/<\/p>/, "") + "</p>";
    _this.globalParam.word = word;
    var isNoScrollFlag = !1;
    if (-1 == option.lyrics.indexOf("[00:") && (isNoScrollFlag = !0,
    songword = "抱歉，该歌词暂不支持自动滑动<br/>" + option.lyrics.replace(/%/g, "\\").replace(/\n/g, "<br/>")),
    "" == option.lyrics && (songword = "还没有歌词哦"),
    option.play_url && 1 == option.is_free_part && "album" == option.store_type ? ($(".songWordContentM .jspPane").html(""),
    $(".songWordContent").jScrollPane({
        hijackInternalLinks: !0,
        animateScroll: !0,
        autoReinitialise: !0
    })) : isNoScrollFlag ? ($(".songWordContent").addClass("__displayNone"),
    $(".songWord4NoScroll").html(songword),
    $(".songWord4NoScroll").removeClass("__displayNone"),
    $(".songWord4NoScroll").animate({
        scrollTop: 0
    }, 200)) : ($(".songWord4NoScroll").addClass("__displayNone"),
    $(".songWordContent").removeClass("__displayNone"),
    $(".songWordContentM .jspPane").length > 0 ? $(".songWordContentM .jspPane").html(songword) : ($(".songWordContentM").html(songword),
    $(".songWordContent").jScrollPane({
        hijackInternalLinks: !0,
        animateScroll: !0,
        autoReinitialise: !0
    }))),
    "undefined" == typeof myAudio && null == myAudio && (myAudio = document.getElementById("myAudio")),
    _this.globalParam.song_info = option,
    option.play_url && 1 == option.is_free_part && "album" == option.store_type) {
        _this.reportErrorInfo("apiError|数专类型"),
        _this.globalParam.myAudio.pause(),
        setTimeout(function() {
            _this.globalParam.myAudio.pause()
        }, 1e3);
        var wranText = "此音乐仅限酷狗客户端播放";
        option.show_tips && (wranText = option.show_tips),
        _this.downloadError({
            type: "current",
            handle: "play",
            text: wranText
        }),
        $(".btnArea2 #openKugou").hide()
    } else if ("" == option.play_url) {
        var flag1 = option.hash && "" != option.hash && "" == option.play_url
            , wranText = "此音乐暂时不能播放";
        2 == (3 & option.privilege) && (wranText = "此音乐仅限酷狗客户端播放"),
        flag1 && _this.downloadError({
            type: "current",
            handle: "play",
            text: wranText
        }),
        $(".btnArea2 #openKugou").hide()
    } else
        1 == option.is_free_part ? (_this.globalParam.saveFreeTryListen = noListenShowDialog,
        $(".btnArea2 #openKugou").hide()) : (_this.globalParam.saveFreeTryListen = null,
        0 == $(".btnArea2 #openKugou").length ? $(".btnArea2").append('<a id="openKugou"   href="https://www.kugou.com/musiclibrary_openplan/?from=pcweb" target="_blank" style="color:rgba(255, 255, 255, 0.5);font-size: 12px;text-align: center;display: block;margin: 20px auto 0;width: 150px;"><span onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'rgba(255, 255, 255, 0.5)\'" style="text-decoration:underline;color:rgba(255, 255, 255, 0.5);">外部播放此歌曲</span>&gt;</a>') : $(".btnArea2 #openKugou").show()),
        myAudio.src = option.play_url,
        myAudio && myAudio.setAttribute && myAudio.setAttribute("data-hash", option && option.hash),
        myAudio && myAudio.setAttribute && myAudio.setAttribute("data-ecid", option && option.encode_album_audio_id),
        myAudio.load(),
        option.trans_param && option.trans_param.hash_offset && option.trans_param.hash_offset.start_ms && _this.setPositioningPlay(option.trans_param.hash_offset.start_ms / 1e3);
    callback && callback()
}

data = {
    "hash": "50AC4C92795F6907A9059A5615A1FEB6",
    "timelength": 238053,
    "filesize": 3809504,
    "audio_name": "Bye Bye Badman - 너의 파도 (你的波涛)",
    "have_album": 1,
    "album_name": "너의 파도",
    "album_id": "15653448",
    "img": "http://imge.kugou.com/stdmusic/480/20210629/20210629180712789909.jpg",
    "sizable_cover": "http://imge.kugou.com/stdmusic/{size}/20210629/20210629180712789909.jpg",
    "have_mv": 0,
    "video_id": 0,
    "author_name": "Bye Bye Badman",
    "song_name": "너의 파도 (你的波涛)",
    "lyrics": "[ti:너의 파도]\r\n[ar:바이 바이 배드맨 (Bye Bye Badman)]\r\n[al:너의 파도]\r\n[by:]\r\n[offset:0]\r\n[00:00.00]너의 파도 - Bye Bye Badman\r\n[00:02.19]词：정봉길\r\n[00:04.39]曲：바이 바이 배드맨\r\n[00:06.58]编曲：바이 바이 배드맨\r\n[00:08.78]아직 남아있을까\r\n[00:12.67]너의 기억 속의 희미해진 나\r\n[00:16.62]단지 사라질 뿐이야\r\n[00:20.48]우리 가슴속의 뜨거웠던 날\r\n[00:25.89]너의 파도 속을 헤매듯\r\n[00:29.57]숨을 쉴 수가 없어\r\n[00:33.76]서로 닿을 듯한 거리여도\r\n[00:37.60]아직 말할 순 없어\r\n[00:40.27]너에게만은 들킬 수 없는 내 맘\r\n[00:46.92]널 볼 수 없어 난\r\n[00:48.79]끝인 것 같아 다\r\n[00:51.20]아직 할 말이 남아있는데\r\n[00:54.36]너는 모르니\r\n[00:57.03]끝인 것 같아 다\r\n[00:58.82]아직 할 말이 남아있는데\r\n[01:02.38]너는 모르니\r\n[01:10.31]너는 모르니\r\n[01:20.91]아직 남아있을까\r\n[01:24.67]너의 기억 속의 희미해진 나\r\n[01:28.66]단지 사라질 뿐이야\r\n[01:32.52]우리 가슴속의 뜨거웠던 날\r\n[01:37.69]너의 파도 속을 헤매듯\r\n[01:41.59]숨을 쉴 수가 없어\r\n[01:45.76]서로 닿을 듯한 거리여도\r\n[01:49.71]아직 말할 순 없어\r\n[01:52.39]너에게만은 들킬 수 없는 내 맘\r\n[01:58.85]널 볼 수 없어 난\r\n[02:01.04]끝인 것 같아 다\r\n[02:03.01]아직 할 말이 남아있는데\r\n[02:06.33]너는 모르니\r\n[02:08.84]끝인 것 같아 다\r\n[02:11.08]아직 할 말이 남아있는데\r\n[02:14.36]너는 모르니\r\n[02:22.46]너는 모르니\r\n[02:46.85]널 볼 수 없어 난\r\n[02:55.20]미칠 것 같아 난\r\n[03:03.03]널 볼 수 없어 난\r\n[03:10.92]미칠 것 같아 난\r\n[03:18.96]널 볼 수 없어 난\r\n[03:26.90]미칠 것 같아 난\r\n[03:34.81]널 볼 수 없어 난\r\n[03:42.90]미칠 것 같아 난\r\n",
    "author_id": "190999",
    "privilege": 10,
    "privilege2": "1010",
    "play_url": "https://webfs.kugou.com/202511152344/33500aa1d7a48c293fa5b9dd33e6ca2c/v3/50ac4c92795f6907a9059a5615a1feb6/yp/p_0_960147/ap1014_us698985232_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx58782148_s3145842289.mp3",
    "authors": [
        {
            "author_id": "190999",
            "author_name": "Bye Bye Badman",
            "is_publish": "1",
            "sizable_avatar": "http://singerimg.kugou.com/uploadpic/softhead/{size}/20220315/20220315131101120.jpg",
            "e_author_id": "5QGNK72E87B6A",
            "avatar": "http://singerimg.kugou.com/uploadpic/softhead/400/20220315/20220315131101120.jpg"
        }
    ],
    "is_free_part": 1,
    "bitrate": 128,
    "recommend_album_id": 15653448,
    "store_type": "audio",
    "album_audio_id": 58782148,
    "is_publish": 1,
    "e_author_id": "5QGNK72E87B6A",
    "audio_id": "26555638",
    "has_privilege": true,
    "trans_param": {
        "hash_offset": {
            "start_byte": 0,
            "end_byte": 960147,
            "start_ms": 0,
            "end_ms": 60000,
            "offset_hash": "A965AE852C8DC4203BE203B05860D51F",
            "file_type": 0,
            "clip_hash": "5F4AA3786F28ED61E3650E8B13AF0286"
        },
        "musicpack_advance": 1,
        "pay_block_tpl": 1,
        "display": 0,
        "display_rate": 0,
        "cpy_grade": 5,
        "cpy_level": 1,
        "cid": 40164665,
        "cpy_attr0": 50347136,
        "classmap": {
            "attr0": 234881032
        },
        "hash_multitrack": "85042C8008ECB0BBBCD57ED7CC6BAE6A",
        "qualitymap": {
            "attr0": 1999683636,
            "attr1": 134217728,
            "bits": "40000007730c034"
        },
        "language": "韩语",
        "ipmap": {
            "attr0": 524288
        },
        "songname_suffix": "(你的波涛)",
        "ogg_128_hash": "4A2C9B20FFEBA0C0836C43DE849F601B",
        "ogg_128_filesize": 2922013,
        "ogg_320_hash": "707FB9081A7B69B42B0CE9C76C1D64CE",
        "ogg_320_filesize": 10433586,
        "union_cover": "http://imge.kugou.com/stdmusic/{size}/20210629/20210629180712789909.jpg"
    },
    "play_backup_url": "https://webfs.tx.kugou.com/202511152344/9811f30274636a38bfb7841042b5da0f/v3/50ac4c92795f6907a9059a5615a1feb6/yp/p_0_960147/ap1014_us698985232_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx58782148_s3145842289.mp3",
    "small_library_song": 1,
    "encode_album_id": "9bia0d4",
    "encode_album_audio_id": "yzwlg7d",
    "e_video_id": "0df"
}

var a = abc(data)
console.log(a);