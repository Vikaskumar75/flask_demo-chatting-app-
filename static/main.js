console.log('Hello')
 var socketio = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    // socket.on('connect', function() {
    //     socket.emit('my event', {data: 'I\'m connected!'});
    // });



function send()
	{
		var inputBox = document.getElementById('inputBox')
		socketio.emit('message', inputBox.value)
		inputBox.value = ''
	}

socketio.on('push',function(data)
					{
						var chatBox = document.getElementById('chatBox')
						chatBox.innerHTML += '<p>'+data+ '</p>'
						// chatBox.innerHTML += `<p>${data}</p>`
					})



function getUsers()
	 {
		fetch('/users').then(function(res)
			{
				res.json().then(function(data)
								{
									console.log(data)
								})
	})

}













