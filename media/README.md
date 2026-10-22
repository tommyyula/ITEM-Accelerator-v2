# 七个 Demo 视频接入

视频在会上详版保留区域，会前简版只给业务价值总览。

- `case-2.1`：港口拖柜，详版第12页。
- `case-2.2`：WMS Dynamic Form，详版第13页。
- `case-2.3`：BO / Customer Promise，详版第14页。
- `case-2.4`：BNP → Dynamic Form → PEI，详版第17页。
- `case-2.5`：Record & Reply → CEC SOP，详版第18页。
- `case-2.6`：eSVC Small Model，详版第19页。
- `case-2.7`：CEC + Genesys AI App，详版第20页。

将 MP4 放入本目录，然后编辑 `videos.json` 的对应项：

```json
{"title":"港口拖柜","src":"media/port-demo.mp4","poster":""}
```

`poster` 可为空，也可填写封面图片的相对路径。随后在代码包根目录运行 `python3 build.py`，重新上传两个 HTML 和 `media/` 素材。默认不自动播放；视频不被 Base64 内嵌，因此接入视频后必须同时保留媒体文件或可访问的 URL。

请确认可公开范围、脱敏情况、哪些动作真实执行及哪些模拟。当前视频配置为空，不表示已经完成素材接入或审批。
