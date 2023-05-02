const firebaseApp = firebase.initializeApp({ 
  apiKey: "AIzaSyASlWcGUwzm9CAMT99JeVFitE4vuwXIdqs",
  authDomain: "quiz-web-project.firebaseapp.com",
  databaseURL: "https://quiz-web-project-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "quiz-web-project",
  storageBucket: "quiz-web-project.appspot.com",
  messagingSenderId: "962859214784",
  appId: "1:962859214784:web:18c5320dc93b05cf5e4a25"
});


const db = firebaseApp.firestore();
const auth = firebaseApp.auth();

//signup funk 
const signUp=()=>{
    const email = document.getElementById("email1").value;
    const password = document.getElementById("pass1").value;
    console.log(email, password)
    
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((result) => {
        // Signed in 
        document.write("You are Sign up");
        console.log(result)
        // ...
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message)
        
        // ..
    });
}

const signIn=()=> {
    const email = document.getElementById("email").value;
    const password = document.getElementById("pass").value;
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then((result) => {
            // Signed in
            document.write("You are Sign in");
            console.log(result)
            // ...
        })
        .catch((error) => {
            console.log(error.code);
            console.log(error.message)
        });

}