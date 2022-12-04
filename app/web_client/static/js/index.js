function ListBook(){
    const query = `
    query  {  
        books{
            id
            title
            description
            author{
                name
            }
            genre{
                title
            }
        }
    }`;
    const elem = document.getElementById('contetnt');    


    let data = fetch("http://localhost:8000/api/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
          },
        body: JSON.stringify({
            query: query
        })
    }).then(res => res.json())
    .then(res => res.data.books);
    
    // console.log(elem)
    console.log(data)
}

// ListBook()