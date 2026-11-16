/* StudyMate · 邹惟生日页 · 满屏生日蛋糕
 *
 * 一个 canvas，一个无限循环。所有尺寸都按「单位坐标」画（蛋糕占 ±1 宽），
 * 再用 fit 缩放铺满窗口；竖屏时少画几根蜡烛，别挤成一排。
 */
(function () {
  'use strict';

  var cv = document.getElementById('cake');
  if (!cv) return;
  var ctx = cv.getContext('2d');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, S = 1, CY = 0;
  var cakeOn = false;
  var sparkles = [];
  var t0 = 0;

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── 时间轴（秒） ── */
  var T = {
    shadow: .15,
    bottom: .45,
    middle: .85,
    top: 1.2,
    candles: 1.55,
    flames: 1.9,
    words: 2.25,
    age: 2.6,
    banner: 3.05
  };

  function easeOut(x) { return 1 - Math.pow(1 - x, 3); }
  function easeBack(x) { var c = 1.7; return 1 + (c + 1) * Math.pow(x - 1, 3) + c * Math.pow(x - 1, 2); }
  function clamp01(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function prog(now, start, dur) { return clamp01((now - start) / (dur || .7)); }

  /* ── 缩放：让蛋糕铺满窗口（竖屏自动收一点） ── */
  function fit() {
    var wasEmpty = !stars.length;
    W = cv.clientWidth; H = cv.clientHeight;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    // 蛋糕占单位坐标 x∈[-1,1]：宽度方向铺满，垂直居中在屏幕下部，
    // 顶部留出标题与按钮的空间（蜡烛顶端在 y≈-0.65）
    // 铺满：宽度方向撑到 94%，竖直方向由上面留白决定
    S = Math.min(W * .5, H * .5);
    CY = H * .66;
    if (wasEmpty) seedStars();
  }

  var stars = [];
  function seedStars() {
    stars = [];
    var n = Math.round((W * H) / 14000);
    for (var i = 0; i < n; i += 1) {
      stars.push({
        x: Math.random() * W, y: Math.random() * H * .72,
        r: Math.random() * 1.1 + .3, a: Math.random() * .5 + .12,
        ph: Math.random() * Math.PI * 2, sp: Math.random() * .02 + .004
      });
    }
  }

  function begin(now) {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    for (var i = 0; i < stars.length; i += 1) {
      var st = stars[i];
      st.ph += st.sp;
      ctx.beginPath();
      ctx.arc(st.x, st.y, st.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255, 248, 235, ' + (st.a * (.55 + .45 * Math.sin(st.ph))).toFixed(3) + ')';
      ctx.fill();
    }
    ctx.save();
    ctx.translate(W / 2, CY);
    ctx.scale(S, S);
    drawTable(now);
  }
  function end() { ctx.restore(); }

  /* ── 桌面与光晕 ── */
  function drawTable(now) {
    if (true) return;   // 桌面光晕在铺满时会被裁掉一半，改由 CSS 底部渐隐负责
    var p = prog(now, T.shadow);
    if (p <= 0) return;
    ctx.save();
    ctx.globalAlpha = .55 * p;
    var g = ctx.createRadialGradient(0, 1.08, 0, 0, 1.08, 1.55);
    g.addColorStop(0, 'rgba(255, 190, 110, .5)');
    g.addColorStop(.55, 'rgba(255, 150, 80, .1)');
    g.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = g;
    ctx.beginPath();
    ctx.ellipse(0, 1.12, 1.5, .3, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  /* ── 一层蛋糕 ── */
  function tierLayer(cx, cy, rx, h, colTop, colFront, colSide, alpha, labels) {
    ctx.save();
    ctx.globalAlpha = alpha;

    // 侧面（圆柱体）
    var sideG = ctx.createLinearGradient(cx - rx, 0, cx + rx, 0);
    sideG.addColorStop(0, colSide[0]);
    sideG.addColorStop(.5, colSide[1]);
    sideG.addColorStop(1, colSide[2]);
    ctx.fillStyle = sideG;
    ctx.beginPath();
    ctx.moveTo(cx - rx, cy);
    ctx.lineTo(cx - rx, cy + h);
    ctx.ellipse(cx, cy + h, rx, rx * .28, 0, Math.PI, 0, true);
    ctx.lineTo(cx + rx, cy);
    ctx.closePath();
    ctx.fill();

    // 正面奶油高光
    var frontG = ctx.createLinearGradient(0, cy, 0, cy + h);
    frontG.addColorStop(0, colFront[0]);
    frontG.addColorStop(1, colFront[1]);
    ctx.fillStyle = frontG;
    ctx.beginPath();
    ctx.ellipse(cx, cy + h * .42, rx * .96, h * .5, 0, 0, Math.PI * 2);
    ctx.globalAlpha = alpha * .28;
    ctx.fill();
    ctx.globalAlpha = alpha;

    // 顶面
    var topG = ctx.createLinearGradient(0, cy - rx * .28, 0, cy + rx * .28);
    topG.addColorStop(0, colTop[0]);
    topG.addColorStop(1, colTop[1]);
    ctx.fillStyle = topG;
    ctx.beginPath();
    ctx.ellipse(cx, cy, rx, rx * .28, 0, 0, Math.PI * 2);
    ctx.fill();

    // 顶边亮线
    ctx.strokeStyle = 'rgba(255,255,255,.5)';
    ctx.lineWidth = .012;
    ctx.beginPath();
    ctx.ellipse(cx, cy, rx, rx * .28, 0, Math.PI * 1.05, Math.PI * 1.95);
    ctx.stroke();

    // 侧面的小字（写在「正面」上）
    if (labels) {
      ctx.save();
      // 压进椭圆正面：竖直方向缩小
      ctx.translate(cx, cy + h * .58);
      ctx.scale(1, .42);
      ctx.rotate(0);
      ctx.globalAlpha = alpha * .92;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillStyle = '#4a2b1c';
      ctx.font = '700 .2px "PingFang SC", "Hiragino Sans GB", sans-serif';
      ctx.fillText(labels.text, 0, 0);
      ctx.font = '900 .46px "PingFang SC", "Hiragino Sans GB", sans-serif';
      ctx.fillStyle = '#3a1f12';
      ctx.fillText(labels.age, 0, .46);
      ctx.restore();
    }

    ctx.restore();
  }

  /* ── 蜡烛 + 火苗 ── */
  function candle(x, baseY, h, phase, k, now) {
    var grow = prog(now, T.candles + k * .09, .45);
    var flick = prog(now, T.flames, .45);
    if (grow <= 0) return;

    var hh = h * easeOut(grow);
    var alpha = Math.min(1, grow * 2);

    ctx.save();
    ctx.globalAlpha = alpha;

    // 蜡烛身
    var bodyG = ctx.createLinearGradient(x - .035, 0, x + .035, 0);
    bodyG.addColorStop(0, '#e94f6b');
    bodyG.addColorStop(.5, '#fff3f5');
    bodyG.addColorStop(1, '#c93a55');
    ctx.fillStyle = bodyG;
    ctx.beginPath();
    ctx.moveTo(x - .04, baseY);
    ctx.lineTo(x - .04, baseY - hh);
    ctx.quadraticCurveTo(x, baseY - hh - .035, x + .04, baseY - hh);
    ctx.lineTo(x + .04, baseY);
    ctx.closePath();
    ctx.fill();

    // 斜条纹
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(x - .04, baseY);
    ctx.lineTo(x - .04, baseY - hh);
    ctx.quadraticCurveTo(x, baseY - hh - .035, x + .04, baseY - hh);
    ctx.lineTo(x + .04, baseY);
    ctx.closePath();
    ctx.clip();
    ctx.strokeStyle = 'rgba(220, 60, 90, .5)';
    ctx.lineWidth = .016;
    for (var s = -1; s < 4; s += 1) {
      ctx.beginPath();
      ctx.moveTo(x - .05, baseY - s * .11);
      ctx.lineTo(x + .05, baseY - s * .11 - .07);
      ctx.stroke();
    }
    ctx.restore();

    // 火苗
    if (flick > 0) {
      var fl = .78 + .22 * Math.sin(now * 7.3 + phase) + .1 * Math.sin(now * 13.1 + phase * 2);
      var fy = baseY - hh - .05;
      var scale = easeBack(flick) * fl;

      ctx.save();
      ctx.translate(x, fy);
      ctx.scale(1, scale);
      ctx.globalAlpha = alpha;

      // 外焰
      var g = ctx.createRadialGradient(0, -0.09, 0, 0, -0.02, .26);
      g.addColorStop(0, 'rgba(255, 236, 160, .95)');
      g.addColorStop(.35, 'rgba(255, 186, 70, .85)');
      g.addColorStop(.75, 'rgba(255, 120, 40, .45)');
      g.addColorStop(1, 'rgba(255, 90, 30, 0)');
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.moveTo(0, -0.21);
      ctx.quadraticCurveTo(.075, -0.07, 0, 0);
      ctx.quadraticCurveTo(-.075, -0.07, 0, -0.21);
      ctx.fill();

      // 内焰
      ctx.fillStyle = 'rgba(255, 255, 235, .92)';
      ctx.beginPath();
      ctx.moveTo(0, -0.11);
      ctx.quadraticCurveTo(.042, -0.04, 0, 0);
      ctx.quadraticCurveTo(-.042, -0.04, 0, -0.11);
      ctx.fill();
      ctx.restore();
    }

    ctx.restore();
  }

  /* ── 顶部浮字 ── */
  function banner(now) {
    var p = prog(now, T.banner, .8);
    if (p <= 0) return;
    ctx.save();
    ctx.globalAlpha = easeOut(p);
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = 'rgba(255, 246, 226, .96)';
    ctx.font = '700 .2rem "PingFang SC", "Hiragino Sans GB", sans-serif';
    // 用像素字号：这里已经缩放过了，按窗口宽换算
    var px = Math.min(20, W / 26);
    ctx.font = '700 ' + px + 'px "PingFang SC", "Hiragino Sans GB", sans-serif';
    ctx.fillText('邹惟', 0, -1.62);
    ctx.font = '500 ' + (px * .54) + 'px "PingFang SC", "Hiragino Sans GB", sans-serif';
    ctx.fillStyle = 'rgba(255, 236, 205, .7)';
    ctx.fillText('十九岁 · 生日快乐', 0, -1.44);
    ctx.restore();
  }

  /* ── 火星 ── */
  function sparks(now, dt) {
    // 每 1.6 秒补一批从火苗飘起来的火星
    var last = sparks.last || 0;
    if (now - last > 1.6) {
      sparks.last = now;
      for (var i = 0; i < 10; i += 1) {
        var cx = (-1 + Math.random() * 2) * .82;
        sparkles.push({
          x: cx, y: -.55 - Math.random() * .5,
          vx: (Math.random() - .5) * .06,
          vy: -(Math.random() * .12 + .04),
          life: 1, r: .012 + Math.random() * .016, hue: 30 + Math.random() * 20
        });
      }
    }
    for (var k = sparkles.length - 1; k >= 0; k -= 1) {
      var s = sparkles[k];
      s.x += s.vx * dt * 60; s.y += s.vy * dt * 60; s.life -= dt * .38;
      if (s.life <= 0) { sparkles.splice(k, 1); continue; }
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r * s.life, 0, Math.PI * 2);
      ctx.fillStyle = 'hsla(' + s.hue.toFixed(0) + ', 100%, 72%, ' + (s.life * .85).toFixed(3) + ')';
      ctx.fill();
    }
  }

  /* ── 主循环 ── */
  var last = 0;
  function frame(ts) {
    var now = ts / 1000;
    var dt = last ? Math.min(.05, now - last) : .016;
    last = now;
    if (!t0) t0 = now;
    var t = now - t0;

    fit();
    begin(t);

    // 蛋糕主体从上往下：底层先出
    var rows = [
      { y: .66, rx: 1.0, h: .46, top: ['#fff6ec', '#ffe3cf'], front: ['#ffd9c4', '#f7b9a0'], side: ['#c98a72', '#dba98f', '#b97b64'], start: T.bottom },
      { y: .12, rx: .78, h: .4, top: ['#fff8f0', '#ffe9d6'], front: ['#ffcfba', '#f2a98e'], side: ['#bf7c63', '#d79b82', '#ae6c55'], start: T.middle },
      { y: -.3, rx: .56, h: .34, top: ['#fffaf4', '#ffeedd'], front: ['#ffd9c9', '#f3b49b'], side: ['#c5866e', '#dda890', '#b27359'], start: T.top }
    ];

    for (var i = 0; i < rows.length; i += 1) {
      var r = rows[i];
      var p = easeOut(prog(t, r.start, .65));
      if (p <= 0) continue;
      var cy = (r.y + r.h * .5) * (1 - p) + r.y * p;
      var h = r.h * p;
      var labels = null;
      if (i === 1 && prog(t, T.words, .6) > .35) {
        labels = { text: '生日快乐', age: '19' };
      }
      tierLayer(0, cy - h, r.rx, h, r.top, r.front, r.side, Math.min(1, p * 1.6), labels);
    }

    // 蜡烛
    var positions = [-.4, -.2, 0, .2, .4];
    var n = W < 520 ? 3 : 5;
    var shown = positions.slice(0, n);
    var mid = (shown.length - 1) / 2;
    for (var c = 0; c < shown.length; c += 1) {
      var x = shown[c] * .94;
      candle(x, -.31, .34, c * .7, c, t);
    }

    sparks(t, dt);
    banner(t);
    end();

    requestAnimationFrame(frame);
  }

  /* ── 进场：先撒花，再让蛋糕长出来 ── */
  function reveal() {
    cakeOn = true;
    t0 = 0; last = 0;
    requestAnimationFrame(frame);
  }

  window.CakePage = {
    cut: function () {
      reveal();
      if (window.MiniBurst) {
        for (var i = 0; i < 7; i += 1) {
          setTimeout(function (k) {
            return function () {
              window.MiniBurst.at(W * (.16 + Math.random() * .68), H * (.16 + Math.random() * .34));
            };
          }(i), i * 110);
        }
      }
    }
  };

  var again = document.getElementById('again-btn');
  if (again) {
    again.addEventListener('click', function () {
      sparkles.length = 0;
      t0 = 0;
      if (window.MiniBurst) {
        window.MiniBurst.at(W * .3, H * .3);
        setTimeout(function () { window.MiniBurst.at(W * .7, H * .22); }, 180);
      }
    });
  }

  window.addEventListener('resize', function () { fit(); seedStars(); });
  fit();

  if (!reduce) {
    setTimeout(function () {
      if (window.MiniBurst) {
        window.MiniBurst.at(W * .22, H * .24);
        setTimeout(function () { window.MiniBurst.at(W * .8, H * .2); }, 260);
      }
    }, 420);
  }
  reveal();
}());
