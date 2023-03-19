let timer = 60;

const time = setInterval(async function(){
    timer -= 1;
    $('#timer').text("Timer: " + timer);
    if(timer == 0){

        clearInterval(time);
        $('#form').remove();

        const response = await axios({
            url: `/check-highscore`,
            method: "GET"
        });

        $('.boggle-result').text(response.data['highscore']);
        $("#Game-Area").append($('<button>')
                            .attr('class', 'button')
                            .attr('onclick', "window.location.href='/';")
                            .text('Play Again?'));
    }
}, 1000);

async function checkAnswer(){

    const word = $('input').val();
    $('input').val('');

    const response = await axios({
        url: `/check-answer`,
        method: "POST",
        data: { word },
    });

    $('.boggle-result').remove();
    $("#Game-Area").append($('<div>')
                            .attr('class', 'boggle-result')
                            .text(response.data['result'].replace("-", " ")));
    $('#score').text("Score: " + response.data['score']);
}


$('button').on('click', checkAnswer);
$('input').on('keypress', function(e){
    if(e.which == 13) $('button').click();
})