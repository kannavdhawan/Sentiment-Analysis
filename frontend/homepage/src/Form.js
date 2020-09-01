
import ReactDOM from 'react-dom'
import React, { useState } from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'; // version boot react problem

class Form extends React.Component {
    state = { user_keyword: ''};  //1
  
  
    handleSubmit = async (event) => {    //2  using hooks . it becomes simpler  ASYNCHRONOUS F UNCTION https://medium.com/@ian.mundy/async-event-handlers-in-react-a1590ed24399
      event.preventDefault();
      console.log(this.user_keyword)
      const resp = await axios.get(`http://localhost:5000/word?place=${this.state.user_keyword}`, {headers:{'Access-Control-Allow-Origin':'*'}});
      this.props.onSubmit(resp.data);  
      console.log(this.props.p)
      // this.setState({resp1:resp})                                                                                   //take data from the api and pass it to onsubmit  
      this.setState({ user_keyword: '' });
    };
       render() {
        return (
  //2
          <form onSubmit={this.handleSubmit}  >
        {/* // <form  action="http://localhost:5000/word" method="GET">  */}
        
        <div class="input-group">
        <span className="formtext"></span>
            <input 
            type="text" 
            value={this.state.user_keyword}    //1
            onChange={event => this.setState({ user_keyword: event.target.value })}   //1
            //<input value={this.state.value} onChange={this.handleChange} />
            placeholder="Enter keywords.." 
            class="form-control"
            size="50"
            required 
          />
  
          <button type="submit" class="btn btn-danger" >DO Analysis!!</button>
        </div>
          </form>
      );
    }
  }
  export default Form;
  