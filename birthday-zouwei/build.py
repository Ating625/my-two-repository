# 邹惟 19 岁生日网站 · 生成脚本
#
# 一次性生成 1 个首页 + 3 个照片页。照片已在 assets/photos/ 下：
#   photo-canteen.jpg  食堂吃肉串
#   photo-69.jpg       宿舍举「69」牌子
#   photo-selfie.jpg   Puma 近距自拍
#
# 用法：python3 build.py
# 想改文字：改下面 PHOTOS 里的字段再重跑；想加照片：加一条 dict + 把图拷进 assets/photos/。

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
NAME = "邹惟"
AGE = 19

# 场次编号：按 PHOTOS 里出现的位置自动给，和手工写死告别
CN_NUM = {i: n for i, n in enumerate(
    ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
     "十一", "十二"], start=1)}

PHOTOS = [
    {
        "slug": "canteen",
        "file": "photo-canteen.jpg",
        "nav": "干饭现场",
        "kicker": "干饭现场",
        "title": "先把饭吃饱",
        "lines": [
            "高中食堂里最真实的快乐，是牙签举到嘴边、眼睛都没来得及眨。",
            "愿你往后每一顿饭都吃得这么香，每一件事都这么有劲。",
        ],
        "quote": "人生头等大事：先吃饱。",
        "accent": "#f0a94a",
        "accent2": "#ff7a45",
        "glow": "rgba(240, 169, 74, .45)",
        "veil": "linear-gradient(160deg, #1a1208 0%, #241507 42%, #0b0a16 100%)",
    },
    {
        "slug": "classmates",
        "file": "photo-classmates.jpg",
        "nav": "教室里的合影",
        "kicker": "教室里的合影",
        "title": "挤进一个镜头",
        "lines": [
            "蓝窗帘拉开一半，后墙的红横幅写着「努力造就」，三个人硬挤进同一个取景框：你在后头比了个耶，笑得最开。",
            "很多年后你未必记得每道题的解法，但会记得谁在你旁边、谁先笑了场。",
        ],
        "quote": "长大以后，最想念的往往是这几分钟的课间。",
        "accent": "#8fe3c8",
        "accent2": "#4fc3a1",
        "glow": "rgba(143, 227, 200, .4)",
        "veil": "linear-gradient(160deg, #071813 0%, #0a2a22 42%, #0b0a16 100%)",
    },
    {
        "slug": "classroom",
        "file": "photo-classroom.jpg",
        "nav": "课间的教室",
        "kicker": "课间的教室",
        "title": "课间十分钟",
        "lines": [
            "桌上摊着卷子和水杯，谁站着聊天，谁回头看一眼镜头，谁在窗边笑——一个再普通不过的下午。",
            "就是这样的下午，被你记住了。以后搬进更漂亮的教室、带更新的电脑，也别把它们弄丢。",
        ],
        "quote": "普通的日子攒够多了，就成了后来的「那时候」。",
        "accent": "#ffb3c7",
        "accent2": "#ff7f9e",
        "glow": "rgba(255, 179, 199, .38)",
        "veil": "linear-gradient(160deg, #180a12 0%, #2a0f1c 42%, #0b0a16 100%)",
    },
    {
        "slug": "selfie",
        "file": "photo-selfie.jpg",
        "nav": "你拍我干嘛",
        "kicker": "镜头前的小孩",
        "title": "不用装大人",
        "lines": [
            "黑板还没擦干净，后墙的红色奖状还挂着，你就这么凑到镜头前，一副「拍完了没」的表情。",
            "十九岁可以很想长大，也可以继续做被镜头逗烦的那个小孩。两样都对。",
        ],
        "quote": "长大不是删掉小孩的部分，是带着他一起走。",
        "accent": "#c49bff",
        "accent2": "#ff82c0",
        "glow": "rgba(196, 155, 255, .4)",
        "veil": "linear-gradient(160deg, #140a20 0%, #1d0f2e 42%, #0b0a16 100%)",
    },
    {
        "slug": "shower",
        "file": "photo-shower.jpg",
        "nav": "刚洗完头",
        "kicker": "刚洗完头",
        "title": "刚洗完头的人",
        "lines": [
            "宿舍的白瓷砖、一个花洒、头发还滴着水，你就这么盯着镜头，一副「拍什么拍」的表情。",
            "大学生活的一半长这样：拥挤、随便、有点狼狈，但很自由。愿你在这种自由里，把自己照顾得像样。",
        ],
        "quote": "平常的日子过得踏实，才撑得起偶尔的高光。",
        "accent": "#9fd8ff",
        "accent2": "#6bb8ff",
        "glow": "rgba(159, 216, 255, .38)",
        "veil": "linear-gradient(160deg, #08131c 0%, #0c1e2c 42%, #0b0a16 100%)",
    },
    {
        "slug": "hat",
        "file": "photo-hat.jpg",
        "nav": "山路上的一天",
        "kicker": "山路上的一天",
        "title": "去发现更大的世界",
        "lines": [
            "蓝帽子、黑 T 恤、背后一座山和一片晃眼的阳光——一看就是出门在外的一天。",
            "十九岁最好的地方，是你还有整片地图没走。去看、去闯、去把自己晒黑一点。",
        ],
        "quote": "世界那么大，值得你亲自走一趟。",
        "accent": "#ffd48a",
        "accent2": "#ffb347",
        "glow": "rgba(255, 212, 138, .38)",
        "veil": "linear-gradient(160deg, #191307 0%, #241a08 42%, #0b0a16 100%)",
    },
    {
        "slug": "gaokao",
        "file": "photo-69.jpg",
        "ratio": "tall",
        "nav": "高考倒计时 69",
        "kicker": "高考倒计时 69",
        "title": "69 天，你撑住了",
        "lines": [
            "那块牌子上写着「高考倒计时 69」，底下一行 SZTU——深技大，是你后来考上的地方。",
            "现在回头看，那 69 天没有白熬——你考上了，而且笑得比牌子上的云还亮。",
        ],
        "quote": "偶尔的失落不是失败，而是为成功攒运气。",
        "accent": "#5fd4ff",
        "accent2": "#7b6cff",
        "glow": "rgba(95, 212, 255, .4)",
        "veil": "linear-gradient(160deg, #060f1e 0%, #0a1a33 42%, #0b0a16 100%)",
        "filter": "brightness(1.06)",
    },
    {
        "slug": "father",
        "file": "photo-father.jpg",
        "nav": "你爸和同学",
        "kicker": "父亲的老照片",
        "title": "左边那个人是你爸",
        "lines": [
            "照片里左边那个人是你爸，「初三（8）班」的牌子挂在门口，他背着 D'ckies 的书包，冲着镜头比了个耶，笑得有点拘谨；右边是他当年的同学，手里举着一张证件。",
            "这张照片的年份已经记不清了，但有一点很清楚：他也曾经是这个样子——校服、书包、站在教室门口，被人随手按下一次快门。",
        ],
        "quote": "你现在这个样子，他也曾经有过。",
        "accent": "#e8c9a0",
        "accent2": "#c9975f",
        "glow": "rgba(232, 201, 160, .4)",
        "veil": "linear-gradient(160deg, #171009 0%, #221607 42%, #0b0a16 100%)",
        "filter": "sepia(.35) saturate(.9) contrast(1.05)",
    },
    {
        "slug": "couple",
        "file": "photo-couple.jpg",
        "nav": "和你在一起的人",
        "kicker": "最后一场 · 和你在一起的人",
        "title": "她也在你的十九岁里",
        "ratio": "tall",
        "lines": [
            "宿舍里灯还没开、床帘半垂，你从背后抱住她，两个人都在笑。这张照片不用摆姿势，也不用挑角度。",
            "爸爸想说的只有一句：被人喜欢、也喜欢一个人，是件好事。愿你们在一起的日子，既有一起笑的时候，也有能好好说话的耐心。",
        ],
        "quote": "有个人愿意陪你过这些平常日子，比什么都难得。",
        "accent": "#ffb3c7",
        "accent2": "#ff8fab",
        "glow": "rgba(255, 179, 199, .4)",
        "veil": "linear-gradient(160deg, #1a0b13 0%, #2b1020 42%, #0b0a16 100%)",
        "filter": "brightness(1.14) contrast(1.03)",
    },
]

