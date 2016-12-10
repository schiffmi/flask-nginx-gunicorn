import React, { Component } from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {monsters: [], spells: []};
  }
  componentWillMount() {
    axios.get('api/monsters')
      .then(response => this.setState({monsters: response.data.monsters }) )
      .catch(e => console.log('Error', e));
    axios.get('api/spells') 
      .then(response => this.setState({spells: response.data.spells }) )
      .catch(e => console.log('Error', e));

  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}


export default App;
