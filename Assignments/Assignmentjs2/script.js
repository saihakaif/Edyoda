// // Question 1:

// var any1 = [1, 2, 3, 4, 5, 1, 3];
// var any2 = [];

// var searchelement = 4;

// for ( var i=0; i<any1.length; i++){
//     if(any1[i] == searchelement){
//         any2.push(i);
//       }
//   }


//   if(any2 == ""){
//     console.log(-1);
//   }else{
//     console.log(any2);
//   }


// Question 2:

// for (var i=1; i<=5; i++ ){
//     var pattern="";
//     for (var j=5; j>=i; j--){
//         pattern = pattern +j;
//     }
   
//     console.log(pattern);
// }

// Question 3:


// let array = [3, 2, 1, 4, 5, 45];
// array.sort( function (a , b){
//     if(a > b) return 1;
//     if(a < b) return -1;
//     return 0;

// });

// console.log (array);



// Question 4:

// const isAnagram = (str1, str2) => {
//   const normalize = str =>
//     str
//       .toLowerCase()
//       .replace(/[^a-z0-9]/gi, '')
//       .split('')
//       .sort()
//       .join('');
//   return normalize(str1) === normalize(str2);
// };
// console.log(isAnagram('LISTEN', 'SILENT')); 
// console.log(isAnagram('HELLO', 'JELLO'));


// Question 5:

// function reverse1(str){
//   let r = "";
//   for(let i = str.length-1; i >= 0; i--){
//     r += str[i];
//   }
//   return r;
// }

// console.log(reverse1("Hello"))