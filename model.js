 let employ = {
    "_id" : 1,
    "name": "albert",
    "email" : "albert@gmail.com",
    "address" : {
        "city": "delhi",
        "pin_code": "1234"
    },
    "age": "40",
    "hobbies": ["acting", "reading", "playing"]

}

console.log(employ)
console.log(employ._id, employ.email, employ.address.pin_code, employ.hobbies[2]);
