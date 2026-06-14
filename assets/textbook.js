// 모바일 목차 토글 + 현재 챕터로 사이드바 스크롤
(function () {
  var btn = document.getElementById('menuBtn');
  var toc = document.getElementById('toc');
  if (btn && toc) {
    btn.addEventListener('click', function () { toc.classList.toggle('open'); });
    toc.addEventListener('click', function (e) {
      if (e.target.closest('a') && window.innerWidth <= 920) toc.classList.remove('open');
    });
  }
  var active = toc && toc.querySelector('a.lnk.active');
  if (active) active.scrollIntoView({ block: 'center' });
})();
