function consult_user(){
    let id_user = document.getElementById("ident").value
    let obj_user = {
         "id": id_user
    }
     fetch("/consult_user", {
         "method": "post",
         "headers":{"Content-Type":"applicaation/json"},
         "body":JSON.stringify(obj_user)
     })
     .then(resp => resp.json())
     .then(data => {
        alert(data)
     })
     .catch(err => {
          alert("Error" + err)
     })
 }