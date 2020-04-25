$(document).ready(function(){
    
    $("#submit_login").on("click", function(event){
        event.preventDefault();
        console.log("Username = " + $('#username_login').val() + "and Password is = " + $('#password_login').val());

        var username = $('#username_login').val();
        var password = $('#password_login').val();
        console.log("username = " + username + " and password = " + password);

        if(username != "" && password != ""){
            $.ajax({
                type : "POST",
                url : '/login',
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({'username' : username, 'password' : password }),
                dataType: "json",
                success: function(data) {
                    if(data.error){
                        console.log("Error : " + data.error)
                        $('#error_alert').text(data.error).show();
                        $('#success_alert').hide();
                    }else{
                        if(data.results == "Username or password incorrect!"){
                            console.log("Error : " + data.results)
                            $('#error_alert').text(data.results).show();
                            $('#success_alert').hide(); 
                        }else{
                            console.log("Success! : " + data.results)
                            window.location.replace("http://sciq-unimib-dev.herokuapp.com/logged_user")
                        }
                    }
                },
                error: function(err) {
                console.log("General error"+ err);
                }
            });

        }else{
            $('#error_alert').text("Username or password empty!").show();
            $('#success_alert').hide(); 
        }
    });
});