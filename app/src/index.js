import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import AddSite from './App';

var addsitenode = document.getElementById('addsite');
if (addsitenode)
  ReactDOM.render(<AddSite />, addsitenode);

