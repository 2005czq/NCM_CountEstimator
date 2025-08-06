# NCM_CountEstimator

在网易云音乐中访问其它用户主页时，**最近一周听歌排行**只展示了歌曲和它们对应的百分比，但并未直接提供播放次数。本工具用于通过分析这些百分比数据推算出最可能对应的播放次数。

## 项目依赖

- Python 3
- 第三方 Python 库 `requests`
- [NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)

## 配置说明

```json
{
    "api": "",
    "id": "",
    "MUSIC_U": ""
}
```

- `api`：NeteaseCloudMusicApi 的 API 基础地址。在你**确保账号隐私安全**的情况下，你也可以使用未知第三方部署的 API 服务，例如[这个](https://neteasecloudmusicapi-main-api.vercel.app/)，但**仍然建议自行本地部署**。
- `id`：需要查询的目标用户 ID。在网易云音乐网页端打开目标用户主页，URL 地址中的 `uid=` 后面的数字就是用户 ID。
- `MUSIC_U`：可选，进行信息抓取的登录凭证。当目标用户的听歌排行**对仅关注者可见**时，可以在[网易云音乐网页端](https://music.163.com/)登录被目标用户关注的账号，并将 Cookies 中该字段的值填入配置文件中。

## 快速开始

1.  克隆本仓库：

	```bash
	git clone https://github.com/2005czq/NCM_CountEstimator.git
	cd NCM_CountEstimator
	```

2.  安装依赖：

	```bash
	pip install -r requirements.txt
	```

3.  参考上面的配置说明在 `config.json` 中填入相关配置信息。

4.  运行程序：

	```bash
	python main.py
	```

## 注意事项

- 本人不对使用第三方部署的 NeteaseCloudMusicApi 服务可能产生的任何后果负责。请**优先选择本地部署**。
- 在最近一周听歌排行中最高播放量次数超过 100 的情况下，推算结果可能会有误差，这在算法上无法避免。

## 开源许可

本项目采用 **GNU General Public License v3.0**。详细内容请参阅 [LICENSE](./LICENSE) 文件。