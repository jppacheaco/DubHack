import './App.css';
// import { useState, useEffect } from 'react';

// function App() {
//   useEffect(() => {
//     fetch('/test')
//     .then(res => res.text())
//     .then(console.log)
//   })
//   return ;
// }
import {ContactPage} from './Pages/ContactPage';

function App() {
  return (
    <div className="App">
      <ContactPage />
    </div>
  );
}

export default App;

//ask if free is an api
//calculate distance
