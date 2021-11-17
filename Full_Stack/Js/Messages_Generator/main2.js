// create the messages which I want to generate 

var mixedMessages = [
    'The greatest glory in living lies not in never falling, but in rising every time we fall',
    'The way to get started is to quit talking and begin doing',
    'Your time is limited, so dont waste it living someone elses life. Dont be trapped by dogma – which is living with the results of other peoples thinking',
    'Life is what happens when you are busy making other plans',
    'Spread love everywhere you go. Let no one ever come to you without leaving happier',
    'When you reach the end of your rope, tie a knot in it and hang on',
    'Always remember that you are absolutely unique. Just like everyone else',
    'Do not judge each day by the harvest you reap but by the seeds that you plant'

]


var Messages = [

    'The purpose of our lives is to be happy',
    'Life is what happens when you’re busy making other plans',
    'You only live once, but if you do it right, once is enough'
]




function getmessagesrandom(mixedMessages){

    return mixedMessages[Math.floor(Math.random()*mixedMessages.length)];


}

console.log(getmessagesrandom(mixedMessages));



function getRandomindex(mixedMessages){

    return Math.floor(Math.random()*mixedMessages.length); 
}


console.log(getRandomindex(mixedMessages));




function getfullmessages(mixedMessages,messages){


    return mixedMessages[Math.floor(Math.random()*mixedMessages.length)] + " " + Messages[Math.floor(Math.random()*messages.length)];
}


console.log(getfullmessages(mixedMessages,Messages));