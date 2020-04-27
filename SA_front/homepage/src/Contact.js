

import ReactDOM from 'react-dom'
import React, { useState } from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'; // version boot react problem
<div class="contact">
<div class="container-fluid bg-grey">
{/* REMOVE ABOVE COMMENT TO MAKE A SOLID BACKGROUND THAT WE HAVE DONE EARLIER */}

  <h1 class="text-center" id="inner2"><strong>CONTACT US</strong></h1>
  <div class="row">
    <div class="col-sm-5" >
      <p id="inner2">Contact us for adding new functionality or any other issues you are facing while doing the analysis.</p>
      <p id="inner2"> <span class="glyphicon glyphicon-map-marker"></span> Waterloo, ON</p>
      <p id="inner2"><span class="glyphicon glyphicon-phone"></span> +1 222332433434</p>
      <p id="inner2"><span class="glyphicon glyphicon-envelope"></span> info@humansentiment.com</p>
    </div>
    <div class="col-sm-7">
      <div class="row">
        <div class="col-sm-6 form-group">
          <input class="form-control" id="name" name="name" placeholder="Name" type="text" required></input>
        </div>
        <div class="col-sm-6 form-group">
          <input class="form-control" id="email" name="email" placeholder="Email" type="email" required></input>
        </div>
      </div>
      <textarea class="form-control" id="comments" name="comments" placeholder="Comment" rows="5"></textarea><br></br>
      <div class="row">
        <div class="col-sm-12 form-group">
          <button class="btn btn-danger" type="submit" >Send</button>
          
        </div>
      </div>
    </div>
  </div>
</div>
</div>
export default Form;

