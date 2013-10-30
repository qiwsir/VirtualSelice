$(document).ready(function(){
    $("#adduser").click(function(){
        var newusername=$("#username").val();
        var newuserrole=$("#userrole").val();

        var reg=/^[\u4e00-\u9fa5A-Za-z_0-9]+$/;

        var reg_newusername=reg.test(newusername);

        if(!reg_newusername){
            $(".error").text("用户名不能为空，且只能输入汉字、字母和数字。").css("display","inline");
            }
        else{
            $.post("/adminuser_add/headmaster",{newusername:newusername,newuserrole:newuserrole},function(data){
                if(data=="False"){
                    $(".error").text("此用户名称已经存在").css("display","inline");
                    }
                else if(data=="True"){
                    alert("用户名："+newusername+"  已经成功添加");
                    location.href="/adminuser_add/headmaster";
                    }
                },"html");
            }
        });
    });


$(document).ready(function(){
    $("#checkusername").click(function(){
        var username=$("#username").val();
        var reg=/^[\u4e00-\u9fa5A-Za-z_0-9]+$/;
        var reg_username=reg.test(username);

        if(!reg_username){
            $(".error").text("用户名错误。").css("display","inline");
            }
        else{
            $.post("/adminuser_look/headmaster",{username:username},function(data){
                if(data=="False"){
                    $(".error").text("此用户名不存在").css("display","inline");
                    }
                else{
                    location.href="/adminuser_look/headmaster?user="+username;
                    }
                },"html");
            }
        });
    });

$(document).ready(function(){
    $("#oknewpassword").click(function(){
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
            $.post("/adminuser/headmaster",{newpassword:newpassword},function(data){
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
