alert('hello');

window.onbeforeunload = function(e){
    return 'あまり推奨されていない動作です';
}