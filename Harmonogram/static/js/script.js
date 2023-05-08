console.log('hello world')
const helloWorldBox = document.getElementById('rowsd')
const storeBox = document.getElementById('rowsd')

$.ajax({
    type: 'GET',
    url: "/json_view/",
    success: function(response) {
        console.log('success', response.text)
        helloWorldBox.textContent = response.text
    },
    error: function(error){
        console.log('error', error)
    }
})

$.ajax({
    type: 'GET',
    url: '/json_view',
    success: function(response){
        console.log(response)
        const data = response.data
        console.log(data)
        data.forEach(el =>{
            storeBox.innerHTML += `
                ${el.id} - <b>${el.name}</b><br>

            `

        });
    },
    error: function(error){
        console.log(error)
    }

})