const mixedMessages = {
    greetings: ['Hi', 'Hello', 'Good morning', 'Good afernoon', 'Hey'],
    names: ['Ross', 'Rachel', 'Monica', 'Joey', 'Chandler', 'Phoebe'],
    questions: [
      'What’s your favorite book?',
      'Do you like to cook?',
      'What’s on your bucket list?',
      'What do you do for a living?',
      'Do you believe in luck?',
      'What’s your hidden talent?'
    ],
    getRandomItem(arr) {
      const randomIndex = Math.floor(Math.random() * arr.length);
      return arr[randomIndex];
    },
    createMessage() {
      const greeting = this.getRandomItem(this.greetings);
      const name = this.getRandomItem(this.names);
      const question = this.getRandomItem(this.questions);
      return `${greeting}, ${name}. ${question}`;
    },
    logMessage() {
      console.log(this.createMessage());
    }
  };
  
  mixedMessages.logMessage();