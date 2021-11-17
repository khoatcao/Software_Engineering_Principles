
class CountSum{
    // init param 
    constructor(a,b){

        this._a = a;
        this._b = b; 
    }
    // method 
    get add_two_number(){

        return this._a + this._b; 
    }
    // method 
    get substract_two_number(){

        return Math.abs(this._a - this._b); 
    }

    get mutiply_two_number(){
        return this._a * this._b; 
    }
}


const numbers = new CountSum(5,6); 
console.log(numbers.add_two_number);

console.log(numbers.substract_two_number);
console.log(numbers._b);
