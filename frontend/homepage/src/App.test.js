import ReactDOM from 'react-dom'
import React, { useState } from 'react';

function Button(props) {
	return (
  	<button onClick={props.onClickFunction}>
      "Click To Increment!"
    </button>
  );
}
function Presentation(props) {
	return (
  	<li>{props.message}</li>
  );
}
 
function App() {
	const [counter, setCounter] = useState(0);
  const incrementCounter = () => setCounter(counter+1);
	return (
    <div>
      <Button onClickFunction={incrementCounter} increment={1} />
      <Presentation message={counter}/>
    </div>  
  );
}
 




ReactDOM.render(
  <App />, 
  document.getElementById('root'),
);
 
export default App;