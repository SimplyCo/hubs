$(function() {

    // all textareas on page
    $('textarea').each(function(e){

            var upload_url = '/adm/redactor/upload/image/';

            $(this).redactor({
                minHeight: 400,
                buttons: [
                    'html',
                    'formatting',
                    'bold',
                    'italic',
                    'deleted',
                    'unorderedlist',
                    'orderedlist',
                    'outdent',
                    'indent',
                    'image',
                    'video',
                    'link',
                    'alignment',
                    'table',
                    'horizontalrule'
                ],
                plugins: [
                    'definedlinks',
                    'fontcolor',
                    'fontfamily',
                    'fontsize',
                    'fullscreen',
                    'table',
                    'video',
                ],
                imageUpload: upload_url

            });


    });


});