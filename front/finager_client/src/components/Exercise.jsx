import React from 'react';
import PropTypes from 'prop-types';

const Exercise = (props) => {
  return (
    <div>
        {props.isAuthenticated &&
          <h4> Authenticated? </h4>
        }
      <br/><br/>
    </div>
  )
};

Exercise.propTypes = {
  isAuthenticated: PropTypes.bool.isRequired,
};

export default Exercise;
