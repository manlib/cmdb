   $( function(){
        var oBtn = document.getElementById('btn');
    var oShow = document.getElementById('show');
    oBtn.onclick = function (e) {
        e.preventDefault();
        oShow.style.display = 'block';
    };
       }
   )