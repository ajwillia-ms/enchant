import React from 'react';
import ReactDOM from 'react-dom';
import AddSite from './App';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<AddSite />, div);
});
