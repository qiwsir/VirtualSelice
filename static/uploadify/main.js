$(document).ready(function() {
    $('#file_upload').uploadify({
        'fileExt' : '*.jpg;*.jpeg;*.gif;*.png',
        //'expressInstall' : '/static/uploadify/expressInstall.swf',
        'uploader' : '/static/uploadify/uploadify.swf',
        'swf':'/static/uploadify/uploadify.swf',
        'script' : '/study_new_video/邓丽君',
        'cancelImg' : '/static/uploadify/uploadify-cancel.png',
        'floder':'/static/video',
        'auto' : true,
        'multi':true,
        'queueSizeLimit':20,
        'sizeLimit':10240000,
        'fileExt':'*.jpg;*.gif;*.png',
        'onInit':function(){},
        'onError':function(event,ID,fileObj,errorObj){$('.error').html("上传失败，错误代码："+errorObj.type+" "+errorObj.info);},
        'onSelect':function(e,queueId,fileObj){$('.error').html("");},
        'onAllComplete':function(event,data){
            if(data.filesUploaded>=1){$('.error').html("ok!You had upload successfully.")};
            },
        'formData':{
            'time':'2013',
            },
        'onComplete':function(data){alert(data)},
    });
});
