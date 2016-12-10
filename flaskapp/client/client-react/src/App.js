import React, { Component } from 'react';
// import Spells from './components/spells';
import Monsters from './components/monsters';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

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

        <Monsters monsters={this.state.monsters} />
        {/*<Spells spells={this.state.spells}/>*/}
      </div>
    );
  }
}


export default App;
