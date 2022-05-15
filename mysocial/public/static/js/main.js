console.log("hi here3")



function login()
{
    var username = document.getElementById('username').value
    var password = document.getElementById('password').value
    var csrf = document.getElementById('csrf').value

    if(username=='' && password=='')
    {
        alert('You must enter both')
    }
    var data = {
        'username': username,
        'password': password
    }
    fetch('/api/login/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        'body': JSON.stringify(data)
    }).then(result=>result.json())
    .then(response=>{
        if(response.status==200)
        {
            window.location.href='/'
        }
        else
        {
            alert(response.message)
        }
    })
}


function register()
{
    var username= document.getElementById('username').value
    var password= document.getElementById('password').value
    var csrf= document.getElementById('csrf').value

    if(username=='' && password=='')
    {
        alert('You must enter both')
    }

    var data={
        'username':username,
        'password':password
    }

    fetch('/api/register/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrf
        },
        'body': JSON.stringify(data)
    }).then(result=>result.json())
    .then(response=>{
        if(response.status==200)
        {
            window.location.href='/'
        }
        else
        {
            alert(response.message)
        }
    })
}


function comment() {
    var commentDid = document.getElementById('comment').value;
    var commented = document.getElementById('commented').value;
    var csrf = document.getElementById('csrf').value
    if(commentDid=='')
    {
        alert('You must enter a comment')
    }
    var data = {
        'comment':commentDid,
        'commented':commented,
    }
    fetch('/api/comment/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrf
        },
        'body': JSON.stringify(data)
    }).then(result=>result.json())
    .then(response=>{
        if(response.status==200)
        {
            location.reload()
        }
        else
        {
            alert(response.message)
        }
    })
}



function mylike() {
    var use = document.getElementById('use').value;
    var used = document.getElementById('liked').value;
    var csrf = document.getElementById('csrf').value;
    var data = {
        'action':use,
        'onpost':used,
    }
    fetch('/api/like/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrf
        },
        'body': JSON.stringify(data)
    }).then(result=>result.json())
    .then(response=>{
        if(response.status==200)
        {
            location.reload()
        }
        else
        {
            alert(response.message)
        }
    })
}


function myfollow() {
    var use = document.getElementById('use').value;
    var used = document.getElementById('foll').value;
    var csrf = document.getElementById('csrf').value;
    var data = {
        'action':use,
        'person':used,
    }
    fetch('/api/follow/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrf
        },
        'body': JSON.stringify(data)
    }).then(result=>result.json())
    .then(response=>{
        if(response.status==200)
        {
            location.reload()
        }
        else
        {
            alert(response.message)
        }
    })
}