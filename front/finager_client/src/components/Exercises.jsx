import React, { Component } from 'react';
import PropTypes from 'prop-types';

import Exercise from './Exercise';

class Exercises extends Component {
  constructor (props) {
    super(props)
    this.state = {
    };
  };

  componentDidMount() {
  };

  render() {
    return (
      <div>
        <h1>Exercises</h1>
        <hr/><br/>
        {!this.props.isAuthenticated &&
          <div>
            <div className="alert alert-warning">
              <span
                className="glyphicon glyphicon-exclamation-sign"
                aria-hidden="true">
              </span>
              <span>&nbsp;Please log in.</span>
            </div>
            <br/>
          </div>
        }

        <Exercise
          isAuthenticated={this.props.isAuthenticated}
        />

      </div>
    )
  };
};

Exercises.propTypes = {
  isAuthenticated: PropTypes.bool.isRequired,
};

export default Exercises;
