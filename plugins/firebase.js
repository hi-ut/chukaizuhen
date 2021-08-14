import firebase from 'firebase'

if (!firebase.apps.length) {
  firebase.initializeApp({
    apiKey: "AIzaSyCQJq5w0NLHWFhXEHg94qf2dEHxHfHAgrs",
    authDomain: "kunshujo.firebaseapp.com",
    projectId: "kunshujo",
    storageBucket: "kunshujo.appspot.com",
    messagingSenderId: "767668937895",
    appId: "1:767668937895:web:cc05564c1dca8e22f0e782"
  })
}

export default firebase
