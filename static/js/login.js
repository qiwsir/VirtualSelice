$(document).ready(function(){
    $("#login").click(function(){
        var username=$("#username").val();
        var userpwd=$("#userpwd").val();

        var reg=/^[\u4e00-\u9fa5A-Za-z_0-9]+$/;

        var reg_username=reg.test(username);
        var reg_userpwd=reg.test(userpwd);

        if(!reg_username||!reg_userpwd){
            $(".error").text("用户名和密码不能为空，且只能输入汉字、字母和数字。").css("display","inline");
            }
        else{
            $.post("/logindex",{username:username,userpwd:userpwd},function(data){
                if(data=="0"){
                    $(".error").text("用户名或密码错误。").css("display","inline");
                    }
                else if(data=="1"){
                    location.href="/adminuser/headmaster";
                    }
                else if(data=="2"){
                    location.href="/study/"+username;
                    }
                else if(data=="3"){
                    location.href="/teacher/"+username;
                    }
                else{
                    $(".error").text("用户名或密码有误。").css("display","inline");
                    }
                },"html");
            }
        });
    });
