// jquery stuff

$(document).ready(function() {

    console.log('were live!');

    // retrieves all queries from query list table
    // and appends radio buttons for each of them to html
    $.get('/all-queries', function(data,status) {
        console.log(data);
        console.log('getting all queries');
        var res = data['results'];
        var container = $('#button-stuff');
        for (var i = 1; i < res.length; i++) {
            console.log('looping! ' + i.toString());
            var html = '';
            html += '<input type="radio" name="query" value="';
            html += res[i][0].toString() + '"';
            if (i==1) {
                html += ' checked'
            }
            html += '>';
            html += res[i][1];
            html += '<br>';
            container.append(html);
        }
    },'json');

    // just gets some default table to populate table div
    $.get('/get-table',function(data,status) {
        console.log('status: ' + status);
        $('#sql-table').html(data);
    });

    // need this variable as a hack to prevent
    // the logic below from triggering twice
    var radio_button_logic_set = false;

    // get id of selected input button and request
    // a table generated from the corresponding sql statement
    $(document).ajaxComplete( function(event,request,settings) {

        if (! radio_button_logic_set) {
            $('input[type=radio][name=query]').on('change',
                function() {
                    console.log('radio button changed');
                    var query_id = $(this).val();
                    console.log(query_id);
                     $.ajax({
                         url: '/query/' + query_id.toString(),
                         type: 'POST',
                         success: function(data) {
                             console.log('got the query');
                             $('#sql-table').html(data);
                         }
                     });
                });
            radio_button_logic_set = true;
        }

    });


});

