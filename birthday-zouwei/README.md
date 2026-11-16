# 邹惟 · 十九岁生日快乐（网页）

一个纯静态网页：一张照片一页，首页点按钮进各自的照片页。**不联网、不依赖任何框架**，双击 `index.html` 就能看。

## 怎么打开

- 双击 `index.html`（或 `生日主页.html`，同一个内容的副本，文件名好认一点）
- 想发给别人：整个 `birthday-zouwei` 文件夹压缩成 zip 发过去，对方解压后点开就行

## 有哪些页面

| 文件 | 内容 |
|---|---|
| `index.html` / `生日主页.html` | 首页：星空 + 「邹惟 生日快乐 19」+ 九个照片入口 + 放烟花按钮 |
| `canteen.html` | 01 干饭现场（食堂吃肉串） |
| `classmates.html` | 02 教室里的合影（和两个同学自拍，比耶） |
| `classroom.html` | 03 课间的教室（教室全景） |
| `selfie.html` | 04 镜头前的小孩（Puma 近距自拍） |
| `shower.html` | 05 刚洗完头（宿舍浴室自拍） |
| `hat.html` | 06 山路上的一天（戴帽子出门） |
| `gaokao.html` | 07 高考倒计时 69（宿舍举牌子） |
| `father.html` | 08 你爸和同学（父亲的老照片） |
| `couple.html` | 09 和你在一起的人（压轴） |
| `cake.html` | 满屏生日蛋糕（首页点两下「放一朵烟花」会进来） |

每页底部有「回到起点 / 上一张 / 下一张」，最后一页的「下一张」会绕回第一页；右侧有圆点可跳。

**调整顺序**：改 `build.py` 里 `PHOTOS` 列表的顺序即可——页内编号（01、02…）、「第 N 场」、切换按钮、首页卡片全部自动重排，不用手工改序号。

## 怎么改

**改文字**：用任何文本编辑器打开 `build.py`，顶部的 `PHOTOS` 列表里就是每一页的标题、正文、引言和配色。改完在这个文件夹里跑一次：

```bash
python3 build.py
```

会重新生成全部页面（`assets/site.css`、`assets/sky.js` 也是它生成的，别单独改，会被覆盖）。

**加一张照片**：

1. 把照片拷进 `assets/photos/`，比如 `photo-4.jpg`
2. 在 `build.py` 的 `PHOTOS` 里加一条：

```python
    {
        "slug": "fourth",          # 文件名，别和已有的重名
        "file": "photo-4.jpg",
        "nav": "一句话叫法",        # 显示在按钮和图注上
        "kicker": "第四场 · 小标题",
        "title": "这一页的大标题",
        "lines": ["第一段", "第二段"],
        "quote": "一句引言",
        "accent": "#8fd1ff",       # 主色
        "accent2": "#7b6cff",      # 次色
        "glow": "rgba(143, 209, 255, .4)",
        "veil": "linear-gradient(160deg, #060f1e 0%, #0a1a33 42%, #0b0a16 100%)",
        # 竖版照片加一行："ratio": "tall"
    },
```

3. 再跑 `python3 build.py`——首页卡片、页内切换按钮、右侧圆点都会自动多一个

**给某页加做旧滤镜**：那条 `PHOTOS` 里加一行 `"filter": "sepia(.35) saturate(.9) contrast(1.05)"`，照片和首页缩略图都会变旧照片色调。

**只想改照片、不想碰代码**：直接把 `assets/photos/` 里的同名文件替换掉（`photo-canteen.jpg` 等），刷新页面即可。

## 目录结构

```
birthday-zouwei/
├── index.html / 生日主页.html   # 首页
├── canteen.html                # 第 1 页
├── classmates.html             # 第 2 页
├── classroom.html              # 第 3 页
├── selfie.html                 # 第 4 页
├── shower.html                 # 第 5 页
├── hat.html                    # 第 6 页
├── gaokao.html                 # 第 7 页
├── father.html                 # 第 8 页
├── couple.html                 # 第 9 页（压轴）
├── cake.html                   # 满屏蛋糕页
├── build.py                    # 生成脚本（改内容就改这里）
└── assets/
    ├── site.css                # 样式（由 build.py 生成）
    ├── sky.js                  # 星空 / 流星 / 烟花（由 build.py 生成）
    ├── cake.js                 # 满屏蛋糕的绘制与动画（可直接改）
    └── photos/                 # 9 张原图
```

## 烟花与蛋糕

- **首页按钮**：点一下 = 炸三朵烟花，按钮变成「再放一朵 · 点这儿看蛋糕」；再点一下 = 进入满屏蛋糕页。
- **蛋糕页**：三层蛋糕 + 5 根会晃的蜡烛（手机上 3 根），3 秒内依次长出来；底部按钮「再点一次蛋糕」会重新长一遍。
- 想改蜡烛数、出现速度：改 `assets/cake.js` 顶部的 `T`（时间轴）和 `positions`（蜡烛位置）即可。

## 适配

- 电脑、手机都自适应；手机上照片整图显示、按钮自动换行
- 系统开了「减少动态效果」时，动画会自动关掉
