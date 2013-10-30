
$(document).ready(function(){
    $("#searchlesson").click(function(){
        var lesson=$("#lesson").val();
        var reg=/^[a-zA-Z0-9_\u4e00-\u9fa5]+$/;
        var reg_lesson=reg.test(lesson);

        var username=$("#username").val();

        if(!reg_lesson){
            $(".error").text("搜索课程标题输入错误。").css("display","inline");
            }
        else{
            $.post("/research/"+username,{lesson:lesson,username:username},function(data){
                if(data=="True"){
                    location.href="/research_one/"+username+"?keyword="+lesson;
                    }
                else{
                    $(".error").text("没有符合的课程。").css("display","inline");
                    }
                },"html");
            }
        });
    });