# ── 共享 CSS ────────────────────────────────────────────────────────────────

CSS = r"""
:root {
  --ink: #f4f1ff;
  --dim: rgba(244, 241, 255, .62);
  --faint: rgba(244, 241, 255, .4);
  --gold: #ffd98a;
  --line: rgba(255, 255, 255, .12);
  --sans: "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", system-ui, -apple-system, sans-serif;
  --serif: "Songti SC", "Noto Serif SC", Georgia, serif;
  --mono: "SF Mono", "JetBrains Mono", ui-monospace, monospace;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  min-height: 100vh;
  background: #07060f;
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}
canvas#sky {
  position: fixed; inset: 0; width: 100%; height: 100%;
  z-index: 0; pointer-events: none;
}
.wrap { position: relative; z-index: 2; pointer-events: none; }
/* 画布要能点，文字要能选：只让真正的交互元素恢复响应 */
.wrap a, .wrap button, .wrap .card, .wrap video { pointer-events: auto; }
a { color: inherit; text-decoration: none; }

/* —— 入场动画 —— */
@keyframes rise { from { transform: translateY(18px); } to { transform: none; } }
@keyframes fade { from { opacity: 0; } to { opacity: 1; } }
@keyframes breathe { 0%,100% { opacity: .5 } 50% { opacity: 1 } }
@keyframes floaty { 0%,100% { transform: translateY(0) } 50% { transform: translateY(-10px) } }
@keyframes shimmer { 0% { background-position: 0% 50% } 100% { background-position: 200% 50% } }

/* ═══════════════ 首页 ═══════════════ */
.home {
  min-height: 100vh;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 4vh 5vw 4vh; text-align: center;
  background:
    radial-gradient(80% 55% at 50% 0%, #1b1440 0%, transparent 70%),
    radial-gradient(60% 50% at 85% 90%, #2a1030 0%, transparent 70%),
    #07060f;
}
.home__eyebrow {
  font-family: var(--mono); font-size: .74rem; letter-spacing: .32em; max-width: 100%;
  text-transform: uppercase; color: var(--faint); margin-bottom: 1.3rem;
  animation: rise 1.2s .05s backwards;
}
.home__name {
  max-width: 100%; font-family: var(--serif);
  font-size: clamp(2.6rem, 8vw, 5.4rem);
  line-height: 1.12; margin: 0; font-weight: 700; letter-spacing: .02em;
  background: linear-gradient(100deg, #fff5da 0%, #ffd18a 28%, #ff9a6b 52%, #c9a4ff 78%, #7fd8ff 100%);
  background-size: 200% 100%;
  -webkit-background-clip: text; background-clip: text; color: transparent;
  animation: shimmer 9s linear infinite;
}
.home__name small {
  display: block; font-size: .5em; letter-spacing: .1em; margin-top: .5rem;
  color: transparent;
}
.home__age {
  display: flex; align-items: baseline; justify-content: center; gap: .55rem;
  margin: .9rem 0 .1rem; animation: rise 1.2s .35s backwards;
}
.home__age b {
  font-family: var(--serif); font-size: clamp(4.5rem, 17vw, 9.5rem);
  line-height: .9; font-weight: 700;
  background: linear-gradient(180deg, #fff6dd, #ffbf6e 62%, #ff8f5e);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  filter: drop-shadow(0 0 34px rgba(255, 170, 90, .38));
}
.home__age span { font-size: 1rem; letter-spacing: .32em; color: var(--dim); }
.home__sub {
  max-width: 37rem; width: 100%; margin: 1.05rem auto 0;
  font-size: clamp(.9rem, 2.6vw, 1.02rem); line-height: 2;
  color: var(--dim); animation: rise 1.2s .5s backwards;
}
.home__rule {
  width: min(30rem, 76vw); height: 1px; margin: 1.5rem auto;
  background: linear-gradient(90deg, transparent, var(--line) 20%, var(--line) 80%, transparent);
}
.home__hint {
  font-family: var(--mono); font-size: .7rem; letter-spacing: .2em; max-width: 100%;
  color: var(--faint); margin-bottom: 1.7rem; animation: rise 1.2s backwards;
}

/* 三个入口卡片 */
.cards {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: clamp(.7rem, 1.5vw, 1.15rem);
  width: min(56rem, 94vw); margin: 0 auto;
}
.card {
  position: relative; display: block; overflow: hidden;
  border-radius: 1.15rem; border: 1px solid var(--line);
  aspect-ratio: 4 / 5; background: #0d0b18;
  animation: rise .9s backwards; transition: transform .5s cubic-bezier(.2,.8,.2,1), box-shadow .5s, border-color .5s;
}
.card:nth-child(1) { animation-delay: .55s; }
.card:nth-child(2) { animation-delay: .65s; }
.card:nth-child(3) { animation-delay: .75s; }
.card:nth-child(4) { animation-delay: .85s; }
.card:nth-child(5) { animation-delay: .95s; }
.card img {
  position: absolute; inset: 0; width: 100%; height: 100%;
  object-fit: cover; object-position: center 22%;
  transition: transform 1.1s cubic-bezier(.2,.8,.2,1), filter .6s;
  filter: saturate(.92) brightness(.82);
}
.card::after {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(7,6,15,.96) 0%, rgba(7,6,15,.5) 34%, transparent 62%);
  transition: opacity .5s;
}
.card:hover { transform: translateY(-8px); border-color: rgba(255,255,255,.28); box-shadow: 0 26px 60px -24px var(--c, rgba(255,255,255,.35)); }
.card:hover img { transform: scale(1.06); filter: saturate(1.05) brightness(.92); }
.card__meta {
  position: absolute; z-index: 2; left: 0; right: 0; bottom: 0; padding: 1.15rem 1.15rem 1.25rem;
  text-align: left;
}
.card__no {
  font-family: var(--mono); font-size: .58rem; letter-spacing: .18em;
  color: var(--c, var(--faint)); display: block; margin-bottom: .4rem;
}
.card__t { font-family: var(--serif); font-size: clamp(.95rem, 1.05vw, 1.1rem); font-weight: 700; line-height: 1.35; margin: 0; display: block; }
.card__go {
  position: absolute; z-index: 3; top: .95rem; right: 1rem;
  width: 2rem; height: 2rem; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  border: 1px solid rgba(255,255,255,.22); background: rgba(7,6,15,.42);
  color: var(--c, #fff); font-size: .95rem;
  opacity: .72; transition: opacity .4s, transform .4s, background .4s;
}
.card:hover .card__go { opacity: 1; transform: translateX(4px); background: rgba(255,255,255,.14); }

.home__foot {
  margin-top: clamp(1.6rem, 4vh, 2.6rem); font-family: var(--mono);
  font-size: .66rem; letter-spacing: .2em; color: var(--faint);
  animation: rise 1.2s backwards;
}
.fire-btn {
  margin-top: 1.45rem; appearance: none; cursor: pointer;
  display: inline-flex; align-items: center; gap: .55rem;
  background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.2); border-radius: 100px;
  padding: .7rem 1.5rem; color: var(--ink); font-family: inherit;
  font-size: .82rem; letter-spacing: .14em; line-height: 1.4;
  transition: background .35s, border-color .35s, transform .35s, box-shadow .35s;
  animation: rise 1s .95s backwards;
}
.fire-btn:hover { background: rgba(255,255,255,.09); border-color: rgba(255,255,255,.36); transform: translateY(-2px); box-shadow: 0 0 24px -6px rgba(255,200,120,.5); }
.fire-btn:active { transform: scale(.97); }
.fire-btn__icon { font-size: 1.05rem; line-height: 1; filter: saturate(.9); }
.fire-btn--lit { border-color: rgba(255,201,120,.55); box-shadow: 0 0 26px -6px rgba(255,201,120,.6); }

/* ═══════════════ 蛋糕页 ═══════════════ */
.cake-canvas {
  position: fixed; inset: 0; width: 100%; height: 100%;
  z-index: 1; pointer-events: none;
  -webkit-mask-image: linear-gradient(to bottom, #000 0%, #000 72%, rgba(0,0,0,.55) 88%, transparent 100%);
  mask-image: linear-gradient(to bottom, #000 0%, #000 72%, rgba(0,0,0,.55) 88%, transparent 100%);
}
.is-cake #sky { opacity: .7; }
.cake-page {
  position: relative; z-index: 4;
  min-height: 100vh; display: flex; align-items: flex-start; justify-content: center;
  padding: 4.2vh 5vw 0; pointer-events: none;
}
.cake-page__text {
  position: relative; text-align: center; max-width: 30rem; pointer-events: auto;
}
.cake-page__text::before {
  content: ""; position: absolute; z-index: -1; inset: -1.1rem -1rem -.9rem;
  background: rgba(7, 6, 15, .62);
  border-radius: 1.4rem;
  box-shadow: 0 0 0 1px rgba(255, 255, 255, .045), 0 0 80px 44px rgba(7, 6, 15, .62);
  pointer-events: none;
}
.cake-page__kicker {
  font-family: var(--mono); font-size: .68rem; letter-spacing: .34em;
  color: var(--faint); margin: 0 0 1.1rem;
}
.cake-page__title {
  font-family: var(--serif); font-weight: 700; margin: 0;
  font-size: clamp(1.55rem, 3.6vw, 2.35rem); line-height: 1.3;
  background: linear-gradient(100deg, #fff3d8, #ffcb87 45%, #ffb27a 70%, #ffd9a8);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.cake-page__sub {
  margin: .8rem auto 0; max-width: 21rem;
  font-size: .82rem; line-height: 1.95; color: var(--dim);
}
.cake-page__acts {
  position: fixed; z-index: 5; left: 50%; bottom: clamp(1rem, 3.2vh, 2rem);
  transform: translateX(-50%);
  display: flex; flex-wrap: wrap; gap: .6rem; justify-content: center;
}
.cake-btn { background: rgba(12, 9, 20, .82); border-color: rgba(255,255,255,.26); color: var(--ink); font-size: .76rem; }
@media (max-width: 560px) {
  .cake-page { padding-top: 3.5vh; }
  .cake-page__sub { font-size: .78rem; max-width: 17rem; }
  .cake-page__acts { bottom: .9rem; }
}

/* ═══════════════ 内页 ═══════════════ */
.scene {
  min-height: 100vh; display: grid; align-items: center;
  grid-template-columns: minmax(0, 1.34fr) minmax(0, 1fr);
  gap: clamp(1.6rem, 3.6vw, 4rem);
  padding: clamp(3.4rem, 8vh, 6rem) clamp(1.2rem, 4vw, 3.6rem);
  background: var(--veil, #07060f);
  overflow-x: clip;            /* 光晕故意溢出照片框，别让它把页面撑宽 */
}
.scene__photo {
  position: relative; animation: rise 1.1s backwards;
}
/* figure 默认有 1em/40px 的外边距，且作为栅格子项会被拉伸——
   两样都会让照片缩成一小块，所以宽度、边距、对齐全部显式钉死。 */
.scene__photo {
  display: flex; flex-direction: column; justify-content: center;
  margin: 0; width: 100%; min-width: 0;
}
.scene__frame {
  position: relative; overflow: hidden; border-radius: 1.4rem;
  width: 100%; max-width: 100%;
  box-shadow: 0 40px 90px -34px #000, 0 0 0 1px var(--line);
  background: #0b0916;
}
.scene__frame img {
  display: block; width: 100%; height: auto;
  max-height: 82vh; object-fit: cover;
  object-position: center 38%;
  animation: rise 1.2s backwards;
}
.scene__frame--tall { aspect-ratio: 4 / 5; max-width: min(100%, 34rem); margin: 0 auto; }
.scene__frame--tall img { object-position: center 34%; }
.scene__frame::after {
  content: ""; position: absolute; inset: 0;
  box-shadow: inset 0 0 90px rgba(0,0,0,.42);
  pointer-events: none;
}
.scene__halo {
  position: absolute; z-index: -1; inset: -14% -10%;
  background: radial-gradient(closest-side, var(--glow, rgba(255,255,255,.3)), transparent 72%);
  filter: blur(28px); animation: breathe 7s ease-in-out infinite;
}
.scene__photo figcaption {
  margin-top: .95rem; font-family: var(--mono); font-size: .66rem;
  letter-spacing: .22em; color: var(--dim); text-align: right;
}
.scene__text { animation: rise 1.1s .18s backwards; }
.scene__kicker {
  display: inline-block; font-family: var(--mono); font-size: .68rem;
  letter-spacing: .28em; color: var(--accent, var(--gold));
  padding-bottom: .55rem; border-bottom: 1px solid var(--line);
  margin-bottom: 1.5rem;
}
.scene__title {
  font-family: var(--serif); font-weight: 700;
  font-size: clamp(1.9rem, 4.6vw, 3.1rem); line-height: 1.22; margin: 0 0 1.35rem;
  letter-spacing: .01em;
}
.scene__body p {
  margin: 0 0 1.05rem; font-size: clamp(.95rem, 1.6vw, 1.04rem);
  line-height: 2.05; color: var(--dim);
}
.scene__quote {
  margin: 1.9rem 0 0; padding-left: 1.05rem;
  border-left: 2px solid var(--accent, var(--gold));
  font-family: var(--serif); font-size: 1.06rem; line-height: 1.9;
  color: var(--ink); opacity: .92;
}
.scene__nav {
  display: flex; flex-wrap: wrap; gap: .7rem; margin-top: 2.4rem;
}
.btn {
  display: inline-flex; align-items: center; gap: .45rem;
  max-width: 100%;
  border: 1px solid var(--line); border-radius: 100px;
  padding: .66rem 1.15rem; font-size: .8rem; letter-spacing: .08em;
  line-height: 1.3; white-space: normal; text-align: center;
  color: var(--dim); transition: all .35s;
}
.btn:hover { color: var(--ink); border-color: rgba(255,255,255,.32); background: rgba(255,255,255,.05); }
.btn--home { color: var(--faint); }
.scene__pager {
  position: fixed; z-index: 5; right: clamp(1rem, 3vw, 2.2rem); top: 50%;
  transform: translateY(-50%); display: flex; flex-direction: column; gap: .55rem;
}
.dot {
  width: 8px; height: 8px; border-radius: 50%; background: rgba(244,241,255,.5);
  transition: all .4s;
}
.dot:hover { background: var(--ink); transform: scale(1.5); }
.dot.is-on { background: var(--accent, var(--gold)); box-shadow: 0 0 12px var(--accent, var(--gold)); }

@media (max-width: 560px) {
  .cards { grid-template-columns: 1fr; }
  .scene__nav { gap: .5rem; }
  .btn { padding: .58rem .95rem; font-size: .74rem; letter-spacing: .04em; }
  .scene__pager { display: none; }
  .home { padding: 7vh 6vw 8vh; }
  .home__sub { max-width: 21rem; line-height: 1.95; }
  .home__rule { margin: 2rem auto; }
}
@media (max-width: 860px) {
  .scene { grid-template-columns: 1fr; gap: 1.6rem; padding-top: 3rem; }
  .scene__frame img { max-height: 52vh; object-fit: contain; background: #000; }
  .scene__pager { display: none; }
  .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); width: 100%; gap: .6rem; }
  .card { aspect-ratio: 4 / 3; }
  .card img { object-position: center 26%; }
}
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
}
"""

