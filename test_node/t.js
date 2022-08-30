function concat(s1, s2) {
    return s1 + s2;
}
function add(num1, num2) {
    return Number(num1) + Number(num2);
}

//新增一个导出函数（node方式）
module.exports.init = function (arg1, arg2) {
    //调用函数，并返回
    console.log(concat(arg1, arg2));
};

console.log(concat(process.argv[2], process.argv[3]))
// console.log(add(process.argv[2] ?? 0, process.argv[3] ?? 1))

const map1 = new Map()

const d = {a:1, c:3, b:2}
d[Symbol('abc')] = 10
console.log(d.__proto__)
for (const t in d) {
    console.log(t, d[t])
}

const m = new Map()
m.set('a', 1)
m.set('b', 2)
m.set('c', 3)
m.set(Symbol('abc'), 10)
console.log(m)
for (const t of m) {
    console.log(t)
}

const t = {}
console.log(t.__proto__ === Object.prototype)
console.log(Object.getPrototypeOf(t))
console.log(add.prototype)

const a = new add(1, 2)
a.a = 10
console.log(a)

function Person() {}

const p = new Person;
console.log(Object.getOwnPropertyDescriptors(Person.prototype))

var obj = {
    name : 'why',
    age:18
}

Object.defineProperty(obj,"address",{
    value:'北京',
    //假如不写 下面三个参数的默认值都是false
    // configurable:false,
    // enumerable:false,
    // writable:false, 
})

// Object.freeze(obj)
obj.address = '上海'
console.log(obj.address); //北京
delete obj.address 
console.log(obj.address); //北京并没被删除
for(let value in obj){
    console.log(value);  //北京没有被打印出来
}

// import axios from "axios";
const axios = require('axios')

axios.all([
    axios.get(''),
    axios.get('https://www.cnblogs.com/ltfxy/p/12515307.html')
]).then((resp) => {
    console.log(resp[0].data)
    console.log(resp[1].data)
})