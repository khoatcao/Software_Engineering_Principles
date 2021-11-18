// parent class
class Media{
    constructor(title){

        this._title = title; 
        this._isCheckOut = False; 
        this._ratings = []; 

    }

    get title(){

        return this._title; 
    }

    get _isCheckOut(){

        return this._isCheckOut; 
    }

    get ratings(){
        
        return this._ratings; 
    }

    // setter 

   set isCheckOut(newCheckOut){

    this._isCheckOut = newCheckOut; 

    }

    // method 

    toggleCheckOutStatus(){

        this._isCheckOut = !this._isCheckOut; 

    }

    getAverageRating()
    {
      let ratingSum = this._ratings.reduce((currentSum,rating) => currentSum + rating,0); 

      const lenofarray = this._ratings.length; 


      return ratingSum/lenofarray; 
    }


    addRating(rating){

       this._ratings.push(rating);



    }
}



// class 1 
class Book extends Media{

    constuctor(author,title,pages){
        
        super(title); 
        this._author = author;
        this._pages = pages; 

    }

    // getter 


    get author(){
        return this._author; 
    }

    get pages(){
        return this._pages; 
    }

    // methods 
    getAverageRating(){

    }

    toggleCheckOutStatus(){

    }

    addRating()
    {

    }
}


// class 2 

class Movie extends media{ 
 constuctor(director,title,runTime){

    super(title);

    this._director = director; 
    this._runTime = runTime;
 }
 // getter 
 get director(){
     return this._director;

 }

 get runTime(){

    return this._runTime;
 }

 // method 

 getAverageRating(){

 }

 toggleCheckOutStatus(){

 }

 addRating(){

 }
}

// class 3 

class CD extends Media {
    constructor(artist,titlesongs){

        super(title); 
        this._artist = artist; 
        this._songs = songs; 
    }

    // getter 

    get artists(){
        return this._artists;
    }

    get songs(){
        return this._songs; 
    }

    // methods 
    getAverageRating(){


    }
    
    toggleCheckOutStatus(){

    }
    addRating(){

    }
}


const historyOfEverything = new Book('Bill Bryson', 'A Short History of Nearly Everything', 544);
const speed = new Movie('Jan de Bont', 'Speed', 116);

historyOfEverything.toggleCheckOutStatus(); 
console.log(historyOfEverything.isCheckedOut);

historyOfEverything.addRating(4,5,5); 
console.log(historyOfEverything.getAverageRating());