# ── 蛋糕动画（独立文件，便于单独改） ────────────────────────────────────────

CAKE_JS = pathlib.Path(__file__).with_name("assets").joinpath("cake.js").read_text(encoding="utf-8")


# ── 星空 / 流星 / 烟花脚本 ───────────────────────────────────────────────────

JS = r"""
(function () {
  'use strict';
  var cv = document.getElementById('sky');
  if (!cv) return;
  var ctx = cv.getContext('2d');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, stars = [], shots = [], bursts = [];
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function resize() {
    W = cv.clientWidth; H = cv.clientHeight;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var n = Math.round((W * H) / 9000);
    stars = [];
    for (var i = 0; i < n; i += 1) {
      stars.push({
        x: Math.random() * W, y: Math.random() * H,
        r: Math.random() * 1.25 + .25,
        a: Math.random() * .6 + .15,
        tw: Math.random() * .018 + .004,
        ph: Math.random() * Math.PI * 2
      });
    }
  }

  function shooting() {
    var fromLeft = Math.random() > .5;
    shots.push({
      x: fromLeft ? -40 : W + 40,
      y: Math.random() * H * .55,
      vx: (fromLeft ? 1 : -1) * (Math.random() * 5 + 6),
      vy: Math.random() * 2.4 + 1.6,
      life: 1
    });
  }

  window.burstAt = function (x, y) {
    var hue = [42, 190, 275, 330, 15][Math.floor(Math.random() * 5)];
    var n = 46 + Math.floor(Math.random() * 26);
    for (var i = 0; i < n; i += 1) {
      var ang = (Math.PI * 2 * i) / n + Math.random() * .18;
      var sp = Math.random() * 4.6 + 1.6;
      bursts.push({
        x: x, y: y, vx: Math.cos(ang) * sp, vy: Math.sin(ang) * sp,
        life: 1, hue: hue + Math.random() * 34 - 17, size: Math.random() * 1.7 + .9
      });
    }
  };

  function frame() {
    ctx.clearRect(0, 0, W, H);

    for (var i = 0; i < stars.length; i += 1) {
      var s = stars[i];
      s.ph += s.tw;
      var a = reduce ? s.a : s.a * (.55 + .45 * Math.sin(s.ph));
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255, 248, 235, ' + a.toFixed(3) + ')';
      ctx.fill();
    }

    for (var k = shots.length - 1; k >= 0; k -= 1) {
      var sh = shots[k];
      sh.x += sh.vx; sh.y += sh.vy; sh.life -= .012;
      if (sh.life <= 0) { shots.splice(k, 1); continue; }
      var g = ctx.createLinearGradient(sh.x, sh.y, sh.x - sh.vx * 11, sh.y - sh.vy * 11);
      g.addColorStop(0, 'rgba(255,255,255,' + (.85 * sh.life) + ')');
      g.addColorStop(1, 'rgba(255,255,255,0)');
      ctx.strokeStyle = g; ctx.lineWidth = 1.7; ctx.lineCap = 'round';
      ctx.beginPath();
      ctx.moveTo(sh.x, sh.y);
      ctx.lineTo(sh.x - sh.vx * 11, sh.y - sh.vy * 11);
      ctx.stroke();
    }

    for (var b = bursts.length - 1; b >= 0; b -= 1) {
      var p = bursts[b];
      p.x += p.vx; p.y += p.vy; p.vx *= .972; p.vy = p.vy * .972 + .028; p.life -= .016;
      if (p.life <= 0) { bursts.splice(b, 1); continue; }
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
      ctx.fillStyle = 'hsla(' + p.hue.toFixed(0) + ', 95%, 68%, ' + (p.life * .95).toFixed(3) + ')';
      ctx.fill();
    }

    requestAnimationFrame(frame);
  }

  resize();
  window.addEventListener('resize', resize);

  if (!reduce) {
    setInterval(function () { if (Math.random() > .45 && shots.length < 3) shooting(); }, 1700);
    setTimeout(shooting, 1200);
  }

  var btn = document.getElementById('fire-btn');
  if (btn) {
    var lit = false;
    btn.addEventListener('click', function () {
      // 用视口坐标：按钮可能在首屏外，按它自身位置炸会在看不见的地方
      window.burstAt(W * .5, H * .76);
      window.burstAt(W * .26, H * .3);
      window.burstAt(W * .76, H * .22);
      if (!lit) {
        lit = true;
        btn.classList.add('fire-btn--lit');
        var label = btn.querySelector('.fire-btn__label');
        if (label) label.textContent = '再放一朵 · 点这儿看蛋糕';
      } else {
        window.location.href = 'cake.html';
      }
    });
    if (!reduce) {
      setTimeout(function () {
        window.burstAt(W * .5, H * .34);
      }, 1500);
    }
  }

  window.MiniBurst = { at: window.burstAt };

  if (document.body.classList.contains('is-scene') && !reduce) {
    setTimeout(function () { window.burstAt(W * .28, H * .3); }, 700);
  }

  requestAnimationFrame(frame);
}());
"""

