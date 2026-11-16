
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
