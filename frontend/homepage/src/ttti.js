import ReactDOM from 'react-dom'
import React, { useState } from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'; // version boot react problem
import FusionCharts from "fusioncharts";
import charts from "fusioncharts/fusioncharts.charts";
import ReactFusioncharts from "react-fusioncharts";

import WordCloud from 'react-d3-cloud';



//fusion charts 

charts(FusionCharts);
const dataSource = {
  chart: {
    caption: "Recommended Portfolio Split",
    subcaption: "For a net-worth of $1M",
    showvalues: "1",
    showpercentintooltip: "0",
    numberprefix: "$",
    enablemultislicing: "1",
    theme: "fusion"
  },
  data: [
    {
      label: "MONTREAL",
      value: "0"
    },
    {
      label: "WATERLOO",
      value: "100"
    },
    {
      label: "Bullion",
      value: "180000"
    },
    {
      label: "Real-estate",
      value: "270000"
    },
    {
      label: "Insurance",
      value: "20000"
    }
  ]
};



const data = [
  {
    text: 'told',
    value: 64,
  },
  {
    text: 'mistake',
    value: 11,
  },
  

];



const fontSizeMapper = word => Math.log2(word.value) * 5;
const rotate = word => word.value % 360;

 


class App extends React.Component {
state = {
    array_keyword_object_with_data: [],
  };
 
  append_keyword = (datareturned) => {
  	this.setState(prevState => ({
    	array_keyword_object_with_data: [...prevState.array_keyword_object_with_data, datareturned],
    }));
  };
  
	render() {
  	return (
      
  <React.Fragment>

    <div id="slide" class="cb-slideshow" >
    <ul class="cb-slideshow" >
    <li>
      <span>1</span>
      {}
    </li>
    <li>      
      <span>2</span>
      {}
      </li>
    <li>      
      <span>3</span>
      {}
      </li>
      <li>      
      <span>4</span>
      {}
      </li>
      <li>      
      <span>5</span>
      {}
      </li>
      <li>      
      <span>6</span>
      {}
      </li>
  </ul>
  </div>

  <div id="root" class="jumbotron text-center">
      <h2>We do sentiment Analysis</h2>
        <p> Twitter, Facebook..</p>
      <Form onSubmit={this.append_keyword} />  
      <Keyword_list array_keyword_object_with_data={this.state.array_keyword_object_with_data} /> 
  </div>


<div class="container-fluid bg-grey">

      <span class="glyphicon glyphicon-globe logo"></span>
    <div class="col-sm-8">
      <h1 >HUMAN SENTIMENT ANALYSIS</h1>
      <p></p>
      <p></p>
      <p></p>
      <p><strong>-->ENTER THE KEYWORD IN THE SEARCH BAR ABOVE!</strong> </p>
      <p><strong>-->GET HUMAN SENTIMENT ABOUT THE KEYWORD!</strong> </p>
      <p><strong>-->BOOM !! NO NEED TO CHECK TWITTER!!</strong> </p>

  </div>
</div>

<div class="container-fluid text-center">
  <h1>HOT TOPICS !!!</h1>
  <br></br>
  <div class="row">

    <div class="col-sm-4">

      <h4>DONALD TRUMP</h4>
      <p>Positive Tweets--> ,Negative Tweets--></p>
    </div>

    <div class="col-sm-4">
      <h4>CORONAVIRUS</h4>
      <p>Positive Tweets--> ,Negative Tweets--></p>
    </div>

    <div class="col-sm-4">
      <h4>CHINA</h4>
      <p>Positive Tweets--> ,Negative Tweets--></p>
    </div>

    </div>

    <br></br>

  <div class="row">
    <div class="col-sm-4">

      <h4>ITALY</h4>
      <p>Positive Tweets--> ,Negative Tweets--></p>
    </div>

    <div class="col-sm-4">
      <h4>VACCINE</h4>
      <p>Positive Tweets--> ,Negative Tweets--></p>
    </div>

    <div class="col-sm-4">
      <h4>MAGA2020</h4>
      <p>Positive Tweets--> ,Negative Tweets--></p>
    </div>

  </div>
</div>



<div class="container-fluid bg-grey">
  <h1 class="text-center">CONTACT</h1>
  <div class="row">
    <div class="col-sm-5">
      <p>Contact us for adding new functionality or any other issues you are facing while doing the analysis.</p>
      <p><span class="glyphicon glyphicon-map-marker"></span> Waterloo, ON</p>
      <p><span class="glyphicon glyphicon-phone"></span> +1 222332433434</p>
      <p><span class="glyphicon glyphicon-envelope"></span> info@humansentiment.com</p>
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
          <button class="btn btn-default pull-r ight" type="submit">Send</button>
        </div>
      </div>
    </div>
  </div>
</div>

<footer id="footer" >

    <p class="container-fluid bg-grey"><strong id="headingsize">Disclaimer for Human Sentiment Analysis:: </strong>If you require any more information or have any questions about our site's disclaimer, please feel free to contact us by email at info@humansentiment.com. 
    All the information on this website - Humansentiment.com - is published in good faith and for general information purpose only. Human Sentiment does not make any warranties about the completeness, 
    reliability and accuracy of this information. Any action you take upon the information you find on this website (Human Sentiment), is strictly at your own risk. Human Sentiment will not be liable for any losses and/or damages 
    in connection with the use of our website. Our Disclaimer was generated with the help of the Disclaimer Generator. From our website, you can visit other websites by following hyperlinks to such external sites. While we strive to 
    provide only quality links to useful and ethical websites, we have no control over the content and nature of these sites. These links to other websites do not imply a recommendation for all the content found on these sites. 
    Site owners and content may change without notice and may occur before we have the opportunity to remove a link which may have gone 'bad'..Please be also aware that when you leave our website, other sites may have different 
    privacy policies and terms which are beyond our control. Please be sure to check the Privacy Policies of these sites as well as their "Terms of Service" before engaging in any business or uploading any information.</p>

</footer>

</React.Fragment>
    );
  }	
}