# ── 模板 ────────────────────────────────────────────────────────────────────

def shell(title: str, body: str, body_class: str = "", extra_script: str = "",
          base_script: str = '<script src="assets/sky.js"></script>') -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#07060f">
<meta name="color-scheme" content="dark">
<title>{title}</title>
<link rel="stylesheet" href="assets/site.css">
</head>
<body class="{body_class}">
<canvas id="sky" aria-hidden="true"></canvas>
<div class="wrap">
{body}
</div>
{base_script}{extra_script}
</body>
</html>
"""


def home_page() -> str:
    cards = "\n".join(
        f"""      <a class="card{(' card--old' if p.get('filter') else '')}" href="{p['slug']}.html" style="--c: {p['accent']}; --glow: {p['glow']}">
        <img src="assets/photos/{p['file']}" alt="邹惟 · {p['nav']}">
        <span class="card__meta">
          <span class="card__go" aria-hidden="true">→</span>
          <span class="card__no">{i + 1:02d} · {p['nav']}</span>
          <span class="card__t">{p['title']}</span>
        </span>
      </a>"""
        for i, p in enumerate(PHOTOS)
    )

    return shell(
        f"{NAME} · 十九岁生日快乐",
        f"""<main class="home">
  <p class="home__eyebrow">For {NAME} · 19</p>
  <h1 class="home__name">{NAME}<small>生日快乐</small></h1>

  <div class="home__age"><b>{AGE}</b><span>岁</span></div>
  <p class="home__sub">十九岁这年，你从中学的教室走进大学的校园。这些照片替你记住了那些普通得不能再普通、却再也不会重来的下午。前面几张是爸爸想替你留住的，最后一张，留给你自己。</p>

  <div class="home__rule"></div>
  <p class="home__hint">点开任意一张，看看那天发生了什么</p>

  <div class="cards">
{cards}
  </div>

  <button class="fire-btn" id="fire-btn" type="button">
    <span class="fire-btn__icon" aria-hidden="true">🎂</span>
    <span class="fire-btn__label">放一朵烟花</span>
  </button>

  <p class="home__foot">MADE WITH LOVE · {NAME} 19</p>
