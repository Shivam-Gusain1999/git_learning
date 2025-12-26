// function mailCheck(){
//     return new Promise((resolve, reject)=>{
//         if(Math.random() > 0.8){
//             resolve("mail arrived")
//         }
//         else{
//             reject("mail rejected")

//         }
//     }
// )}
// mailCheck()
// .then((result)=>{
//     console.log(result)
// }).catch((galti)=>{
//     console.log(galti);
    
// }).finally(()=>{
//     console.log("email completed successfully");
    
// })



// object // 

// const source = {
//     a : 1,
//     b : 2,
//     c : 3
// }
// const target = {
//     c: 4,
//     d : 5,
//     e : 6
// }
// const targetValue = Object.assign(source, target)
// console.log(targetValue)
// console.log(targetValue === source);
// console.log(source)



// spread syntax //

// function sum (a, b, c, d) {
//     return a + b + c - d
// }

// let num = [1,2,7,5]
// console.log(sum(...num));



// nullish coalscing //

// const a = {
//     duration : 35
// }
// a.time ??= 10;
// console.log(a.time);

// // a.duration = 20;
// // console.log(a.duration)

// a.duration ??= 40;
// console.log(a.duration)   



// some more examples... //

let a = 20;
a ??= 0;
console.log(a)

let b = 0;
b ??= 15;
console.log(b)

let c = null;
c ??= 42;
console.log(c)

let d = false;
d ||= 2;
console.log(d)


let e = true;
e ||= 12;
console.log(e)



