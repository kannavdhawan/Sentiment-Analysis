
import React from 'react'
import App from '../components/App'
import { shallow } from 'enzyme'
import ReactDOM from 'react-dom'
import React, { useState } from 'react';


function Button(props) {
	return (
  	<button onClick={props.onClickFunction}>
      "Click To Increment!"
    </button>
  );
}