class Company extends React.Component {
	render() {
    const p = this.props;
return(
 <div className="company">
   <span className="companytext"> </span>
    <img src={p.avatar_url}/>

    {/* fusion chart  */}
    <ReactFusioncharts
        type="pie3d"
        width="60%"
        height="60%"
        dataFormat="JSON"
        dataSource={dataSource}
      />
      <WordCloud
    data={data}
    fontSizeMapper={fontSizeMapper}
    rotate={rotate}
  />,

      
  <div className='app-inner'>


  <div className="datareturned">
          <div>Name: {p.name}</div>
          <div>Email: {p.email}</div>
          <div>Bio: {p.bio}</div>
          <div>Repos: {p.public_repos}</div>
          <div></div>
        </div>
    	</div>
      </div>
    );
  }
}
class Keyword_list extends React.Component {
  render() {
    const p = this.props;
      return (
          <div className="companylist">
            
          <span className="companylisttext"></span>
          {p.array_keyword_object_with_data.map(datareturned => <Company key={datareturned.id} {...datareturned}/>)}
          </div>
      );
  }
}


class Form extends React.Component {
  state = { user_keyword: '' };  //1


  handleSubmit = async (event) => {    //2  using hooks . it becomes simpler  ASYNCHRONOUS F UNCTION https://medium.com/@ian.mundy/async-event-handlers-in-react-a1590ed24399
    event.preventDefault();
    const resp = await axios.get(`https://api.github.com/users/${this.state.user_keyword}`);
    this.props.onSubmit(resp.data);                                                                                     //take data from the api and pass it to onsubmit  
    this.setState({ user_keyword: '' });
  };
 	render() {
  	return (
//2
    	<form onSubmit={this.handleSubmit}>    
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
        <button type="button" class="btn btn-danger">DO Analysis!!</button>
      </div>
    	</form>
    );
  }
}
export default App;