// parent class
class Media{
    constructor(title){

        this._title = title; 
        this._isCheckedOut = false; 
        this._ratings = []; 


    }

    get title(){

        return this._title; 
    }

    get isCheckOut(){

        return this._isCheckedOut; 
    }

    get ratings(){
        
        return this._ratings; 
    }

    // setter 

   set isChecedkOut(newCheckOut){

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

        if (rating > 5) {

            console.log("Rating is between 1 and 5"); 

            return 'Rating is between 1 and 5'; 

        }

        this._ratings.push(rating); 



    }
}



// class 1 
class Book extends Media{

    constructor(author,title,pages){
        
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

class Movie extends Media{ 
 constructor(director,title,runTime){

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
    constructor(artist,titlesongs,title){

        super(title); 
        this._artist = artist; 
        this._songs = []; 
    }

    // getter 

    get artists(){
        return this._artists;
    }

    get songs(){
        return this._songs; 
    }

    Shuffle() { 

        
        for (let i = this._songs.length; i > 0 ; i -- ){

            let j = Math.floor(Math.random() * (i+1)); 
                [this._song[i],this._song[j] = this._song[j],this._song[i]]; 
        }



    }

    addSong(newsongs){

        this._songs.push(newsongs); 
    }


}

class Catalog extends Media {

    constructor(medialist,title){
        super(title)
        this._Mycatalog = [medialist]; 

    }

    // getter
    
    get medialist() {
        return this._medialist; 
    }

    set medialist(newmedialist){

        this._Mycatalog.push(newmedialist);
    }
}

const historyOfEverything = new Book('Bill Bryson', 'A Short History of Nearly Everything', 544);

historyOfEverything.toggleCheckOutStatus(); 
console.log(historyOfEverything.isCheckedOut);

historyOfEverything.addRating(4,5,5); 
console.log(historyOfEverything.getAverageRating());

const hobbit = new Book('J.R. Tolkien', 'Hobbit', 744);

const speed = new Movie('Jan de Bont', 'Speed', 116);
speed.addRating(1);
speed.addRating(1);
speed.addRating(5);
console.log(speed.getAverageRating());
const newCd = new CD('Ocean', 'Kasaija Akiiki');
newCd.addSong('Billy Jean');
newCd.addSong('Mafia');
newCd.addSong('Yeke Yeke');
// print newCd 
console.log(newCd); 


const Test = new Catalog();
Test.mediaList = historyOfEverything;
Test.mediaList = speed;
Test.mediaList = hobbit;
Test.medialist = newCd; 
console.log(Test)
