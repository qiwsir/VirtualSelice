
$(document).ready(function(){
    $("#oknewpassword").click(function(){
        var username=$("#username").val();
        var newpassword=$("#newpassword").val();
        var renewpassword=$("#renewpassword").val();
        var reg=/^[A-Za-z_0-9]+$/;
        var reg_newpassword=reg.test(newpassword);
        if(!reg_newpassword){
            $(".error").text("密码设置不符合要求。").css("display","inline");
            }
        else if(newpassword!=renewpassword){
            $(".error").text("两次密码设置得不一样。").css("display","inline");
            }
        else{
            $.post("/study/"+username,{newpassword:newpassword,username:username},function(data){
                if(data=="True"){
                    $(".error").text("密码修改成功。").css('display',"inline");
                    }
                else{
                    $(".error").text("因为网络原因，密码没有修改。").css("display","inline");
                    }
                },"html");
            }
        });
    });


$(document).ready(function(){                                                                       
    $("#checklessonname").click(function(){                                  
        var check_lessonname=$("#lessonname").val();                                          
        var reg=/^[\u4e00-\u9fa5A-Za-z_0-9]+$/;                                                     
        var reg_lessonname=reg.test(username);

        var username=$("#username").val();

        if(!reg_lessonname){
            $(".error").text("名称错误。").css("display","inline");
        }
        else{
            $.post("/study_manage_video/"+username,{lessonname:check_lessonname},function(data){
                if(data=="False"){
                    $(".error").text("此课程名称不存在").css("display","inline");
                }
                else{
                    location.href="/study_manage_video/"+username+"?lessonname="+check_lessonname;
                }
            },"html");
        }
    });                                                                                         
});           