</main>""",
        "is-home",
    )


def scene_page(index: int) -> str:
    p = PHOTOS[index]
    prev_i = (index - 1) % len(PHOTOS)
    next_i = (index + 1) % len(PHOTOS)
    prev_p, next_p = PHOTOS[prev_i], PHOTOS[next_i]

    body_paras = "\n".join(f"        <p>{line}</p>" for line in p["lines"])

    dots = "\n".join(
        f'      <a class="dot{" is-on" if i == index else ""}" href="{q["slug"]}.html" title="{q["nav"]}"></a>'
        for i, q in enumerate(PHOTOS)
    )

    return shell(
        f"{p['title']} · {NAME} 19 岁",
        f"""<main class="scene" style="--accent: {p['accent']}; --accent2: {p['accent2']}; --glow: {p['glow']}; --veil: {p['veil']}">
  <figure class="scene__photo">
    <span class="scene__halo" aria-hidden="true"></span>
    <div class="scene__frame{' scene__frame--' + p['ratio'] if p.get('ratio') else ''}">
      <img src="assets/photos/{p['file']}" alt="{p['nav']} · {NAME}"{f' style="filter: {p["filter"]}"' if p.get('filter') else ''}>
    </div>
    <figcaption>NO.{index + 1:02d} · {p['nav']}</figcaption>
  </figure>

  <section class="scene__text">
    <span class="scene__kicker">第{CN_NUM[index + 1]}场 · {p['kicker'].split(' · ')[-1]}</span>
    <h2 class="scene__title">{p['title']}</h2>
    <div class="scene__body">
{body_paras}
    </div>
    <blockquote class="scene__quote">「{p['quote']}」</blockquote>

    <nav class="scene__nav">
      <a class="btn" href="index.html">← 回到起点</a>
      <a class="btn" href="{prev_p['slug']}.html">← {prev_p['nav']}</a>
      <a class="btn" href="{next_p['slug']}.html">{('再看一遍 ↺') if index == len(PHOTOS) - 1 else (next_p['nav'] + ' →')}</a>
    </nav>
  </section>
