
$(document).ready(function(){
    $("#okupload").click(function(){
        var videotitle=$("#videotitle").val();
        var reg=/^[a-zA-Z0-9_\u4e00-\u9fa5]+$/;
        var reg_videotitle=reg.test(videotitle);

        var username=$("#username").val();

        var videofile=$("#videofile").val();
        var formData = new FormData($('form')[0]);


        if(!reg_videotitle){
            $(".error").text("课程标题不符合规范，只能是数字、字母或汉字组成。").css("display","inline");
            }
        else{
            $.post("/study_new_video/"+username,{formdata:formData,username:username,videotitle_file:videotitle,videofile_file:videofile},function(data){
                if(data=="True"){
                    alert(data);
                    }
                else{
                    $(".error").text("课程上传失败，请查看课程是否为.ogv格式。").css("display","inline");
                    }
                },"html");
            }
        });
    });