</main>

<nav class="scene__pager" aria-label="照片切换">
{dots}
</nav>""",
        "is-scene",
    )


def cake_page() -> str:
    return shell(
        f"生日蛋糕 · {NAME} 19 岁",
        f"""<main class="cake-page">
  <div class="cake-page__text">
    <p class="cake-page__kicker">HAPPY BIRTHDAY · {NAME}</p>
    <h1 class="cake-page__title">十九岁，<br>先吹个蜡烛</h1>
    <p class="cake-page__sub">没来得及买蛋糕，就先给你画一个。<br>蜡烛真的会晃，许个愿。</p>
    <div class="cake-page__acts">
      <a class="btn cake-btn" href="index.html">← 回去看照片</a>
      <button class="btn cake-btn" id="again-btn" type="button">再点一次蛋糕</button>
    </div>
  </div>
</main>
<canvas id="cake" class="cake-canvas" aria-label="生日蛋糕" role="img"></canvas>""",
        "is-cake",
        '<script src="assets/cake.js"></script>',
        "",
    )


def main() -> None:
    (ROOT / "assets").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets" / "site.css").write_text(CSS, encoding="utf-8")
    (ROOT / "assets" / "sky.js").write_text(JS, encoding="utf-8")
    (ROOT / "index.html").write_text(home_page(), encoding="utf-8")
    for i, p in enumerate(PHOTOS):
        (ROOT / f"{p['slug']}.html").write_text(scene_page(i), encoding="utf-8")
    (ROOT / "cake.html").write_text(cake_page(), encoding="utf-8")
    (ROOT / "assets" / "cake.js").write_text(CAKE_JS, encoding="utf-8")
    files = sorted(x.name for x in ROOT.glob("*.html"))
    print(f"生成完成：{len(files)} 个页面 · {files}")
    print(f"照片 {len(list((ROOT / 'assets/photos').glob('*.jpg')))} 张")
    print(f"入口：{ROOT / 'index.html'}")


if __name__ == "__main__":
    main()
